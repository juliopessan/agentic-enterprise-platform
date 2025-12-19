from crewai import Crew, Task
from app.agents.hr.talent_ops import talent_acquisition_agent
from app.agents.hr.people_lifecycle import onboarding_agent
from app.agents.hr.compliance import hr_compliance_agent

def run_talent_ops(task_name: str, payload: dict):
    t = Task(
        description=f"Execute comprehensive talent acquisition processes including candidate sourcing, evaluation, and selection. Ensure alignment with role requirements and company culture. Task: {task_name}",
        expected_output="A detailed candidate assessment report including rankings, strengths/weaknesses analysis, cultural fit evaluation, and hiring recommendations with justification."
    )
    crew = Crew(agents=[talent_acquisition_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_people_lifecycle(task_name: str, payload: dict):
    t = Task(
        description=f"Orchestrate seamless employee onboarding experiences that accelerate productivity and ensure compliance. Personalize journeys based on role and organizational needs. Task: {task_name}",
        expected_output="A comprehensive onboarding plan including timeline, key milestones, required resources, compliance checkpoints, and success metrics with risk mitigation strategies."
    )
    crew = Crew(agents=[onboarding_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_hr_compliance(task_name: str, payload: dict):
    t = Task(
        description=f"Conduct thorough HR compliance assessments to identify gaps and ensure adherence to employment laws and company policies. Maintain detailed audit trails. Task: {task_name}",
        expected_output="An HR compliance audit report detailing findings, risk levels, regulatory gaps, and corrective action plans with implementation timelines and responsible parties."
    )
    crew = Crew(agents=[hr_compliance_agent], tasks=[t])
    return crew.kickoff(inputs=payload)
