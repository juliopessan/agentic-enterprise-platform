from crewai import Crew, Task
from app.agents.hr.talent_ops import talent_acquisition_agent
from app.agents.hr.people_lifecycle import onboarding_agent
from app.agents.hr.compliance import hr_compliance_agent

def run_talent_ops(task_name: str, payload: dict):
    t = Task(description=f"{task_name}: Use payload to complete the task and return structured output.")
    crew = Crew(agents=[talent_acquisition_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_people_lifecycle(task_name: str, payload: dict):
    t = Task(description=f"{task_name}: Use payload to complete the task and return structured output.")
    crew = Crew(agents=[onboarding_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_hr_compliance(task_name: str, payload: dict):
    t = Task(description=f"{task_name}: Use payload to complete the task and return structured output.")
    crew = Crew(agents=[hr_compliance_agent], tasks=[t])
    return crew.kickoff(inputs=payload)
