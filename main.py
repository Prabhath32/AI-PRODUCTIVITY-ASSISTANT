from graph import graph
from state import AssistantState

query = input("Ask: ")

state = AssistantState(
    user_query=query
)

result = graph.invoke(state)

print("\n")
print(result["final_report"])