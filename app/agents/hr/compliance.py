from crewai import Agent

hr_compliance_agent = Agent(
    role="HR Compliance Agent",
    goal="Validate HR documents and workflows against policy rules and produce an audit trail.",
    backstory="Compliance-focused agent that flags risk early and documents decisions clearly.",
    verbose=True,
    memory=True
)
