from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

from dotenv import load_dotenv
import os

from edu.tools.custom_tool import HandleReviewedBlogTool

load_dotenv()

@CrewBase
class Edu():
    """Edu crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def BlogWriter(self) -> Agent: 
        return Agent(
            config=self.agents_config['BlogWriter'], 
            verbose=True,
            # You can also add any other parameters you want to pass to the LLM
            # https://docs.crewai.com/concepts/agents#llm-configuration
            llm=LLM(
                model=os.getenv("MODEL"),
                api_key=os.getenv("GEMINI_API_KEY")
            )
        ) # a blog writer agent

    @agent
    def BlogReviewer(self) -> Agent: 
        return Agent(
            config=self.agents_config['BlogReviewer'], 
            verbose=True,
            llm=LLM(
                model=os.getenv("MODEL"),
                api_key=os.getenv("GEMINI_API_KEY")
            )
        ) # a blog reviewer agent
    
    @agent
    def BlogPoster(self) -> Agent: 
        return Agent(
            config=self.agents_config['BlogPoster'], 
            verbose=True,
            llm=LLM(
                model=os.getenv("MODEL"),
                api_key=os.getenv("GEMINI_API_KEY")
            )
        ) # a blog poster agent
    
    @agent
    def humanInput(self) -> Agent:
        return Agent(
            config=self.agents_config['humanInput'],
            verbose=True,
            llm=LLM(
                model=os.getenv("MODEL"),
                api_key=os.getenv("GEMINI_API_KEY")
            ),
            tools=[HandleReviewedBlogTool()]  # Use the tool instance
        )  # a human review handler agent

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def createBlog(self) -> Task: 
        return Task( 
            config=self.tasks_config['createBlog'], 
        ) # a task to create a blog

    @task
    def reviewBlog(self) -> Task: 
        return Task(
            config=self.tasks_config['reviewBlog'], 
        ) # a task to review the blog
    
    @task
    def getHumanConsent(self) -> Task: 
        return Task( 
            config=self.tasks_config['getHumanConsent'], 
        ) # a task to get human consent for the blog
    
    
    @task
    def publish(self) -> Task: 
        return Task( 
            config=self.tasks_config['publish'], 
            output_file='FINALreport.md'
        ) # a task to post the blog to a website



    @crew
    def crew(self) -> Crew:
        """Creates the Edu crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
