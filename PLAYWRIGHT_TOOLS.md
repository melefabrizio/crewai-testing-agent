# Playwright Tools Reference

This document describes all the Playwright tools available to the CrewAI agents.

## Overview

Both the **Test Planner** and **Test Executor** agents have access to a full suite of Playwright tools. These tools enable real browser automation using the Playwright library.

## Architecture

- **BrowserManager**: A singleton class that manages a shared Playwright browser instance
- **Tool Classes**: Each tool inherits from CrewAI's `BaseTool` and wraps Playwright functionality
- **Shared State**: All tools share the same browser instance, allowing state to persist across tool calls

## Available Tools

### 1. NavigateTool
**Name**: `navigate_to_url`

**Description**: Navigate the browser to a specific URL.

**Parameters**:
- `url` (str): The URL to navigate to

**Example**:
```python
navigate_to_url(url="https://example.com")
```

**Returns**: Success/failure message

---

### 2. ClickTool
**Name**: `click_element`

**Description**: Click on an element on the page.

**Parameters**:
- `selector` (str): CSS selector or text of the element to click
- `by_text` (bool): If True, treat selector as text to find and click (default: False)

**Examples**:
```python
# Click by CSS selector
click_element(selector="button.submit")

# Click by text
click_element(selector="Sign In", by_text=True)
```

**Returns**: Success/failure message

---

### 3. TypeTool
**Name**: `type_text`

**Description**: Type text into an input field.

**Parameters**:
- `selector` (str): CSS selector of the input element
- `text` (str): Text to type into the element
- `press_enter` (bool): Press Enter after typing (default: False)

**Example**:
```python
type_text(selector="#email", text="user@example.com", press_enter=False)
```

**Returns**: Success/failure message

---

### 4. FillFormTool
**Name**: `fill_form`

**Description**: Fill multiple form fields at once.

**Parameters**:
- `form_data` (Dict[str, str]): Dictionary mapping CSS selectors to values

**Example**:
```python
fill_form(form_data={
    "#email": "user@example.com",
    "#password": "mypassword",
    "#name": "John Doe"
})
```

**Returns**: Success/failure message with list of filled fields

---

### 5. VerifyElementTool
**Name**: `verify_element`

**Description**: Verify that an element exists and optionally check its text content and visibility.

**Parameters**:
- `selector` (str): CSS selector of element to verify
- `expected_text` (Optional[str]): Expected text content
- `should_be_visible` (bool): Whether element should be visible (default: True)

**Example**:
```python
verify_element(
    selector="h1.title",
    expected_text="Welcome",
    should_be_visible=True
)
```

**Returns**: Success/failure message with verification details

---

### 6. WaitForTool
**Name**: `wait_for_element`

**Description**: Wait for an element to appear, disappear, or reach a certain state.

**Parameters**:
- `selector` (Optional[str]): CSS selector to wait for
- `timeout` (int): Timeout in milliseconds (default: 5000)
- `state` (str): State to wait for: visible, hidden, attached, detached (default: "visible")

**Examples**:
```python
# Wait for element to be visible
wait_for_element(selector=".loading-spinner", timeout=5000, state="visible")

# Wait for a fixed time
wait_for_element(timeout=3000)
```

**Returns**: Success/failure message

---

### 7. SnapshotTool
**Name**: `take_snapshot`

**Description**: Take an accessibility snapshot of the current page.

**Parameters**:
- `save_to_file` (bool): Save snapshot to file (default: False)

**Example**:
```python
take_snapshot(save_to_file=True)
```

**Returns**: Snapshot information (URL, title, content length)

---

### 8. ScreenshotTool
**Name**: `take_screenshot`

**Description**: Take a screenshot of the current page.

**Parameters**:
- `filename` (Optional[str]): Filename to save screenshot (default: auto-generated)
- `full_page` (bool): Capture full scrollable page (default: False)

**Example**:
```python
take_screenshot(filename="homepage.png", full_page=True)
```

**Returns**: Success message with filename

---

### 9. EvaluateTool
**Name**: `evaluate_javascript`

**Description**: Execute JavaScript code on the page and return the result.

**Parameters**:
- `script` (str): JavaScript code to evaluate

**Example**:
```python
evaluate_javascript(script="document.title")
evaluate_javascript(script="document.querySelectorAll('button').length")
```

**Returns**: Success message with script result

---

### 10. GetCurrentUrlTool
**Name**: `get_current_url`

**Description**: Get the current URL of the browser page.

**Parameters**: None

**Example**:
```python
get_current_url()
```

**Returns**: Current URL

---

### 11. GetPageTextTool
**Name**: `get_page_text`

**Description**: Get all visible text content from the current page.

**Parameters**: None

**Example**:
```python
get_page_text()
```

