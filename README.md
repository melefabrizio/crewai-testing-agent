# Frontend Test Crew

A multi-agent frontend testing system built with CrewAI and Playwright. This system uses two specialized AI agents to plan and execute comprehensive frontend tests for web applications.

## Features

- **Multi-Agent Architecture**: Two specialized agents working together
  - **Test Planner**: Analyzes requirements, explores websites, and creates detailed test plans
  - **Test Executor**: Executes tests using Playwright and reports results
  - **Both agents have access to 12+ Playwright tools** for complete browser automation

- **Full Playwright Integration**: Real browser automation using Playwright Python API
  - Navigate to URLs
  - Click elements (by selector or text)
  - Type into inputs and fill forms
  - Verify element presence and content
  - Take screenshots and page snapshots
  - Execute JavaScript
  - Wait for dynamic content

- **Intelligent Test Planning**: The Test Planner can explore websites before planning tests

- **Comprehensive Testing**: Covers functionality, user flows, edge cases, and error handling

## Architecture

```
Frontend Test Crew
├── Test Planner Agent (with Playwright tools)
│   ├── Explores the website
│   ├── Analyzes testing requirements
│   ├── Creates detailed test plans with exact selectors
│   └── Considers edge cases
│
├── Test Executor Agent (with Playwright tools)
│   ├── Executes test plans step-by-step
│   ├── Uses Playwright for real browser automation
│   ├── Verifies expected outcomes
│   ├── Takes screenshots on failures
│   └── Reports detailed results
│
└── Playwright Tools (12 tools available to both agents)
    ├── NavigateTool - Navigate to URLs
    ├── ClickTool - Click elements
    ├── TypeTool - Type into inputs
    ├── FillFormTool - Fill multiple fields
    ├── VerifyElementTool - Verify elements
    ├── WaitForTool - Wait for elements
    ├── SnapshotTool - Capture page state
    ├── ScreenshotTool - Take screenshots
    ├── EvaluateTool - Execute JavaScript
    ├── GetCurrentUrlTool - Get current URL
    ├── GetPageTextTool - Get page content
    └── CloseBrowserTool - Cleanup resources
```

## Installation

1. Clone the repository and navigate to the directory:
```bash
cd crewai-testing
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
playwright install
```

5. Set up environment variables:
```bash
cp .env.example .env
```

Edit `.env` and add your API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Quick Start

Run the simple test to verify setup:
```bash
python simple_test.py
```

Or run the full example script with multiple scenarios:
```bash
python example_usage.py
```

This provides an interactive menu with several pre-built test scenarios.

### Programmatic Usage

```python
from src.frontend_test_crew.crew import FrontendTestCrew

# Create the crew
crew = FrontendTestCrew()

# Run a test
result = crew.test_website(
    website_url="https://example.com",
    test_scenario="""
    Test the login functionality:
    1. Navigate to the login page
    2. Enter valid credentials
    3. Verify successful login
    4. Check error handling for invalid credentials
    """
)

print(f"Status: {result['status']}")
print(f"Results: {result['result']}")
```

### Custom Test Scenarios

You can create custom test scenarios using natural language:

```python
crew = FrontendTestCrew()

result = crew.test_website(
    website_url="https://yourapp.com",
    test_scenario="""
    Test the shopping cart:
    1. Navigate to the products page
    2. Add 3 items to the cart
    3. Go to the cart page
    4. Verify all items are present
    5. Update quantities
    6. Proceed to checkout
    """,
    additional_context="Focus on mobile responsiveness"
)
```

## Project Structure

```
crewai-testing/
├── src/
│   └── frontend_test_crew/
│       ├── __init__.py
│       ├── crew.py                 # Main crew orchestration
│       ├── agents/
│       │   ├── __init__.py
│       │   └── test_agents.py      # Agent definitions
│       ├── tasks/
│       │   ├── __init__.py
│       │   └── test_tasks.py       # Task definitions
│       └── tools/
│           ├── __init__.py
│           └── playwright_tools.py # Playwright integration
├── example_usage.py                # Example scripts
├── requirements.txt                # Python dependencies
├── pyproject.toml                 # Poetry configuration
├── .env.example                   # Environment variables template
└── README.md                      # This file
```

## Test Plan Format

The Test Planner creates semi-structured test plans that follow this format:

