"""FastAPI interface for an intentionally deterministic text-retrieval baseline."""

from fastapi import FastAPI, Request
from fastapi.responses import Response
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from starlette.middleware.base import RequestResponseEndpoint

from app.scoring import rank_documents, tokenize


class Document(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1, max_length=64, pattern=r"^[A-Za-z0-9_-]+$")
    text: str = Field(min_length=1, max_length=2000)


class RankRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str = Field(min_length=1, max_length=500)
    documents: list[Document] = Field(min_length=1, max_length=20)
    top_k: int = Field(default=5, ge=1, le=20)

    @field_validator("query")
    @classmethod
    def require_word_token(cls, value: str) -> str:
        if not tokenize(value):
            raise ValueError("query must contain a word token")
        return value

    @model_validator(mode="after")
    def require_unique_ids(self) -> "RankRequest":
        ids = [document.id for document in self.documents]
        if len(ids) != len(set(ids)):
            raise ValueError("document IDs must be unique")
        return self


class RankMatch(BaseModel):
    id: str
    score: float
    matched_terms: list[str]


class RankResponse(BaseModel):
    matches: list[RankMatch]
    algorithm: str = "query_term_recall_v1"


app = FastAPI(title="Lexical Retrieval Baseline", version="0.1.0")


@app.middleware("http")
async def no_store_response(
    request: Request, call_next: RequestResponseEndpoint
) -> Response:
    response: Response = await call_next(request)
    response.headers["Cache-Control"] = "no-store"
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.get("/healthz")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/rank", response_model=RankResponse)
def rank(request: RankRequest) -> RankResponse:
    results = rank_documents(
        request.query,
        [(document.id, document.text) for document in request.documents],
        request.top_k,
    )
    return RankResponse(
        matches=[
            RankMatch(id=item.id, score=item.score, matched_terms=list(item.matched_terms))
            for item in results
        ]
    )
