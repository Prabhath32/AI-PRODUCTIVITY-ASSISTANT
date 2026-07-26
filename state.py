from pydantic import BaseModel, Field


class AssistantState(BaseModel):
    user_query: str

    plan: str = ""

    meetings: list = Field(default_factory=list)

    notes: list = Field(default_factory=list)

    documents: list = Field(default_factory=list)

    emails: list = Field(default_factory=list)

    final_report: str = ""