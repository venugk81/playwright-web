"""
Simple Playwright script to open Chrome and navigate to amazon.in
https://rahulshettyacademy.com/AutomationPractice/
"""

from playwright.sync_api import sync_playwright
import time


def open_amazon():
    """
    Opens Chrome browser and navigates to amazon.in using Playwright.
    
    This script:
    - Launches a Chromium browser in non-headless mode (visible window)
    - Creates a new page
    - Navigates to https://www.amazon.in
    - Waits for 10 seconds to allow user interaction
    - Closes the browser
    
    Raises:
        Exception: If Playwright or browser setup fails
    """
    try:
        with sync_playwright() as p:
            # Launch Chrome (Chromium) in non-headless mode
            print("🚀 Launching Chrome browser...")
            browser = p.chromium.launch(headless=False)
            
            # Create a new page
            print("📄 Creating new page...")
            context = browser.new_context()
            page = context.new_page()
            
            # Navigate to amazon.in
            print("🌐 Navigating to amazon.in...")
            page.goto("https://www.amazon.in")
            
            # Get page title and URL for verification
            title = page.title()
            url = page.url
            print(f"✅ Successfully loaded: {title}")
            print(f"📍 Current URL: {url}")
            
            # Keep the browser open for 10 seconds to allow interaction
            print("⏳ Browser will stay open for 10 seconds...")
            time.sleep(10)
            
            # Close the browser
            print("🔒 Closing browser...")
            browser.close()
            print("✅ Done!")
            
    except Exception as e:
        print(f"❌ Error occurred: {type(e).__name__}")
        print(f"📝 Error details: {str(e)}")
        raise


if __name__ == "__main__":
    open_amazon()