**Returns**: Page text content (truncated if too long)

---

### 12. CloseBrowserTool
**Name**: `close_browser`

**Description**: Close the browser and cleanup resources. **Use this at the end of testing.**

**Parameters**: None

**Example**:
```python
close_browser()
```

**Returns**: Success/failure message

---

## CSS Selectors Reference

### Common Selectors

```css
/* By ID */
#elementId

/* By class */
.className

/* By tag */
button, input, div

/* By attribute */
[type="submit"]
[name="email"]

/* By multiple classes */
.btn.btn-primary

/* Descendant */
.container .item

/* Direct child */
.parent > .child

/* Multiple selectors */
button, .submit, #send
```

### Selector Examples

```python
# Input field by ID
"#email"

# Button by class
"button.submit"

# Link by text (use by_text=True)
"Sign In"

# First paragraph in a div
"div.content p:first-child"

# Input with specific type
"input[type='password']"

# Element with data attribute
"[data-testid='login-button']"
```

## Typical Test Flow

### Test Planner Agent Workflow

1. **Navigate** to the website
2. **Take snapshot** to understand page structure
3. **Get page text** to see content
4. **Create detailed test plan** with exact selectors

### Test Executor Agent Workflow

1. **Navigate** to test URL
2. **Fill form** or **Type text** into inputs
3. **Click** buttons or links
4. **Wait for** elements to load
5. **Verify element** presence and content
6. **Take screenshot** if test fails
7. **Close browser** when done

## Example Test Scenario

```yaml
Test Plan:
1. Navigate to: https://example.com/login
2. Fill form:
   - #email: "test@example.com"
   - #password: "password123"
3. Click element: button[type="submit"]
4. Wait for element: .dashboard (5000ms)
5. Verify element: h1.welcome
   - Expected text: "Welcome"
6. Take screenshot: dashboard.png
7. Close browser

Expected Result: User successfully logs in and sees dashboard
```

## Error Handling

All tools return descriptive error messages if they fail:

```
✓ Successfully navigated to: https://example.com
✗ Click failed: Timeout 30000ms exceeded waiting for selector "button.missing"
✓ Successfully typed 'test@example.com' into: #email
✗ Element not found: .non-existent-class
```

## Best Practices

### For Test Planner Agent

1. **Explore first**: Use `navigate_to_url` and `take_snapshot` to understand the page
2. **Be specific**: Provide exact CSS selectors in your test plans
3. **Consider timing**: Include wait steps for dynamic content
4. **Plan for verification**: Include verify steps to check expected outcomes

### For Test Executor Agent

1. **Execute sequentially**: Follow the test plan step by step
2. **Wait appropriately**: Use `wait_for_element` after clicks or navigation
3. **Verify outcomes**: Use `verify_element` to check results
4. **Capture evidence**: Take screenshots when tests fail
5. **Clean up**: Always call `close_browser` at the end

## Troubleshooting

### Element Not Found
- Verify the selector is correct
- Check if you need to wait for the element to load
- Use `get_page_text` or `take_snapshot` to inspect page state

### Click Fails
- Ensure element is visible and clickable
- Try using `by_text=True` for text-based clicking
- Wait for page to fully load before clicking

### Timeout Errors
- Increase timeout values for slow-loading pages
- Check network connectivity
- Verify the page URL is correct

## Advanced Usage

### Chaining Operations

```python
# Navigate and verify
navigate_to_url(url="https://example.com")
wait_for_element(selector="body")
verify_element(selector="h1", expected_text="Example Domain")

# Fill and submit form
fill_form(form_data={"#email": "user@test.com", "#password": "pass"})
click_element(selector="button[type='submit']")
wait_for_element(selector=".success-message")

# Verify and capture
verify_element(selector=".dashboard")
take_screenshot(filename="success.png", full_page=True)
close_browser()
```

### Dynamic Content

```python
# Wait for AJAX content
navigate_to_url(url="https://example.com/dynamic")
click_element(selector="button.load-data")
wait_for_element(selector=".data-loaded", timeout=10000)
verify_element(selector=".data-item:first-child")
```

### JavaScript Interaction

```python
# Get computed values
evaluate_javascript(script="window.innerWidth")

# Check application state
evaluate_javascript(script="localStorage.getItem('userId')")

# Count elements
evaluate_javascript(script="document.querySelectorAll('.item').length")
```

## Integration with CrewAI

These tools are automatically available to agents through the `tools` parameter:

```python
from src.frontend_test_crew.agents.test_agents import create_test_planner, create_test_executor

# Both agents have all Playwright tools
planner = create_test_planner()
executor = create_test_executor()
```

The agents will automatically choose and invoke appropriate tools based on:
- The test scenario provided
- The current state of the test execution
- Their role and responsibilities
