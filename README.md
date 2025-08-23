# KeyTyper 🎨⌨️

[![PyPI version](https://badge.fury.io/py/keytyper.svg)](https://badge.fury.io/py/keytyper)
[![Python Support](https://img.shields.io/pypi/pyversions/keytyper.svg)](https://pypi.org/project/keytyper/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/keytyper)](https://pepy.tech/project/keytyper)

A powerful, cross-platform Python library for creating beautiful terminal output with typing effects, colors, and formatting. KeyTyper automatically detects your operating system and provides optimal terminal support for Windows, macOS, and Linux.

## ✨ Features

- **🎬 Simulated Typing Effect** - Display text with realistic typing animation
- **🎨 Rich Formatting** - Apply colors, bold, italic, underline styles
- **🖥️ Cross-Platform** - Works seamlessly on Windows, macOS, and Linux
- **🔍 OS Detection** - Automatically detects and optimizes for your operating system
- **🌈 ANSI Color Support** - Full support for 16 colors plus bright variants
- **🚀 Easy API** - Simple and intuitive methods for all use cases
- **⚡ Performance** - Efficient ANSI sequence handling
- **🛡️ Safe** - No low-level system dependencies that cause compatibility issues
- **📦 Lightweight** - Zero required dependencies (uses only Python standard library)

## 🚀 Quick Start

### Installation

```bash
pip install keytyper
```

### Basic Usage

```python
from keytyper import KeyTyper

# Create a KeyTyper instance
kt = KeyTyper()

# Print with typing effect
kt.print("Hello, World!", fore_color="green", bold=True)

# Print instantly without typing effect
kt.print_instant("This appears immediately!", fore_color="blue")

# Use convenience methods
kt.print_success("Operation completed successfully!")
kt.print_error("Something went wrong!")
kt.print_warning("This is a warning message")
kt.print_info("Here's some information")
```

## 📖 Comprehensive Examples

### Basic Text Formatting

```python
from keytyper import KeyTyper

kt = KeyTyper()

# Different colors
kt.print("Red text", fore_color="red")
kt.print("Green background", back_color="green")
kt.print("Blue text on yellow background", fore_color="blue", back_color="yellow")

# Text styles
kt.print("Bold text", bold=True)
kt.print("Italic text", italics=True)
kt.print("Underlined text", underline=True)
kt.print("Combined styles", fore_color="magenta", bold=True, underline=True)
```

### Typing Effects

```python
# Customize typing speed
kt.print("Slow typing...", speed=0.1)
kt.print("Fast typing!", speed=0.02)

# Default instance speed
kt = KeyTyper(speed=0.05, fore_color="cyan", bold=True)
kt.print("This uses the default settings")
```

### Convenience Methods

```python
# Predefined message types
kt.print_success("✅ Task completed successfully!")
kt.print_error("❌ An error occurred!")
kt.print_warning("⚠️ Warning: Check your input")
kt.print_info("ℹ️ Processing your request...")
kt.print_ai_response("🤖 AI: How can I help you today?")
```

### Interactive Features

```python
# User input with formatted prompt
name = kt.print_user_prompt("👤 Enter your name: ")
kt.print_success(f"Hello, {name}!")

# Clear screen
kt.clear_screen()

# Print banners
kt.print_banner("WELCOME TO KEYTYPER", char="=", width=50)
```

### Advanced Usage

```python
# Get OS information
os_info = kt.get_os_info()
kt.print_info(f"Running on: {os_info['system']} {os_info['release']}")

# Check color support
if kt.supports_color:
    kt.print("Your terminal supports colors! 🌈", fore_color="bright_green")
else:
    kt.print("Color support not detected")

# Custom formatting
kt.print("Custom message", 
         fore_color="bright_cyan", 
         back_color="black", 
         bold=True, 
         underline=True,
         speed=0.03)
```

## 🎨 Available Colors

### Foreground Colors
- `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`
- `bright_black`, `bright_red`, `bright_green`, `bright_yellow`
- `bright_blue`, `bright_magenta`, `bright_cyan`, `bright_white`

### Background Colors
Same as foreground colors, applied as background

### Text Styles
- `bold` - Bold text
- `italics` - Italic text (may not work on all terminals)
- `underline` - Underlined text

## 🖥️ Platform Support

KeyTyper is designed to work seamlessly across different operating systems:

### Windows
- Automatic ANSI support detection
- Optional colorama integration for enhanced compatibility
- Fallback support for older Windows versions

### macOS
- Native ANSI support
- Optimized for Terminal.app and iTerm2
- Full color and formatting support

### Linux
- Native ANSI support
- Compatible with all major terminal emulators
- Full feature support

## 🔧 Configuration

### Default Settings

```python
# Create with custom defaults
kt = KeyTyper(
    speed=0.05,           # Typing speed (seconds per character)
    fore_color="green",   # Default foreground color
    back_color=None,      # Default background color
    bold=True,            # Default bold styling
    underline=False,      # Default underline styling
    italics=False         # Default italic styling
)
```

### Environment Variables

KeyTyper respects standard environment variables:
- `NO_COLOR` - Disable color output
- `FORCE_COLOR` - Force color output even if not detected

## 🧪 Why KeyTyper?

KeyTyper was created to solve compatibility issues with other terminal libraries, particularly on macOS. Unlike libraries that depend on low-level system access or have complex dependencies, KeyTyper:

- **Uses only Python standard library** - No external dependencies required
- **Cross-platform by design** - Tested on Windows, macOS, and Linux
- **Handles ANSI sequences properly** - Efficient and reliable color/formatting
- **Provides typing effects** - Engaging user experience without complexity
- **Automatic fallbacks** - Works even on limited terminals

## 📚 API Reference

### KeyTyper Class

#### Constructor
```python
KeyTyper(speed=0.05, fore_color="green", back_color=None, bold=True, underline=False, italics=False)
```

#### Methods
- `print(text, **kwargs)` - Print with typing effect
- `print_instant(text, **kwargs)` - Print immediately
- `print_success(text, speed=None)` - Print success message
- `print_error(text, speed=None)` - Print error message
- `print_warning(text, speed=None)` - Print warning message
- `print_info(text, speed=None)` - Print info message
- `print_ai_response(text, speed=None)` - Print AI response
- `print_user_prompt(prompt="")` - Get user input with prompt
- `clear_screen()` - Clear terminal screen
- `print_banner(text, char="=", width=60)` - Print banner
- `get_os_info()` - Get OS information

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/leosavio/keytyper.git
cd keytyper

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Format code
black keytyper/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the need for a reliable, cross-platform terminal formatting library
- Built to replace problematic dependencies in educational and professional projects
- Thanks to the Python community for feedback and suggestions

---

**Made with ❤️ for developers who love beautiful terminal output**
