
# smolagent_ai.py

from smolagents import CodeAgent, DuckDuckGoSearchTool
from smolagents.llms import OpenAIChat

# Initialize the LLM
llm = OpenAIChat(model="gpt-4o-mini")

# Initialize the agent
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],  # built-in search tool
    llm=llm,
    description="You are an AI agent that helps users learn about AI and search the web."
)

# Run the agent
query = "Summarize the latest news about AI agents in 3 lines."
response = agent.run(query)

print("Agent:", response)