```
Test Objective: [Description of what's being tested]

Step 1: Navigate to [URL]
Expected: Page loads successfully

Step 2: Click on [element]
Expected: [Expected result]

Step 3: Type "[text]" into [field]
Expected: Text is entered correctly

Step 4: Verify [condition]
Expected: [Expected state]

Edge Cases:
- [Edge case 1]
- [Edge case 2]
```

## Playwright Tools

Both agents have access to 12 Playwright tools. For complete tool documentation, see [PLAYWRIGHT_TOOLS.md](PLAYWRIGHT_TOOLS.md).

### Core Tools

- **navigate_to_url**: Go to a specific URL
- **click_element**: Click on buttons, links, or elements (by selector or text)
- **type_text**: Enter text into input fields
- **fill_form**: Fill multiple form fields at once
- **verify_element**: Check element presence, visibility, and text content
- **wait_for_element**: Wait for elements to appear or reach a state
- **take_screenshot**: Capture page screenshots
- **take_snapshot**: Capture accessibility snapshot for analysis
- **evaluate_javascript**: Execute JavaScript on the page
- **get_current_url**: Get the current page URL
- **get_page_text**: Get all visible text from the page
- **close_browser**: Cleanup browser resources

### Example Tool Usage

```python
# The agents will automatically use these tools based on the test scenario
# Example of what happens under the hood:

# Test Planner explores the site
navigate_to_url(url="https://example.com/login")
take_snapshot()  # Understand page structure
get_page_text()  # See what's on the page

# Test Executor runs the tests
fill_form(form_data={"#email": "test@example.com", "#password": "pass123"})
click_element(selector="button[type='submit']")
wait_for_element(selector=".dashboard", timeout=5000)
verify_element(selector="h1.welcome", expected_text="Welcome")
take_screenshot(filename="success.png")
close_browser()
```

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (for GPT models)
- `ANTHROPIC_API_KEY`: Your Anthropic API key (for Claude models)
- `OPENAI_MODEL_NAME`: Model to use (default: gpt-4-turbo-preview)

### Agent Configuration

You can customize agent behavior by modifying the agent definitions in `src/frontend_test_crew/agents/test_agents.py`.

## Examples

### Login Test
```python
crew.test_website(
    website_url="https://app.example.com/login",
    test_scenario="Test login with valid and invalid credentials"
)
```

### Form Validation
```python
crew.test_website(
    website_url="https://example.com/signup",
    test_scenario="Test form validation for all fields"
)
```

### User Flow
```python
crew.test_website(
    website_url="https://shop.example.com",
    test_scenario="Complete purchase flow from product selection to checkout"
)
```

## Extending the System

### Adding New Tools

Create new tools in `src/frontend_test_crew/tools/`:

```python
from crewai_tools import BaseTool

class CustomTestTool(BaseTool):
    name = "Custom Tool"
    description = "Description of what it does"

    def _run(self, input: str) -> str:
        # Your implementation
        return result
```

### Adding New Agents

Define new agents in `src/frontend_test_crew/agents/test_agents.py`:

```python
def create_custom_agent(llm=None) -> Agent:
    return Agent(
        role="Custom Role",
        goal="Custom goal",
        backstory="Custom backstory",
        tools=[your_tools],
        llm=llm
    )
```

## Contributing

Contributions are welcome! Areas for improvement:
- Enhanced Playwright MCP integration
- Additional test tools and capabilities
- More sophisticated test result reporting
- Screenshot and video capture
- Parallel test execution
- Test result storage and analytics

## License

MIT License - feel free to use and modify as needed.

## Troubleshooting

### API Key Issues
```
Error: No API key found
```
Solution: Make sure you've created a `.env` file with your API key.

### Import Errors
```
ModuleNotFoundError: No module named 'crewai'
```
Solution: Make sure you've installed all dependencies: `pip install -r requirements.txt`

### Playwright Issues
```
Error: Playwright browser not found
```
Solution: Install Playwright browsers: `playwright install`

## Support

For issues and questions:
- Check the example scripts in `example_usage.py`
- Review the documentation in the code
- Open an issue on the project repository

## Roadmap

- [x] Full Playwright integration with 12+ tools
- [x] Both agents can use Playwright tools
- [ ] Visual regression testing
- [ ] Performance testing capabilities
- [ ] Mobile device testing
- [ ] API testing integration
- [ ] CI/CD integration examples
- [ ] Test result dashboard
- [ ] Video recording of test runs
- [ ] Headless vs headed browser configuration
- [ ] Multi-browser support (Chrome, Firefox, Safari)
