from langgraph.graph import StateGraph, END

from state import AssistantState

from agents.planner import planner_node
from agents.calendar_agent import calendar_node
from agents.notes_agent import notes_node
from agents.document_agent import document_node
from agents.email_agent import email_node
from agents.summary_agent import summary_node

builder = StateGraph(AssistantState)

builder.add_node("planner", planner_node)
builder.add_node("calendar", calendar_node)
builder.add_node("notes", notes_node)
builder.add_node("documents", document_node)
builder.add_node("emails", email_node)
builder.add_node("summary", summary_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "calendar")
builder.add_edge("calendar", "notes")
builder.add_edge("notes", "documents")
builder.add_edge("documents", "emails")
builder.add_edge("emails", "summary")
builder.add_edge("summary", END)

graph = builder.compile()