from config import llm


def planner_agent(user_query: str):

    prompt = f"""
    You are a planning agent.

    User request:
    {user_query}

    Decide which information is required.

    Return ONLY a comma-separated list using these names:
    calendar, notes, documents, emails

    Example:
    calendar,notes,documents,emails
    """

    response = llm.invoke(prompt)

    return response.content.strip().lower()