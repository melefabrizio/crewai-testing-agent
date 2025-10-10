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

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (for GPT models)
- `ANTHROPIC_API_KEY`: Your Anthropic API key (for Claude models)
- `MODEL`: Model to use (default: claude-sonnet-4-5)

### Agent Configuration

You can customize agent behavior by modifying the agent definitions in `src/frontend_test_crew/agents/test_agents.py`.
