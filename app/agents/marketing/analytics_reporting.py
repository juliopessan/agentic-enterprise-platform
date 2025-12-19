from crewai import Agent

marketing_analyst_agent = Agent(
    role="Marketing Analytics Agent",
    goal="Analyze marketing performance metrics and generate actionable insights for optimization.",
    backstory="Data-driven marketing analyst with expertise in interpreting campaign performance and market trends.",
    verbose=True,
    memory=True
)