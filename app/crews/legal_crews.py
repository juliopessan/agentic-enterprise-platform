from crewai import Crew, Task
from app.agents.legal.contract_review import contract_review_agent
from app.agents.legal.compliance_monitoring import regulatory_compliance_agent
from app.agents.legal.litigation_support import litigation_support_agent

def run_contract_review(task_name: str, payload: dict):
    t = Task(
        description=f"Conduct a comprehensive legal review of the provided contract documentation. Analyze for compliance issues, risk factors, key obligations, and unfavorable terms. Provide detailed findings with risk ratings and recommended actions. Task: {task_name}",
        expected_output="A detailed contract analysis report including identified risks, compliance gaps, key obligations, risk ratings (high/medium/low), and specific recommendations for negotiation or acceptance."
    )
    crew = Crew(agents=[contract_review_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_compliance_monitoring(task_name: str, payload: dict):
    t = Task(
        description=f"Perform a thorough assessment of current operations against applicable legal and regulatory requirements. Identify potential compliance gaps and recommend corrective actions. Task: {task_name}",
        expected_output="A compliance assessment report detailing findings, identified gaps, risk levels, and prioritized recommendations for remediation with implementation timelines."
    )
    crew = Crew(agents=[regulatory_compliance_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_litigation_support(task_name: str, payload: dict):
    t = Task(
        description=f"Provide comprehensive litigation support by analyzing case materials, researching relevant precedents, and developing strategic recommendations. Task: {task_name}",
        expected_output="A litigation strategy document including case analysis, precedent research, strength/weakness assessment, and recommended approaches with supporting evidence."
    )
    crew = Crew(agents=[litigation_support_agent], tasks=[t])
    return crew.kickoff(inputs=payload)