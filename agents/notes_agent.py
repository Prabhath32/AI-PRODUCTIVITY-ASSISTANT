from mcp_tools.notes_tools import search_notes


def notes_node(state):

    state.notes = search_notes()

    return state