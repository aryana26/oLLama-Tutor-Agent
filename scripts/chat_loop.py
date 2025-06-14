import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.chat_agent import run_chat_agent

if __name__ == "__main__":
    print("\n🤖 Tutor Agent Ready. Type 'exit' to quit.\n")
    while True:
        query = input("You: ")
        if query.lower() in ("exit", "quit"): break
        response = run_chat_agent(query)
        print("Tutor:", response, "\n")
