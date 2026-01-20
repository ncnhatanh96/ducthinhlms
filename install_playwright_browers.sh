#!/bin/bash
# Install Playwright with all browser options

echo "📦 Installing Playwright with browsers..."

# Install Playwright

# Install all browsers
echo "📥 Installing Firefox, Chromium, and Chrome..."
playwright install firefox chrome

# Install system dependencies
echo "📥 Installing system dependencies..."
playwright install-deps

echo ""
echo "✅ Installation complete!"
echo ""
echo "Installed browsers:"
echo "  - Firefox (RECOMMENDED for stealth)"
echo "  - Chromium"
echo "  - Chrome (uses your system Chrome)"
echo ""
echo "To run:"
echo "  python3 course_keeper_playwright_stealth. py"
