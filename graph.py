from typing import TypedDict


class AssistantState(TypedDict):
    user_query: str

    plan: str

    meetings: list

    notes: list

    documents: list

    emails: list

    final_report: str