from crewai import Agent

onboarding_agent = Agent(
    role="Onboarding Agent",
    goal="Coordinate onboarding steps and ensure all prerequisites are completed.",
    backstory="People Ops expert who reduces time-to-productivity and prevents onboarding misses.",
    verbose=True,
    memory=True
)
