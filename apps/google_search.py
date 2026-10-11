from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent,AgentState
from langgraph.checkpoint.memory import InMemorySaver
import streamlit as st
load_dotenv()
from langchain_groq import ChatGroq
llm_groq = ChatGroq(model="openai/gpt-oss-20b")

st.title("Google Search with Groq")
st.markdown("This is a simple Google Search app using Groq model from OpenAI and Google Serper API.")
search = GoogleSerperAPIWrapper()
query = st.text_input(
"Enter your search query",
key="google_search_query"
)
class CustomAgentState(AgentState):
    user_id: str
    preferences: dict
if st.button("Search"):
    if query:
        st.write(f"Searching for: {query}")
        agent = create_agent(model=llm_groq, tools=[search.run], system_prompt="You are a search expert. You can perform web searches using the Google Serper API. Use the tools provided to you to perform the searches.",
                             state_schema=CustomAgentState,
                        checkpointer=InMemorySaver())
        message = {"messages": [{"role": "user", "content": query}]}
        response = agent.invoke(message,{"configurable": {"thread_id": "1"}})
        #response = agent.invoke()
        st.write(response["messages"][-1].content)
