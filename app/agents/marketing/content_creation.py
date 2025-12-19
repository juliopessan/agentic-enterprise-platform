from crewai import Agent

content_creator_agent = Agent(
    role="Content Creator Agent",
    goal="Generate engaging marketing content tailored to target audiences and brand guidelines.",
    backstory="Creative marketing professional specializing in content creation across various formats and platforms.",
    verbose=True,
    memory=True
)