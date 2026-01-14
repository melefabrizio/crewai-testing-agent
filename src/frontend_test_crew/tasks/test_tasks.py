"""Task definitions for frontend testing workflow"""

from crewai import Task, Agent
from typing import Optional


def create_planning_task(
    agent: Agent,
    website_url: str,
    test_scenario: str,
    additional_context: Optional[str] = None
) -> Task:
    """
    Create a test planning task.

    Args:
        agent: The test planner agent
        website_url: URL of the website to test
        test_scenario: Description of what needs to be tested
        additional_context: Any additional context or requirements

    Returns:
        Task object for test planning
    """
    context_section = f"\n\nAdditional Context:\n{additional_context}" if additional_context else ""

    description = f"""
    Create a detailed test plan for the following web application testing scenario:

    Website URL: {website_url}
    Test Scenario: {test_scenario}{context_section}
    
    The plan should be formulated while exploring deeply the website to infer features and interactions.
    You should look accurately at the website HTML and visual structure to infer features.
    If needed interact with the website to discover tests.
    If the TEST_PLAN.md file already exists, update it with new tests if needed.

    Your test plan should be in a semi-structured format that includes:
    1. Test objective and scope
    2. Numbered test steps with clear actions (navigate, click, type, verify, etc.)
    3. Expected results for each step
    4. Any edge cases or error scenarios to consider

    Format each test step clearly so it can be executed by an executor agent.
    Use action verbs like: Navigate to, Click on, Type, Verify, Wait for, etc.
    
    The plan should be written to TEST_PLAN.md file.

    Example format:
    Step 1: Navigate to {website_url}
    Step 2: Click on "Login" button
    Step 3: Type "testuser@example.com" into email field
    Step 4: Verify that dashboard is displayed
    """

    expected_output = """
    A comprehensive test plan with:
    - Clear test objective
    - Numbered, actionable test steps
    - Expected outcomes for each step
    - Edge cases and error scenarios
    - All in semi-structured format ready for automation
    """

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
    )


def create_execution_task(
    agent: Agent,
    test_plan_context: str = ""
) -> Task:
    """
    Create a test execution task.

    Args:
        agent: The test executor agent
        test_plan_context: Context from the planning task (will be provided automatically)

    Returns:
        Task object for test execution
    """
    description = """
    Execute the test plan provided by the Test Planner using Playwright.

    Steps:
    1. Review the test plan from the previous task
    2. Execute each test step using the Playwright Test Executor tool
    3. Document the results of each step
    4. Report any failures or issues encountered
    5. Provide a summary of the test execution

    Make sure to execute all steps in order and report comprehensive results.
    """

    expected_output = """
    A detailed test execution report including:
    - Status of each test step (passed/failed)
    - Any errors or issues encountered
    - Screenshots or evidence where applicable
    - Overall test result summary
    - Recommendations for any failures found
    """

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
    )

def create_report_task(
        agent: Agent,
        test_execution_context: str = ""
) -> Task:
    """
    Create a test report task.

    Args:
        agent: The test executor agent
        test_execution_context: Context from the test execution task (will be provided automatically)

    Returns:
        Task object for test execution
    """
    description = """
    Review the test execution result provided by the Test Executor and generate a JSON report.

    Steps:
    1. Review the test execution result from the previous task
    2. Analyze the results and generate a JSON report
    3. Include pass_count, fail_count, error_count, test_cases, success, fails, and errors in the report

    Make sure to execute all steps in order and report accurate results.
    Report should NOT be saved on file.
    """

    expected_output = """
    A JSON report with:
    - pass_count -> integer representing the number of passed tests
    - fail_count -> integer representing the number of failed tests
    - error_count -> integer representing the number of errors encountered
    - test_cases -> integer representing the number of test cases executed
    - success -> boolean indicating overall test success
    - fails -> list of failed test cases
    - errors -> list of errors encountered
    - summary -> list of objects, each object containing:
       - test_name -> name of the case
       - test_id -> id of the case
       - passed -> integer representing the number of passed assertions in the case
       - failed -> integer representing the number of failed assertions in the case
       - errors -> integer representing the number of errors encountered in the case
    - recommendations -> suggestions made by the executor about the application or the test suite
    
    The json report will contain ONLY the specified fields and be formatted as valid JSON.
    """

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
    )