from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_community.llms import Ollama
# from langchain_community.tools.python import PythonREPLTool
from langchain.memory import ConversationBufferMemory
from retriever.vector_store import load_vector_store
from retriever.web_retrievers import WebRetriever, WikipediaRetriever
from langchain.tools import Tool

def safe_eval(code: str):
    try:
        return str(eval(code))
    except Exception as e:
        return str(e)

PythonREPLTool = Tool.from_function(
    name="Python Executor",
    func=safe_eval,
    description="Use this for simple math or Python-based code execution."
)
def search_pdf(query):
    store = load_vector_store()
    docs = store.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])

def search_web(query):
    retriever = WebRetriever()
    docs = retriever.retrieve(query)
    return "\n".join([doc.page_content for doc in docs])

def search_wikipedia(query):
    retriever = WikipediaRetriever()
    docs = retriever.retrieve(query)
    return "\n".join([doc.page_content for doc in docs])

llm = Ollama(model="llama3.2")
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

tools = [
    Tool(name="PDF Search", func=search_pdf, description="Use for course or book questions"),
    Tool(name="Web Search", func=search_web, description="Use for general or recent info from web"),
    Tool(name="Wikipedia Search", func=search_wikipedia, description="Use for encyclopedic or factual context"),
    PythonREPLTool
]

chat_agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory
)

def run_chat_agent(user_input):
    return chat_agent.run(user_input)