from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

class HandleReviewedBlogToolInput(BaseModel):
    """Input schema for HandleReviewedBlogTool."""
    blog_content: str = Field(..., description="The content of the blog to be reviewed.")


class HandleReviewedBlogTool(BaseTool):
    """Tool to handle reviewed blogs."""
    name: str = "handle_reviewed_blog"
    description: str = "Handles the reviewed blog by presenting it to the human user via CLI."
    args_schema: Type[BaseModel] = HandleReviewedBlogToolInput

    def _run(self, blog_content: str) -> str | dict:
        """
        Handles the reviewed blog by presenting it to the human user via CLI
        and taking action based on the user's input.
        """
        print("\n--- Reviewed Blog ---")
        print(blog_content)
        print("\nPlease validate the blog:")
        print("1. Approve and send to BlogPoster")
        print("2. Provide feedback and send back to BlogWriter")
        
        while True:
            user_choice = input("Enter your choice (1 or 2): ").strip()
            if user_choice == "1":
                print("Blog approved. Sending to BlogPoster...")
                return "approve"
            elif user_choice == "2":
                feedback = input("Enter your feedback for the BlogWriter: ").strip()
                print("Feedback received. Sending back to BlogWriter...")
                return {"action": "feedback", "feedback": feedback}
            else:
                print("Invalid choice. Please enter 1 or 2.")
