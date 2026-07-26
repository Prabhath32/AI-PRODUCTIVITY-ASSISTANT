from agents.planner import planner_agent
from agents.calendar_agent import calendar_agent
from agents.notes_agent import notes_agent
from agents.document_agent import document_agent
from agents.email_agent import email_agent
from agents.summary_agent import summary_agent

query = input("Ask: ")

plan = planner_agent(query)

print("Plan:", plan)

meetings = calendar_agent()

notes = notes_agent()

documents = document_agent()

emails = email_agent()

report = summary_agent(
    meetings,
    notes,
    documents,
    emails
)

print(report)