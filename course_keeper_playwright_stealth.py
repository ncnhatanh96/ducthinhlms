"""
Course Auto-Keep-Alive Tool - Playwright with Maximum Stealth
Uses real Firefox or Chrome with extensive anti-detection measures
"""

from playwright.sync_api import sync_playwright
import time
import random
import math
import os

class PlaywrightStealthKeeper:
    def __init__(self, url, check_interval=45, browser_type='firefox'):
        """
        Initialize the course keeper with Playwright
        
        Args: 
            url: The URL of the learning website
            check_interval: Minutes between activity simulations (default: 45)
            browser_type: 'firefox', 'chromium', or 'chrome' (default: 'firefox')
        """
        self.url = url
        self.check_interval = check_interval * 60
        self.browser_type = browser_type
        
    def bezier_curve_points(self, start_x, start_y, end_x, end_y, steps=30):
        """Generate points along a Bezier curve"""
        ctrl1_x = start_x + random.randint(-100, 100)
        ctrl1_y = start_y + random.randint(-100, 100)
        ctrl2_x = end_x + random.randint(-100, 100)
        ctrl2_y = end_y + random.randint(-100, 100)
        
        points = []
        for i in range(steps + 1):
            t = i / steps
            x = (1-t)**3 * start_x + 3*(1-t)**2*t * ctrl1_x + 3*(1-t)*t**2 * ctrl2_x + t**3 * end_x
            y = (1-t)**3 * start_y + 3*(1-t)**2*t * ctrl1_y + 3*(1-t)*t**2 * ctrl2_y + t**3 * end_y
            points.append((int(x), int(y)))
        
        return points
    
    def human_mouse_movement(self, page):
        """Simulate natural human mouse movements with Bezier curves"""
        viewport_size = page.viewport_size
        width = viewport_size['width']
        height = viewport_size['height']
        
        # Current position
        current_x = random.randint(100, width - 100)
        current_y = random.randint(100, height - 100)
        
        # Make 2-4 movements
        movements = random.randint(2, 4)
        
        for _ in range(movements):
            target_x = random.randint(100, width - 100)
            target_y = random.randint(100, height - 100)
            
            # Get Bezier curve points
            points = self.bezier_curve_points(current_x, current_y, target_x, target_y)
            
            # Move along the curve
            for x, y in points:
                page.mouse.move(x, y)
                time.sleep(random.uniform(0.01, 0.03))
            
            current_x, current_y = target_x, target_y
            time.sleep(random.uniform(0.5, 2.0))
        
        print(f"🖱️  Completed {movements} natural mouse movements")
    
    def natural_scroll(self, page):
        """Simulate natural scrolling behavior"""
        total_scrolls = random.randint(3, 6)
        direction = random.choice([1, -1])
        
        for _ in range(total_scrolls):
            scroll_amount = random.randint(100, 300) * direction
            page.mouse. wheel(0, scroll_amount)
            time.sleep(random.uniform(0.3, 0.8))
        
        direction_str = "down" if direction > 0 else "up"
        print(f"📜 Scrolled {direction_str} in {total_scrolls} natural chunks")
    
    def micro_movements(self, page):
        """Tiny unconscious movements"""
        viewport_size = page.viewport_size
        center_x = viewport_size['width'] // 2
        center_y = viewport_size['height'] // 2
        
        current_x = center_x + random.randint(-200, 200)
        current_y = center_y + random. randint(-200, 200)
        
        for _ in range(random.randint(5, 10)):
            new_x = current_x + random.randint(-20, 20)
            new_y = current_y + random. randint(-20, 20)
            
            new_x = max(50, min(viewport_size['width'] - 50, new_x))
            new_y = max(50, min(viewport_size['height'] - 50, new_y))
            
            steps = random.randint(5, 10)
            for i in range(steps):
                t = i / steps
                x = current_x + (new_x - current_x) * t
                y = current_y + (new_y - current_y) * t
                page.mouse.move(int(x), int(y))
                time.sleep(random.uniform(0.02, 0.05))
            
            current_x, current_y = new_x, new_y
            time.sleep(random.uniform(0.1, 0.3))
        
        print(f"🖱️  Subtle micro-movements completed")
    
    def reading_behavior(self, page):
        """Simulate reading with small scrolls and pauses"""
        reading_scrolls = random.randint(3, 6)
        
        for _ in range(reading_scrolls):
            scroll_amount = random.randint(50, 150)
            page.mouse.wheel(0, scroll_amount)
            
            # Reading pause with occasional micro-movements
            reading_time = random.uniform(2, 5)
            pause_start = time.time()
            
            while time.time() - pause_start < reading_time:
                if random.random() < 0.3:
                    current_pos = page.evaluate("() => ({x: window.innerWidth/2, y: window.innerHeight/2})")
                    page.mouse.move(
                        current_pos. get('x', 500) + random.randint(-5, 5),
                        current_pos.get('y', 500) + random.randint(-5, 5)
                    )
                time.sleep(0.5)
        
        print(f"📖 Simulated reading behavior ({reading_scrolls} sections)")
    
    def simulate_activity(self, page):
        """Perform random human-like activities"""
        activities = [
            (self.human_mouse_movement, 0.30),
            (self.natural_scroll, 0.30),
            (self.reading_behavior, 0.25),
            (self.micro_movements, 0.15),
        ]
        
        num_activities = random.randint(2, 3)
        
        for _ in range(num_activities):
            rand = random.random()
            cumulative = 0
            selected_activity = activities[0][0]
            
            for activity, weight in activities:
                cumulative += weight
                if rand <= cumulative:
                    selected_activity = activity
                    break
            
            try:
                selected_activity(page)
            except Exception as e: 
                print(f"⚠️  Activity error: {e}")
            
            time.sleep(random. uniform(1, 3))
    
    def check_wsl_display(self):
        """Check if display is available in WSL"""
        display = os.environ.get('DISPLAY')
        if display:
            print(f"✅ Display found: {display}")
            return True
        else: 
            print("ℹ️  No display detected - will run in headless mode")
            return False
    
    def run(self, headless=None, manual_login_wait=300):
        """
        Start the course keeper
        
        Args:
            headless: Run browser in headless mode (None = auto-detect for WSL)
            manual_login_wait:  Seconds to wait for manual login (default:  300)
        """
        print(f"🚀 Starting Playwright Stealth Course Keeper...")
        print(f"📍 URL: {self.url}")
        print(f"🌐 Browser: {self.browser_type. upper()}")
        print(f"⏱️  Activity interval: ~{self.check_interval/60:.1f} minutes")
        
        # Auto-detect headless mode for WSL
        if headless is None:
            has_display = self.check_wsl_display()
            headless = not has_display
        
        print(f"👁️  Headless mode: {headless}")
        print("-" * 60)
        
        with sync_playwright() as p:
            try:
                # Select browser
                if self.browser_type == 'firefox':
                    print("🦊 Launching Firefox with stealth configuration...")
                    browser = p. firefox.launch(
                        headless=headless,
                        firefox_user_prefs={
                            'dom.webdriver. enabled': False,
                            'useAutomationExtension': False,
                            'general.useragent.override': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'
                        }
                    )
                elif self.browser_type == 'chrome':
                    print("🌐 Launching Chrome (installed) with stealth configuration...")
                    browser = p.chromium. launch(
                        headless=headless,
                        channel='chrome',  # Use installed Chrome, not Chromium
                        args=[
                            '--disable-blink-features=AutomationControlled',
                            '--disable-dev-shm-usage',
                            '--no-sandbox',
                            '--disable-setuid-sandbox',
                        ]
                    )
                else:  # chromium
                    print("🌐 Launching Chromium with stealth configuration...")
                    browser = p.chromium.launch(
                        headless=headless,
                        args=[
                            '--disable-blink-features=AutomationControlled',
                            '--disable-dev-shm-usage',
                            '--no-sandbox',
                            '--disable-setuid-sandbox',
                        ]
                    )
                
                # Create context with realistic settings
                context_options = {
                    'viewport': {'width': 1920, 'height': 1080},
                    'locale': 'en-US',
                    'timezone_id': 'America/New_York',
                    'color_scheme': 'light',
                }
                
                # Browser-specific user agents
                if self.browser_type == 'firefox':
                    context_options['user_agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'
                else: 
                    context_options['user_agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                
                context = browser.new_context(**context_options)
                
                # Inject stealth scripts (for Chromium/Chrome)
                if self.browser_type != 'firefox':
                    context.add_init_script("""
                        // Remove webdriver property
                        Object.defineProperty(navigator, 'webdriver', {
                            get: () => undefined
                        });
                        
                        // Mock plugins
                        Object.defineProperty(navigator, 'plugins', {
                            get: () => [
                                {
                                    0: {type: "application/x-google-chrome-pdf", suffixes: "pdf", description: "Portable Document Format"},
                                    description: "Portable Document Format",
                                    filename: "internal-pdf-viewer",
                                    length: 1,
                                    name: "Chrome PDF Plugin"
                                }
                            ]
                        });
                        
                        // Mock languages
                        Object.defineProperty(navigator, 'languages', {
                            get: () => ['en-US', 'en']
                        });
                        
                        // Mock chrome object
                        window.chrome = {
                            runtime: {}
                        };
                        
                        // Override permissions query
                        const originalQuery = window.navigator.permissions.query;
                        window.navigator.permissions.query = (parameters) => (
                            parameters.name === 'notifications' ? 
                                Promise.resolve({state:  Notification.permission}) :
                                originalQuery(parameters)
                        );
                    """)
                
                page = context.new_page()
                
                # Navigate to the website
                print(f"🌐 Navigating to {self.url}")
                page.goto(self. url, wait_until='domcontentloaded', timeout=60000)
                print("✅ Page loaded")
                
                # Wait for manual login
                print("\n" + "="*60)
                print("🔐 PLEASE LOGIN MANUALLY NOW")
                print("="*60)
                print(f"⏰ You have {manual_login_wait//60} minutes to:")
                print("   1. Complete login")
                print("   2. Navigate to your course/lesson page")
                print("   3. Start the video/content if needed")
                print("   4. Just leave the browser open")
                print("\n💡 The script will keep the session active")
                print("="*60 + "\n")
                
                # Countdown
                for remaining in range(manual_login_wait, 0, -30):
                    mins, secs = divmod(remaining, 60)
                    print(f"⏳ Time remaining: {mins: 02d}:{secs:02d}")
                    time.sleep(30)
                
                current_url = page.url
                print(f"\n✅ Starting monitoring on:  {current_url}")
                print("🎯 Keep this terminal open.  Press Ctrl+C to stop.\n")
                
                # Main activity loop
                iteration = 0
                while True: 
                    iteration += 1
                    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                    print(f"\n{'='*60}")
                    print(f"⏰ Activity Session #{iteration} - {current_time}")
                    print(f"{'='*60}")
                    
                    # Check if page is still alive
                    if page.is_closed():
                        print("❌ Page was closed.  Exiting...")
                        break
                    
                    # Simulate activity
                    try:
                        print("🤖 Simulating human behavior...")
                        self.simulate_activity(page)
                        print("✅ Activity session completed")
                    except Exception as e:
                        print(f"⚠️  Error during activity: {e}")
                        import traceback
                        traceback. print_exc()
                    
                    # Calculate next interval with variance
                    variance = random.randint(-300, 300)  # ±5 minutes
                    next_interval = self.check_interval + variance
                    
                    next_time = time.time() + next_interval
                    next_time_str = time.strftime('%H:%M:%S', time.localtime(next_time))
                    
                    print(f"\n💤 Next activity in ~{next_interval/60:.1f} minutes")
                    print(f"⏭️  Approximately at: {next_time_str}")
                    
                    time.sleep(next_interval)
            
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted by user (Ctrl+C)")
            except Exception as e:
                print(f"\n❌ Error occurred: {e}")
                import traceback
                traceback.print_exc()
            finally:
                try:
                    browser.close()
                except:
                    pass
                print("\n👋 Course Keeper stopped")


def main():
    print("""
    ╔════════════════════════════════════════════════╗
    ║   Course Keeper - Playwright Stealth 🥷       ║
    ║     Firefox/Chrome with Anti-Detection        ║
    ╚════════════════════════════════════════════════╝
    """)
    
    print("✨ Features:")
    print("  ✅ Real Firefox (best) or Chrome")
    print("  ✅ Extensive stealth scripts")
    print("  ✅ Bezier curve mouse movements")
    print("  ✅ Random timing variance")
    print("  ✅ Manual login only")
    print("")
    
    # Configuration
    course_url = input("Enter your course URL: ").strip()
    if not course_url:
        print("❌ No URL provided. Exiting.")
        return
    
    print("\nBrowser options:")
    print("  1. Firefox (RECOMMENDED - harder to detect)")
    print("  2. Chrome (uses your installed Chrome)")
    print("  3. Chromium (Playwright's Chromium)")
    browser_choice = input("Select browser (1/2/3, default=1): ").strip() or "1"
    
    browser_map = {
        "1": "firefox",
        "2": "chrome",
        "3": "chromium"
    }
    browser_type = browser_map.get(browser_choice, "firefox")
    
    try:
        interval_input = input("Enter activity interval in minutes (default:  45): ").strip()
        interval = int(interval_input) if interval_input else 45
    except ValueError:
        print("⚠️  Invalid input. Using default:  45 minutes")
        interval = 45
    
    try:
        wait_input = input("How long to wait for manual login in minutes (default: 5): ").strip()
        wait_time = int(wait_input) * 60 if wait_input else 300
    except ValueError:
        print("⚠️  Invalid input. Using default: 5 minutes")
        wait_time = 300
    
    browser_name = {"firefox": "Firefox", "chrome": "Chrome", "chromium": "Chromium"}[browser_type]
    print(f"\n✅ Configuration:")
    print(f"   URL: {course_url}")
    print(f"   Browser: {browser_name}")
    print(f"   Interval: {interval} minutes (±5 min variance)")
    print(f"   Login wait: {wait_time//60} minutes")
    print(f"\nPress Ctrl+C to stop at any time\n")
    
    input("Press Enter to start...")
    
    # Create and run keeper
    keeper = PlaywrightStealthKeeper(course_url, check_interval=interval, browser_type=browser_type)
    keeper.run(headless=None, manual_login_wait=wait_time)


if __name__ == "__main__":
    main()
