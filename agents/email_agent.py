from mcp_tools.email_tools import search_emails


def email_node(state):

    state.emails = search_emails()

    return state
