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

# Check for Python 3
echo "🔍 Checking for Python 3..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ Found:  ${PYTHON_VERSION}"
else
    echo "❌ Python 3 not found. Installing..."
    
    if [ "${MACHINE}" = "Linux" ]; then
        # Try to detect Linux distribution
        if [ -f /etc/debian_version ]; then
            echo "📥 Installing Python 3 on Debian/Ubuntu..."
            sudo apt-get update
            sudo apt-get install -y python3 python3-pip python3-venv
        elif [ -f /etc/redhat-release ]; then
            echo "📥 Installing Python 3 on RedHat/CentOS/Fedora..."
            sudo yum install -y python3 python3-pip
        else
            echo "⚠️  Unknown Linux distribution. Please install Python 3 manually."
            exit 1
        fi
    elif [ "${MACHINE}" = "Mac" ]; then
        echo "📥 Installing Python 3 on macOS..."
        if command -v brew &> /dev/null; then
            brew install python3
        else
            echo "⚠️  Homebrew not found. Please install Homebrew first:"
            echo "    /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install. sh)\""
            exit 1
        fi
    else
        echo "⚠️  Unknown OS.  Please install Python 3 manually."
        exit 1
    fi
    
    # Verify installation
    if command -v python3 &> /dev/null; then
        echo "✅ Python 3 installed successfully:  $(python3 --version)"
    else
        echo "❌ Failed to install Python 3. Please install manually."
        exit 1
    fi
fi

echo ""

# Check for pip
echo "🔍 Checking for pip..."
if command -v pip3 &> /dev/null; then
    echo "✅ Found:  pip3"
elif python3 -m pip --version &> /dev/null; then
    echo "✅ Found: pip (via python3 -m pip)"
else
    echo "❌ pip not found. Installing..."
    python3 -m ensurepip --default-pip || curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py
fi

echo ""

# Install Playwright Python package if not already installed
echo "🔍 Checking for Playwright..."
if python3 -c "import playwright" 2>/dev/null; then
    echo "✅ Playwright Python package already installed"
else
    echo "📥 Installing Playwright Python package..."
    python3 -m pip install playwright
fi

echo ""

# Install all browsers
echo "📥 Installing Firefox, Chromium, and Chrome..."
python3 -m playwright install firefox chrome

# Install system dependencies (Linux only)
if [ "${MACHINE}" = "Linux" ]; then
    echo "📥 Installing system dependencies..."
    python3 -m playwright install-deps
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
echo "  python3 course_keeper_playwright_stealth.py"
