from crewai import Agent

litigation_support_agent = Agent(
    role="Litigation Support Agent",
    goal="Assist legal teams with case preparation, evidence organization, and legal research.",
    backstory="Legal research expert skilled in organizing case materials and conducting thorough legal analysis.",
    verbose=True,
    memory=True
)