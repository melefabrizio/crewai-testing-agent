"""Playwright MCP Server configuration for CrewAI"""

import os
from mcp import StdioServerParameters


def get_playwright_mcp_params(headless: bool = True, browser: str = "chromium") -> StdioServerParameters:
    """
    Get Playwright MCP server parameters for stdio connection.

    Args:
        headless: Run browser in headless mode (default: True)
        browser: Browser type - chromium, firefox, webkit (default: chromium)

    Returns:
        StdioServerParameters configured for Playwright MCP server
    """
    args = ["@playwright/mcp@latest"]

    # Add headless flag if requested
    if headless:
        args.append("--headless")

    # Add browser selection if not chromium
    if browser != "chromium":
        args.extend(["--browser", browser])

    return StdioServerParameters(
        command="npx",
        args=args,
        env=os.environ.copy()
    )


def get_playwright_mcp_params_with_config(config_path: str = None, **options) -> StdioServerParameters:
    """
    Get Playwright MCP server parameters with optional configuration file.

    Args:
        config_path: Path to Playwright MCP configuration file
        **options: Additional options like headless, browser, caps

    Returns:
        StdioServerParameters configured for Playwright MCP server
    """
    args = ["@playwright/mcp@latest"]

    # Add config file path if provided
    if config_path:
        args.extend(["--config", config_path])

    # Add headless flag
    if options.get("headless", True):
        args.append("--headless")

    # Add browser selection
    if "browser" in options:
        args.extend(["--browser", options["browser"]])

    # Add capabilities
    if "caps" in options:
        args.extend(["--caps", options["caps"]])

    return StdioServerParameters(
        command="npx",
        args=args,
        env=os.environ.copy()
    )
