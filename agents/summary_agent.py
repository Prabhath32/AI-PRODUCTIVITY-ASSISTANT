from config import llm


def summary_node(state):

    prompt = f"""
    Prepare a meeting report.

    Meetings:
    {state.meetings}

    Notes:
    {state.notes}

    Documents:
    {state.documents}

    Emails:
    {state.emails}

    Include:

    Meeting Summary

    Discussion Points

    Checklist
    """

    response = llm.invoke(prompt)

    state.final_report = response.content

    return state