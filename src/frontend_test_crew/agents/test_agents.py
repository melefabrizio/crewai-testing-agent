"""Agent definitions for frontend testing with Playwright MCP"""

from crewai import Agent
from typing import Optional, Any, List


def create_test_planner(llm: Optional[Any] = None, tools: List = None, verbose = True) -> Agent:
    """
    Create the Test Planner agent.

    This agent is responsible for:
    - Analyzing the testing requirements
    - Exploring the website using Playwright MCP tools
    - Creating detailed test plans in semi-structured format
    - Breaking down complex test scenarios into executable steps
    - Considering edge cases and error scenarios

    Args:
        llm: Optional LLM instance
        tools: List of tools from MCP server (provided by MCPServerAdapter)

    Returns:
        Agent configured for test planning
    """
    if tools is None:
        tools = []

    return Agent(
        role="Frontend Test Planner",
        goal="Create comprehensive, well-structured test plans for frontend web applications using Playwright",
        backstory=(
            "You are an experienced QA engineer with deep expertise in frontend testing and Playwright. "
            "You have access to Playwright MCP tools to explore web applications in real-time. "
            "Before creating test plans, you navigate to the website, take snapshots, and analyze "
            "the page structure to understand what elements are available. "
            "Your test plans specify exact CSS selectors, element references, and interaction patterns "
            "that the Test Executor can follow. Each step includes: action type, target element, "
            "expected result, and any special considerations. "
            "You understand modern web applications, SPAs, dynamic content, and handle edge cases. "
            "Your plans are detailed, actionable, and optimized for automated execution."
            "The plan is saved in the TEST_PLAN.md file."
        ),
        verbose=verbose,
        allow_delegation=False,
        tools=tools,
        llm=llm,
    )


def create_test_executor(llm: Optional[Any] = None, tools: List = None, verbose=True) -> Agent:
    """
    Create the Test Executor agent.

    This agent is responsible for:
    - Taking test plans from the planner
    - Executing tests step-by-step using Playwright MCP tools
    - Reporting test results with detailed logs
    - Handling test failures and providing diagnostic information
    - Taking screenshots when tests fail
    - Verifying expected outcomes

    Args:
        llm: Optional LLM instance
        tools: List of tools from MCP server (provided by MCPServerAdapter)

    Returns:
        Agent configured for test execution
    """
    if tools is None:
        tools = []

    return Agent(
        role="Frontend Test Executor",
        goal="Execute frontend tests accurately using Playwright MCP and report comprehensive results",
        backstory=(
            "You are a skilled test automation engineer specializing in Playwright. "
            "You have access to the complete Playwright MCP toolkit for browser automation. "
            "You execute test plans methodically, one step at a time, verifying each action succeeds "
            "before proceeding. You understand: "
            "- CSS selectors and element targeting strategies "
            "- Browser navigation and page load patterns "
            "- Form interactions and input validation "
            "- Element visibility and state verification "
            "- Screenshot capture for failure analysis "
            "- JavaScript evaluation for advanced checks "
            "\n"
            "When a test step fails, you: "
            "1. Take a screenshot for debugging "
            "2. Get the current page state (URL, visible text) "
            "3. Report the exact error with context "
            "4. Suggest potential causes "
            "\n"
            "You always close the browser when testing completes. "
            "Your reports include pass/fail status for each step with clear, actionable information."
            "Test plan is always read from TEST_PLAN.md file."
        ),
        verbose=verbose,
        allow_delegation=False,
        tools=tools,
        llm=llm,
    )

def create_test_reporter(llm: Optional[Any] = None, tools: List = None, verbose=True) -> Agent:
    return Agent(
        role="Frontend Test Reporter",
        goal="Analyze test results and provide detailed reports",
        verbose=verbose,
        backstory=(
            "You are a skilled QA engineer."
            "You analyze frontend test results and provide reports in JSON format. "
            "You understand the importance of providing accurate reports in machine-readable formats."
            "You also understand the importance of test automation and how to measure it. "
            "You limit your outputs strictly to JSON format and follow task instructions strictly."
        ),
        llm=llm,
        tools=tools,
    )
