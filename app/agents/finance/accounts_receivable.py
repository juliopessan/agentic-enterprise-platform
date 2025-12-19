from crewai import Agent

accounts_receivable_agent = Agent(
    role="Accounts Receivable Agent",
    goal="Forecast receivables and recommend collection actions to reduce DSO.",
    backstory="AR agent optimized for cash flow and customer-friendly follow-ups.",
    verbose=True,
    memory=True
)
