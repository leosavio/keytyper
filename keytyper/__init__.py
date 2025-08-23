"""
KeyTyper - Cross-Platform Terminal Text Formatter

A powerful, cross-platform Python library for creating beautiful terminal output
with typing effects, colors, and formatting. KeyTyper automatically detects your
operating system and provides optimal terminal support for Windows, macOS, and Linux.

Features:
- ✨ Simulated typing effect - Display text with realistic typing animation
- 🎨 Rich formatting - Apply colors, bold, italic, underline styles
- 🖥️ Cross-platform - Works seamlessly on Windows, macOS, and Linux
- 🔍 OS Detection - Automatically detects and optimizes for your operating system
- 🌈 ANSI Color Support - Full support for 16 colors plus bright variants
- 🚀 Easy API - Simple and intuitive methods for all use cases
- ⚡ Performance - Efficient ANSI sequence handling
- 🛡️ Safe - No low-level system dependencies that cause compatibility issues

Author: Leonardo Savio Ferreira
License: MIT
Version: 0.1.0
"""

from .keytyper import KeyTyper

__version__ = "0.1.0"
__author__ = "Leonardo Savio Ferreira"
__email__ = "leosavio@leosavio.com"
__license__ = "MIT"
__description__ = "A powerful, cross-platform Python library for creating beautiful terminal output with typing effects, colors, and formatting"

# Export main class
__all__ = ["KeyTyper"]
