from mcp_tools.calendar_tools import get_meetings


def calendar_node(state):

    state.meetings = get_meetings()

    return state