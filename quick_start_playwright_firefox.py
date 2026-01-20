#!/usr/bin/env python3
"""
Quick start - Playwright with Firefox (RECOMMENDED)
Firefox is naturally harder to detect than Chrome
"""

from course_keeper_playwright_stealth import PlaywrightStealthKeeper

# ============= CONFIGURATION =============
COURSE_URL = "https://ducthinh.huelms.com/"  # CHANGE THIS
BROWSER_TYPE = 'firefox'  # 'firefox', 'chrome', or 'chromium'
INTERVAL_MINUTES = 15  # Activity interval
LOGIN_WAIT_MINUTES = 5  # Time to login
HEADLESS = False  # True for background
# =========================================

if __name__ == "__main__": 
    print(f"🚀 Playwright Stealth Course Keeper - {BROWSER_TYPE.upper()}")
    print(f"📍 URL: {COURSE_URL}")
    print(f"⏱️  Interval: {INTERVAL_MINUTES} minutes")
    print(f"⏰ Login Wait: {LOGIN_WAIT_MINUTES} minutes")
    print(f"👁️  Headless: {HEADLESS}")
    print("\n🔐 Browser will open - LOGIN MANUALLY")
    print("Press Ctrl+C to stop\n")
    
    input("Press Enter to start...")
    
    keeper = PlaywrightStealthKeeper(
        COURSE_URL,
        check_interval=INTERVAL_MINUTES,
        browser_type=BROWSER_TYPE
    )
    keeper.run(headless=HEADLESS, manual_login_wait=LOGIN_WAIT_MINUTES * 60)
