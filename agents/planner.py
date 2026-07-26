from state import AssistantState
from config import llm


def planner_node(state: AssistantState):

    prompt = f"""
    User request:
    {state.user_query}

    Decide required information.

    Return only:
    calendar,notes,documents,emails
    """

    response = llm.invoke(prompt)

    state.plan = response.content.strip().lower()

    return state