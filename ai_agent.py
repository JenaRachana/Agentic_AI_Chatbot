# step-1: Setup api keys for GROQ, OPENAI and Tavily 

import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPEN_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


# step-2 : Setup LLMS & Tools

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI   # llm
from langchain_tavily import TavilySearch # tool
from langchain.agents import create_agent   


openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
search_tool = TavilySearch(max_results=2)

# setup-3 : Setup AI Agent with Search Tool functionality

# from langgraph.prebuilt import create_react_agent


from langchain.agents import create_agent
from langchain_core.messages.ai import AIMessage
from langchain_core.messages import HumanMessage

# system_prompt="Act As an Ai chatbot who is smart and friendly"

# agent = create_agent(
#     model=groq_llm,
#     tools=[search_tool],
#     system_prompt=system_prompt
# )
# query="who is the president of india"
# state={"messages": [HumanMessage(content=query)]}
# response = agent.invoke(state)
# messages = response.get("messages")
# ai_message=[i.content for i in messages if isinstance(i, AIMessage)]
# return ai_message[-1])



def get_response_from_ai_agent(llm_id,query,allow_search,provider,system_prompt):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)
    
    tools = [TavilySearch(max_result=2)] if  allow_search else []
    agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt
    )
    state={"messages": [HumanMessage(content=query)]}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_message=[i.content for i in messages if isinstance(i, AIMessage)]
    return ai_message[-1]