"""
Run suite in CI with essential output
"""

import os
import subprocess

import litellm.llms.anthropic.chat
from crewai import LLM
from dotenv import load_dotenv
from src.frontend_test_crew.crew import FrontendTestCrew
from litellm.llms.anthropic.chat import AnthropicChatCompletion


def main():
    """Run a simple test"""
    # Load environment variables
    load_dotenv()

    # Check for API key
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  Error: No API key found!")
        print("Please set OPENAI_API_KEY or ANTHROPIC_API_KEY in your .env file")
        return

    if not os.getenv("WEBSITE"):
        print("⚠️  Error: No WEBSITE found!")
        print("Please set WEBSITE in your .env file")
        return

    website_url = os.getenv(
        "WEBSITE") or "https://v0-erp-application-development-eight.vercel.app/"

    # Check for Node.js (required for Playwright MCP)
    try:
        result = subprocess.run(["node", "--version"], capture_output=True,
                                check=True, text=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠️  Error: Node.js is required to run Playwright MCP server")
        print("Please install Node.js from https://nodejs.org/")
        return

    # Create the crew
    crew = FrontendTestCrew(headless=False)

    result = crew.test_website(
        website_url=website_url,
        verbose=False,
        test_scenario="""
        Test the Contacts module. Test all features available in the contacts page.
        Plan and execute tests, then report the JSON results.
        """
    )


    if result['status'] == 'completed':
        json_result = result['result'].json_dict
        print(json_result)
        if json_result.get('success', True):
            exit(0)
    else:
        print(f"\nError: {result.get('error', 'Unknown error')}")
        print("\n❌ Test failed!")
    exit(1)


if __name__ == "__main__":
    main()
