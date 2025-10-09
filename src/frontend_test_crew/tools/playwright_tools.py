"""Playwright MCP integration tools for CrewAI agents"""

from typing import Optional, Any, Dict, Type
from crewai_tools import BaseTool
from pydantic import BaseModel, Field
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
import json


# Shared browser context manager
class BrowserManager:
    """Manages a shared Playwright browser instance across tools"""

    _instance = None
    _browser: Optional[Browser] = None
    _context: Optional[BrowserContext] = None
    _page: Optional[Page] = None
    _playwright = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def get_page(self) -> Page:
        """Get or create the browser page"""
        if self._page is None:
            self.start_browser()
        return self._page

    def start_browser(self):
        """Start the Playwright browser"""
        if self._playwright is None:
            self._playwright = sync_playwright().start()
            self._browser = self._playwright.chromium.launch(headless=True)
            self._context = self._browser.new_context(
                viewport={'width': 1280, 'height': 720}
            )
            self._page = self._context.new_page()

    def close_browser(self):
        """Close the browser and cleanup"""
        if self._page:
            self._page.close()
            self._page = None
        if self._context:
            self._context.close()
            self._context = None
        if self._browser:
            self._browser.close()
            self._browser = None
        if self._playwright:
            self._playwright.stop()
            self._playwright = None

    def get_current_url(self) -> str:
        """Get current page URL"""
        if self._page:
            return self._page.url
        return ""


# Input schemas for tools
class NavigateInput(BaseModel):
    """Input for Navigate tool"""
    url: str = Field(..., description="The URL to navigate to")


class ClickInput(BaseModel):
    """Input for Click tool"""
    selector: str = Field(..., description="CSS selector or text of the element to click")
    by_text: bool = Field(False, description="If True, treat selector as text to find and click")


class TypeInput(BaseModel):
    """Input for Type tool"""
    selector: str = Field(..., description="CSS selector of the input element")
    text: str = Field(..., description="Text to type into the element")
    press_enter: bool = Field(False, description="Press Enter after typing")


class SnapshotInput(BaseModel):
    """Input for Snapshot tool"""
    save_to_file: bool = Field(False, description="Save snapshot to file")


class ScreenshotInput(BaseModel):
    """Input for Screenshot tool"""
    filename: Optional[str] = Field(None, description="Filename to save screenshot")
    full_page: bool = Field(False, description="Capture full scrollable page")


class FillFormInput(BaseModel):
    """Input for Fill Form tool"""
    form_data: Dict[str, str] = Field(..., description="Dictionary of field selectors and values to fill")


class WaitForInput(BaseModel):
    """Input for Wait For tool"""
    selector: Optional[str] = Field(None, description="CSS selector to wait for")
    timeout: int = Field(5000, description="Timeout in milliseconds")
    state: str = Field("visible", description="State to wait for: visible, hidden, attached, detached")


class EvaluateInput(BaseModel):
    """Input for Evaluate tool"""
    script: str = Field(..., description="JavaScript code to evaluate")


class VerifyElementInput(BaseModel):
    """Input for Verify Element tool"""
    selector: str = Field(..., description="CSS selector of element to verify")
    expected_text: Optional[str] = Field(None, description="Expected text content")
    should_be_visible: bool = Field(True, description="Whether element should be visible")


# Tool implementations
class NavigateTool(BaseTool):
    name: str = "navigate_to_url"
    description: str = (
        "Navigate the browser to a specific URL. "
        "Use this tool to open web pages and start testing workflows."
    )
    args_schema: Type[BaseModel] = NavigateInput

    def _run(self, url: str) -> str:
        try:
            browser_manager = BrowserManager.get_instance()
            page = browser_manager.get_page()
            page.goto(url, wait_until="networkidle", timeout=30000)
            return f"✓ Successfully navigated to: {url}"
        except Exception as e:
            return f"✗ Navigation failed: {str(e)}"


