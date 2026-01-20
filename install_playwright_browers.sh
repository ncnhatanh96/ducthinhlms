#!/bin/bash
# Install Playwright with all browser options
# Supports both Linux and macOS

echo "📦 Installing Playwright with browsers..."

# Detect OS
OS="$(uname -s)"
case "${OS}" in
    Linux*)     MACHINE=Linux;;
    Darwin*)    MACHINE=Mac;;
    *)          MACHINE="UNKNOWN: ${OS}"
esac

echo "🖥️  Detected OS: ${MACHINE}"
echo ""

# Install Playwright

# Install all browsers
echo "📥 Installing Firefox, Chromium, and Chrome..."
playwright install firefox chrome

# Install system dependencies (Linux only)
if [ "${MACHINE}" = "Linux" ]; then
    echo "📥 Installing system dependencies..."
    playwright install-deps
elif [ "${MACHINE}" = "Mac" ]; then
    echo "ℹ️  macOS detected - skipping system dependencies (not required)"
    echo "ℹ️  Note: If you encounter issues, ensure you have:"
    echo "    - Xcode Command Line Tools installed"
    echo "    - Homebrew installed (optional, but recommended)"
else
    echo "⚠️  Unknown OS detected.  System dependencies may need manual installation."
fi

echo ""
echo "✅ Installation complete!"
echo ""
echo "Installed browsers:"
echo "  - Firefox (RECOMMENDED for stealth)"
echo "  - Chromium"
echo "  - Chrome (uses your system Chrome)"
echo ""
if [ "${MACHINE}" = "Mac" ]; then
    echo "💡 macOS Tips:"
    echo "  - Firefox is the recommended browser for stealth mode"
    echo "  - Chrome will use your system installation if available"
    echo ""
fi
echo "To run:"
echo "  python3 course_keeper_playwright_stealth. py"
