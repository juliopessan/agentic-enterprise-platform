from crewai import Crew, Task
from app.agents.legal.contract_review import contract_review_agent
from app.agents.legal.compliance_monitoring import regulatory_compliance_agent
from app.agents.legal.litigation_support import litigation_support_agent

def run_contract_review(task_name: str, payload: dict):
    t = Task(description=f"{task_name}: Use payload to complete the task and return structured output.")
    crew = Crew(agents=[contract_review_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_compliance_monitoring(task_name: str, payload: dict):
    t = Task(description=f"{task_name}: Use payload to complete the task and return structured output.")
    crew = Crew(agents=[regulatory_compliance_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_litigation_support(task_name: str, payload: dict):
    t = Task(description=f"{task_name}: Use payload to complete the task and return structured output.")
    crew = Crew(agents=[litigation_support_agent], tasks=[t])
    return crew.kickoff(inputs=payload)