class ClickTool(BaseTool):
    name: str = "click_element"
    description: str = (
        "Click on an element on the page. "
        "You can use CSS selectors or set by_text=True to click by visible text. "
        "Examples: 'button.submit' or selector='Sign In', by_text=True"
    )
    args_schema: Type[BaseModel] = ClickInput

    def _run(self, selector: str, by_text: bool = False) -> str:
        try:
            browser_manager = BrowserManager.get_instance()
            page = browser_manager.get_page()

            if by_text:
                # Click by text content
                page.get_by_text(selector).click()
            else:
                # Click by CSS selector
                page.click(selector)

            return f"✓ Successfully clicked: {selector}"
        except Exception as e:
            return f"✗ Click failed: {str(e)}"


class TypeTool(BaseTool):
    name: str = "type_text"
    description: str = (
        "Type text into an input field. "
        "Provide a CSS selector and the text to type. "
        "Optionally press Enter after typing."
    )
    args_schema: Type[BaseModel] = TypeInput

    def _run(self, selector: str, text: str, press_enter: bool = False) -> str:
        try:
            browser_manager = BrowserManager.get_instance()
            page = browser_manager.get_page()

            page.fill(selector, text)
            if press_enter:
                page.press(selector, "Enter")

            return f"✓ Successfully typed '{text}' into: {selector}"
        except Exception as e:
            return f"✗ Type failed: {str(e)}"


class SnapshotTool(BaseTool):
    name: str = "take_snapshot"
    description: str = (
        "Take an accessibility snapshot of the current page. "
        "This captures the page structure and content for analysis."
    )
    args_schema: Type[BaseModel] = SnapshotInput

    def _run(self, save_to_file: bool = False) -> str:
        try:
            browser_manager = BrowserManager.get_instance()
            page = browser_manager.get_page()

            # Get page content
            content = page.content()
            title = page.title()
            url = page.url

            snapshot = {
                "url": url,
                "title": title,
                "content_length": len(content),
                "timestamp": "now"
            }

            if save_to_file:
                with open("page_snapshot.json", "w") as f:
                    json.dump(snapshot, f, indent=2)
                return f"✓ Snapshot saved to page_snapshot.json\nURL: {url}\nTitle: {title}"

            return f"✓ Snapshot captured\nURL: {url}\nTitle: {title}"
        except Exception as e:
            return f"✗ Snapshot failed: {str(e)}"


class ScreenshotTool(BaseTool):
    name: str = "take_screenshot"
    description: str = (
        "Take a screenshot of the current page. "
        "Optionally specify a filename and whether to capture the full page."
    )
    args_schema: Type[BaseModel] = ScreenshotInput

    def _run(self, filename: Optional[str] = None, full_page: bool = False) -> str:
        try:
            browser_manager = BrowserManager.get_instance()
            page = browser_manager.get_page()

            if filename is None:
                import time
                filename = f"screenshot_{int(time.time())}.png"

            page.screenshot(path=filename, full_page=full_page)
            return f"✓ Screenshot saved to: {filename}"
        except Exception as e:
            return f"✗ Screenshot failed: {str(e)}"


class FillFormTool(BaseTool):
    name: str = "fill_form"
    description: str = (
        "Fill multiple form fields at once. "
        "Provide a dictionary mapping CSS selectors to values. "
        "Example: {'#email': 'user@example.com', '#password': 'pass123'}"
    )
    args_schema: Type[BaseModel] = FillFormInput

    def _run(self, form_data: Dict[str, str]) -> str:
        try:
            browser_manager = BrowserManager.get_instance()
            page = browser_manager.get_page()

            results = []
            for selector, value in form_data.items():
                page.fill(selector, value)
                results.append(f"  • Filled {selector}")

            return "✓ Form filled successfully:\n" + "\n".join(results)
        except Exception as e:
            return f"✗ Form fill failed: {str(e)}"


