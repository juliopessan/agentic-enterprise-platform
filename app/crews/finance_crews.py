from crewai import Crew, Task
from app.agents.finance.accounts_payable import accounts_payable_agent
from app.agents.finance.accounts_receivable import accounts_receivable_agent
from app.agents.finance.risk import finance_risk_agent

def run_accounts_payable(task_name: str, payload: dict):
    t = Task(description=f"{task_name}: Use payload to complete the task and return structured output.")
    crew = Crew(agents=[accounts_payable_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_accounts_receivable(task_name: str, payload: dict):
    t = Task(description=f"{task_name}: Use payload to complete the task and return structured output.")
    crew = Crew(agents=[accounts_receivable_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_finance_risk(task_name: str, payload: dict):
    t = Task(description=f"{task_name}: Use payload to complete the task and return structured output.")
    crew = Crew(agents=[finance_risk_agent], tasks=[t])
    return crew.kickoff(inputs=payload)
