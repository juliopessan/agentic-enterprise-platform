from crewai import Crew, Task
from app.agents.marketing.campaign_management import campaign_manager_agent
from app.agents.marketing.content_creation import content_creator_agent
from app.agents.marketing.analytics_reporting import marketing_analyst_agent

def run_campaign_management(task_name: str, payload: dict):
    t = Task(description=f"{task_name}: Use payload to complete the task and return structured output.")
    crew = Crew(agents=[campaign_manager_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_content_creation(task_name: str, payload: dict):
    t = Task(description=f"{task_name}: Use payload to complete the task and return structured output.")
    crew = Crew(agents=[content_creator_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_analytics_reporting(task_name: str, payload: dict):
    t = Task(description=f"{task_name}: Use payload to complete the task and return structured output.")
    crew = Crew(agents=[marketing_analyst_agent], tasks=[t])
    return crew.kickoff(inputs=payload)