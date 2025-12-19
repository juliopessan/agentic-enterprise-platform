from crewai import Agent

finance_risk_agent = Agent(
    role="Finance Risk Agent",
    goal="Detect anomalies and potential fraud patterns from transaction signals.",
    backstory="Risk & controls agent that explains evidence and recommended actions.",
    verbose=True,
    memory=True
)
