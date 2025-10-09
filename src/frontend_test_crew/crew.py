"""Main crew orchestration for frontend testing with Playwright MCP"""

from crewai import Crew, Process, LLM
from crewai_tools import MCPServerAdapter
from typing import Optional, Dict, Any

from crewai_tools.tools.file_read_tool.file_read_tool import FileReadTool
from crewai_tools.tools.file_writer_tool.file_writer_tool import FileWriterTool
from openai.types.beta import FileSearchTool

from .agents.test_agents import create_test_planner, create_test_executor
from .tasks.test_tasks import create_planning_task, create_execution_task
from .mcp_config import get_playwright_mcp_params


class FrontendTestCrew:
    """
    Frontend Test Crew orchestrates multi-agent testing workflow using Playwright MCP.

    The crew consists of:
    1. Test Planner: Explores websites and creates detailed test plans
    2. Test Executor: Executes tests using Playwright MCP and reports results

    Both agents connect to the Playwright MCP server via stdio for browser automation.
    """

    def __init__(self, llm: Optional[LLM] = None, headless: bool = True, browser: str = "chromium"):
        """
        Initialize the Frontend Test Crew.

        Args:
            llm: Optional LLM instance to use for agents. If not provided,
                 agents will use the default LLM from environment.
            headless: Run browser in headless mode (default: True)
            browser: Browser type - chromium, firefox, webkit (default: chromium)
        """
        self.llm = llm
        self.headless = headless
        self.browser = browser

    def test_website(
        self,
        website_url: str,
        test_scenario: str,
        additional_context: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Execute a complete testing workflow for a website.

        This method uses a context manager to automatically start and stop
        the Playwright MCP server connection.

        Args:
            website_url: URL of the website to test
            test_scenario: Description of what needs to be tested
            additional_context: Optional additional context or requirements

        Returns:
            Dictionary containing test results and reports
        """
        # Configure Playwright MCP server parameters
        server_params = get_playwright_mcp_params(
            headless=self.headless,
            browser=self.browser
        )

        try:
            # Use context manager to automatically manage MCP server lifecycle
            with MCPServerAdapter(server_params) as tools:
                file_tools = [FileWriterTool(), FileReadTool()]
                # Create agents with tools from MCP server
                test_planner = create_test_planner(llm=self.llm, tools=tools + file_tools)
                test_executor = create_test_executor(llm=self.llm, tools=tools + file_tools)

                # Create tasks
                planning_task = create_planning_task(
                    agent=test_planner,
                    website_url=website_url,
                    test_scenario=test_scenario,
                    additional_context=additional_context
                )

                execution_task = create_execution_task(
                    agent=test_executor
                )

                # Execution task depends on planning task output
                execution_task.context = [planning_task]

                # Create and configure crew
                crew = Crew(
                    agents=[test_planner, test_executor],
                    tasks=[planning_task, execution_task],
                    process=Process.sequential,
                    verbose=True,
                )

                # Execute the crew
                result = crew.kickoff()

                return {
                    "status": "completed",
                    "result": result,
                    "website_url": website_url,
                    "test_scenario": test_scenario
                }

        except Exception as e:
            return {
                "status": "failed",
                "error": str(e),
                "website_url": website_url,
                "test_scenario": test_scenario
            }


def test_website_standalone(
    website_url: str,
    test_scenario: str,
    additional_context: Optional[str] = None,
    llm: Optional[Any] = None,
    headless: bool = True,
    browser: str = "chromium"
) -> Dict[str, Any]:
    """
    Standalone function to test a website using Playwright MCP.

    This is a convenience function that creates a FrontendTestCrew instance
    and executes the test in one call.

    Args:
        website_url: URL of the website to test
        test_scenario: Description of what needs to be tested
        additional_context: Optional additional context or requirements
        llm: Optional LLM instance
        headless: Run browser in headless mode (default: True)
        browser: Browser type - chromium, firefox, webkit (default: chromium)

    Returns:
        Dictionary containing test results and reports
    """
    crew = FrontendTestCrew(llm=llm, headless=headless, browser=browser)
    return crew.test_website(
        website_url=website_url,
        test_scenario=test_scenario,
        additional_context=additional_context
    )


def main():
    """
    Example usage of the Frontend Test Crew with Playwright MCP.
    """
    import os
    from dotenv import load_dotenv

    # Load environment variables
    load_dotenv()

    # Ensure API key is set
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  Please set OPENAI_API_KEY or ANTHROPIC_API_KEY in your .env file")
        return

    # Ensure Node.js is available for Playwright MCP
    import subprocess
    try:
        subprocess.run(["node", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠️  Node.js is required to run Playwright MCP server")
        print("Please install Node.js from https://nodejs.org/")
        return

    print("🤖 Frontend Test Crew with Playwright MCP")
    print("="*60)

    # Example test scenario
    website_url = "https://example.com"
    test_scenario = """
    Test the Example.com homepage:
    1. Navigate to the homepage
    2. Verify the page title
    3. Check that the main heading is visible
    4. Verify the 'More information' link exists
    """

    print(f"\n🌐 Website: {website_url}")
    print(f"📋 Scenario: {test_scenario}")
    print("\n🚀 Starting test execution...\n")

    # Execute the test
    result = test_website_standalone(
        website_url=website_url,
        test_scenario=test_scenario,
        headless=True
    )

    print("\n" + "="*60)
    print("📊 Test Results:")
    print("="*60)
    print(f"Status: {result['status']}")

    if result['status'] == 'completed':
        print(f"\n{result['result']}")
    else:
        print(f"\nError: {result['error']}")


if __name__ == "__main__":
    main()
