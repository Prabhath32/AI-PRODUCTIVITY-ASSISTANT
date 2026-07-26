from config import llm


def summary_agent(meetings, notes, documents, emails):

    prompt = f"""
    You are an AI Productivity Assistant.

    Prepare a meeting preparation report.

    Meetings:
    {meetings}

    Notes:
    {notes}

    Documents:
    {documents}

    Emails:
    {emails}

    Generate:

    1. Meeting Summary

    2. Important Discussion Points

    3. Things To Remember

    4. Checklist
    """

    response = llm.invoke(prompt)

    return response.content