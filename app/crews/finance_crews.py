from crewai import Crew, Task
from app.agents.finance.accounts_payable import accounts_payable_agent
from app.agents.finance.accounts_receivable import accounts_receivable_agent
from app.agents.finance.risk import finance_risk_agent

def run_accounts_payable(task_name: str, payload: dict):
    t = Task(
        description=f"Process vendor invoices with meticulous attention to detail, ensuring compliance with payment terms and company policies. Detect anomalies and maintain audit trails. Task: {task_name}",
        expected_output="A detailed accounts payable report including invoice validation results, discrepancy findings, approval recommendations, and audit trail documentation with compliance verification."
    )
    crew = Crew(agents=[accounts_payable_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_accounts_receivable(task_name: str, payload: dict):
    t = Task(
        description=f"Optimize accounts receivable processes to accelerate cash collection while maintaining positive customer relationships. Forecast cash flows and implement collection strategies. Task: {task_name}",
        expected_output="An accounts receivable analysis including cash flow forecasts, aging report insights, collection strategy recommendations, and DSO improvement plans with projected financial impact."
    )
    crew = Crew(agents=[accounts_receivable_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_finance_risk(task_name: str, payload: dict):
    t = Task(
        description=f"Conduct comprehensive financial risk assessments to identify potential fraud, operational inefficiencies, and compliance violations. Provide detailed investigative findings. Task: {task_name}",
        expected_output="A financial risk assessment report detailing identified anomalies, fraud indicators, risk levels, investigative findings, and recommended mitigation strategies with implementation priorities."
    )
    crew = Crew(agents=[finance_risk_agent], tasks=[t])
    return crew.kickoff(inputs=payload)
