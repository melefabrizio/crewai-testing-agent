"""
Example usage of the Frontend Test Crew

This script demonstrates how to use the multi-agent testing system
to test various web application scenarios.
"""

import os
from dotenv import load_dotenv
from src.frontend_test_crew.crew import FrontendTestCrew


def example_login_test():
    """Example: Testing a login flow"""
    print("\n" + "="*60)
    print("Example 1: Login Flow Test")
    print("="*60 + "\n")

    crew = FrontendTestCrew()

    result = crew.test_website(
        website_url="https://example.com/login",
        test_scenario="""
        Test the complete login workflow:
        1. Navigate to the login page
        2. Fill in the username field with 'testuser@example.com'
        3. Fill in the password field with 'password123'
        4. Click the 'Sign In' button
        5. Verify that the user is redirected to the dashboard
        6. Verify that the user's name is displayed in the header
        """,
        additional_context="Test both successful login and error handling for invalid credentials"
    )

    print(f"\n✅ Test Status: {result['status']}")
    if result['status'] == 'completed':
        print(f"\n{result['result']}")


def example_form_submission_test():
    """Example: Testing a form submission"""
    print("\n" + "="*60)
    print("Example 2: Form Submission Test")
    print("="*60 + "\n")

    crew = FrontendTestCrew()

    result = crew.test_website(
        website_url="https://example.com/contact",
        test_scenario="""
        Test the contact form submission:
        1. Navigate to the contact page
        2. Fill in the name field
        3. Fill in the email field
        4. Fill in the message textarea
        5. Click the submit button
        6. Verify success message is displayed
        7. Verify form is cleared after submission
        """,
        additional_context="Test form validation for empty fields and invalid email formats"
    )

    print(f"\n✅ Test Status: {result['status']}")
    if result['status'] == 'completed':
        print(f"\n{result['result']}")


def example_navigation_test():
    """Example: Testing navigation and page elements"""
    print("\n" + "="*60)
    print("Example 3: Navigation Test")
    print("="*60 + "\n")

    crew = FrontendTestCrew()

    result = crew.test_website(
        website_url="https://example.com",
        test_scenario="""
        Test the main navigation:
        1. Navigate to the homepage
        2. Click on the 'Products' menu item
        3. Verify products page loads with product listings
        4. Click on a specific product
        5. Verify product detail page shows correct information
        6. Click 'Add to Cart' button
        7. Verify cart count increases
        """,
        additional_context="Ensure all navigation links work and pages load correctly"
    )

    print(f"\n✅ Test Status: {result['status']}")
    if result['status'] == 'completed':
        print(f"\n{result['result']}")


def example_search_test():
    """Example: Testing search functionality"""
    print("\n" + "="*60)
    print("Example 4: Search Functionality Test")
    print("="*60 + "\n")

    crew = FrontendTestCrew()

    result = crew.test_website(
        website_url="https://example.com",
        test_scenario="""
        Test the search functionality:
        1. Navigate to the homepage
        2. Locate the search input field
        3. Type 'laptop' into the search field
        4. Click the search button or press Enter
        5. Verify search results page loads
        6. Verify results contain items related to 'laptop'
        7. Test with no results - search for 'xyz123nonexistent'
        8. Verify appropriate 'no results' message is shown
        """,
        additional_context="Test both successful searches and empty result scenarios"
    )

    print(f"\n✅ Test Status: {result['status']}")
    if result['status'] == 'completed':
        print(f"\n{result['result']}")


def custom_test():
    """Run a custom test scenario"""
    print("\n" + "="*60)
    print("Custom Test Scenario")
    print("="*60 + "\n")

    # Get custom inputs
    website_url = input("Enter website URL to test: ").strip()
    if not website_url:
        website_url = "https://example.com"

    print("\nEnter test scenario (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    test_scenario = "\n".join(lines)

    if not test_scenario:
        test_scenario = "Navigate to the homepage and verify it loads correctly"

    crew = FrontendTestCrew()

    result = crew.test_website(
        website_url=website_url,
        test_scenario=test_scenario
    )

    print(f"\n✅ Test Status: {result['status']}")
    if result['status'] == 'completed':
        print(f"\n{result['result']}")


def main():
    """Main function to run examples"""
    # Load environment variables
    load_dotenv()

    # Check for API key
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  Error: No API key found!")
        print("Please set OPENAI_API_KEY or ANTHROPIC_API_KEY in your .env file")
        print("\nCopy .env.example to .env and add your API key:")
        print("  cp .env.example .env")
        return

    print("🤖 Frontend Test Crew - Multi-Agent Testing System")
    print("="*60)

    while True:
        print("\nSelect an example to run:")
        print("1. Login Flow Test")
        print("2. Form Submission Test")
        print("3. Navigation Test")
        print("4. Search Functionality Test")
        print("5. Custom Test Scenario")
        print("0. Exit")

        choice = input("\nEnter your choice (0-5): ").strip()

        if choice == "1":
            example_login_test()
        elif choice == "2":
            example_form_submission_test()
        elif choice == "3":
            example_navigation_test()
        elif choice == "4":
            example_search_test()
        elif choice == "5":
            custom_test()
        elif choice == "0":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
