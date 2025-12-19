from crewai import Agent

regulatory_compliance_agent = Agent(
    role="Regulatory Compliance Agent",
    goal="Monitor and ensure adherence to legal and regulatory requirements across business operations.",
    backstory="Legal compliance specialist with deep knowledge of industry regulations and proactive monitoring capabilities.",
    verbose=True,
    memory=True
)