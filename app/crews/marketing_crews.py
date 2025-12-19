from crewai import Crew, Task
from app.agents.marketing.campaign_management import campaign_manager_agent
from app.agents.marketing.content_creation import content_creator_agent
from app.agents.marketing.analytics_reporting import marketing_analyst_agent

def run_campaign_management(task_name: str, payload: dict):
    t = Task(
        description=f"Develop and execute comprehensive marketing campaigns aligned with business objectives and target audience needs. Optimize performance based on real-time data and market feedback. Task: {task_name}",
        expected_output="A detailed campaign plan including strategy, channel allocation, budget distribution, timeline, KPIs, and optimization recommendations with projected ROI metrics."
    )
    crew = Crew(agents=[campaign_manager_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_content_creation(task_name: str, payload: dict):
    t = Task(
        description=f"Create engaging, brand-consistent content tailored to specific audiences and marketing channels. Ensure content aligns with campaign objectives and brand guidelines. Task: {task_name}",
        expected_output="High-quality marketing content assets including copy, visuals, and multimedia elements optimized for specific platforms and audience segments with performance tracking recommendations."
    )
    crew = Crew(agents=[content_creator_agent], tasks=[t])
    return crew.kickoff(inputs=payload)

def run_analytics_reporting(task_name: str, payload: dict):
    t = Task(
        description=f"Analyze marketing performance data to extract actionable insights and inform strategic decisions. Identify optimization opportunities and measure campaign effectiveness. Task: {task_name}",
        expected_output="A comprehensive analytics report with performance metrics, trend analysis, insight extraction, and data-driven recommendations for optimization with projected impact assessments."
    )
    crew = Crew(agents=[marketing_analyst_agent], tasks=[t])
    return crew.kickoff(inputs=payload)