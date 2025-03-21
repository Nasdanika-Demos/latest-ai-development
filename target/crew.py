from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
@CrewBase
class LatestAiDevelopment:
	"""Latest AI Development"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	@agent
	def researcher(self) -> Agent:
		return Agent(
		    config=self.agents_config['researcher'],
		    verbose=True
		)
	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
		    config=self.agents_config['reporting_analyst'],
		    verbose=True
		)
	@task
	def research_task(self) -> Task:
		return Task(
		    config=self.tasks_config['research_task'],
		    tools=[SerperDevTool()]
		)
	@task
	def reporting_task(self) -> Task:
		return Task(
		    config=self.tasks_config['reporting_task']
		)
	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True
		)