class WaitForTool(BaseTool):
    name: str = "wait_for_element"
    description: str = (
        "Wait for an element to appear, disappear, or reach a certain state. "
        "Useful for waiting for dynamic content to load."
    )
    args_schema: Type[BaseModel] = WaitForInput

    def _run(self, selector: Optional[str] = None, timeout: int = 5000, state: str = "visible") -> str:
        try:
            browser_manager = BrowserManager.get_instance()
            page = browser_manager.get_page()

            if selector:
                page.wait_for_selector(selector, timeout=timeout, state=state)
                return f"✓ Element {selector} reached state: {state}"
            else:
                page.wait_for_timeout(timeout)
                return f"✓ Waited for {timeout}ms"
        except Exception as e:
            return f"✗ Wait failed: {str(e)}"


class EvaluateTool(BaseTool):
    name: str = "evaluate_javascript"
    description: str = (
        "Execute JavaScript code on the page and return the result. "
        "Useful for checking page state, getting element properties, or executing custom logic."
    )
    args_schema: Type[BaseModel] = EvaluateInput

    def _run(self, script: str) -> str:
        try:
            browser_manager = BrowserManager.get_instance()
            page = browser_manager.get_page()

            result = page.evaluate(script)
            return f"✓ Script executed successfully\nResult: {result}"
        except Exception as e:
            return f"✗ Script execution failed: {str(e)}"


class VerifyElementTool(BaseTool):
    name: str = "verify_element"
    description: str = (
        "Verify that an element exists and optionally check its text content and visibility. "
        "Use this to assert expected page state."
    )
    args_schema: Type[BaseModel] = VerifyElementInput

    def _run(self, selector: str, expected_text: Optional[str] = None, should_be_visible: bool = True) -> str:
        try:
            browser_manager = BrowserManager.get_instance()
            page = browser_manager.get_page()

            # Check if element exists
            element = page.query_selector(selector)
            if not element:
                return f"✗ Element not found: {selector}"

            # Check visibility
            is_visible = element.is_visible()
            if should_be_visible and not is_visible:
                return f"✗ Element exists but is not visible: {selector}"
            if not should_be_visible and is_visible:
                return f"✗ Element exists but should not be visible: {selector}"

            # Check text content if provided
            if expected_text:
                actual_text = element.text_content()
                if expected_text not in actual_text:
                    return f"✗ Text mismatch. Expected: '{expected_text}', Got: '{actual_text}'"

            return f"✓ Element verified successfully: {selector}"
        except Exception as e:
            return f"✗ Verification failed: {str(e)}"


class GetCurrentUrlTool(BaseTool):
    name: str = "get_current_url"
    description: str = "Get the current URL of the browser page"

    def _run(self) -> str:
        try:
            browser_manager = BrowserManager.get_instance()
            url = browser_manager.get_current_url()
            return f"Current URL: {url}"
        except Exception as e:
            return f"✗ Failed to get URL: {str(e)}"


class GetPageTextTool(BaseTool):
    name: str = "get_page_text"
    description: str = (
        "Get all visible text content from the current page. "
        "Useful for verifying page content without specific selectors."
    )

    def _run(self) -> str:
        try:
            browser_manager = BrowserManager.get_instance()
            page = browser_manager.get_page()

            text = page.evaluate("() => document.body.innerText")
            return f"Page text content:\n{text[:1000]}..." if len(text) > 1000 else f"Page text content:\n{text}"
        except Exception as e:
            return f"✗ Failed to get page text: {str(e)}"


class CloseBrowserTool(BaseTool):
    name: str = "close_browser"
    description: str = "Close the browser and cleanup resources. Use this at the end of testing."

    def _run(self) -> str:
        try:
            browser_manager = BrowserManager.get_instance()
            browser_manager.close_browser()
            return "✓ Browser closed successfully"
        except Exception as e:
            return f"✗ Failed to close browser: {str(e)}"


# Export all tools
__all__ = [
    "NavigateTool",
    "ClickTool",
    "TypeTool",
    "SnapshotTool",
    "ScreenshotTool",
    "FillFormTool",
    "WaitForTool",
    "EvaluateTool",
    "VerifyElementTool",
    "GetCurrentUrlTool",
    "GetPageTextTool",
    "CloseBrowserTool",
    "BrowserManager"
]
