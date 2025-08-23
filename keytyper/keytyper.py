"""
KeyTyper - Cross-Platform Terminal Text Formatter

A powerful, cross-platform Python library for creating beautiful terminal output 
with typing effects, colors, and formatting.

Features:
- Simulated typing effect: Display text with a realistic typing animation.
- Customizable formatting: Apply foreground and background colors, underline, bold, and italics to your printed text.
- OS Detection: Automatically detects operating system for optimal terminal support.
- Cross-platform compatibility: Works on Windows, macOS, and Linux.
- Easy-to-use API: Simple and intuitive functions for printing and input.

We cannot use keyboard lib because it has known compatibility issues on macOS, 
especially with newer Python versions and Apple Silicon Macs.
"""

import time
import random
import platform
import sys
import os


class KeyTyper:
    """
    A cross-platform terminal text formatter with typing effects and rich formatting.
    
    This class provides methods to display text with simulated typing effects,
    apply colors and formatting, and handle cross-platform terminal compatibility.
    """
    
    def __init__(self, speed=0.05, fore_color="green", back_color=None, bold=True, underline=False, italics=False):
        """
        Initialize KeyTyper with default formatting options.
        
        Args:
            speed (float): Typing speed in seconds per character (default: 0.05)
            fore_color (str): Default foreground color (default: "green")
            back_color (str): Default background color (default: None)
            bold (bool): Default bold styling (default: True)
            underline (bool): Default underline styling (default: False)
            italics (bool): Default italic styling (default: False)
        """
        self.speed = speed
        self.fore_color = fore_color
        self.back_color = back_color
        self.bold = bold
        self.underline = underline
        self.italics = italics

        # Detect operating system
        self.os_type = platform.system().lower()
        self.is_windows = self.os_type == "windows"
        self.is_macos = self.os_type == "darwin"
        self.is_linux = self.os_type == "linux"

        # Initialize Windows color support if needed
        if self.is_windows:
            self._init_windows_colors()

        # Check if terminal supports colors
        self.supports_color = self._check_color_support()

        # ANSI color codes for foreground
        self.fg_colors = {
            "black": 30, "red": 31, "green": 32, "yellow": 33,
            "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
            "bright_black": 90, "bright_red": 91, "bright_green": 92,
            "bright_yellow": 93, "bright_blue": 94, "bright_magenta": 95,
            "bright_cyan": 96, "bright_white": 97
        }

        # ANSI color codes for background
        self.bg_colors = {
            "black": 40, "red": 41, "green": 42, "yellow": 43,
            "blue": 44, "magenta": 45, "cyan": 46, "white": 47,
            "bright_black": 100, "bright_red": 101, "bright_green": 102,
            "bright_yellow": 103, "bright_blue": 104, "bright_magenta": 105,
            "bright_cyan": 106, "bright_white": 107
        }

        # ANSI style codes
        self.styles = {
            "reset": 0, "bold": 1, "dim": 2, "italics": 3,
            "underline": 4, "blink": 5, "reverse": 7, "strikethrough": 9
        }

    def _init_windows_colors(self):
        """Initialize Windows console for ANSI color support."""
        try:
            import colorama
            colorama.init()
        except ImportError:
            # Try to enable ANSI support on Windows 10+
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except:
                pass

    def _check_color_support(self):
        """Check if the terminal supports ANSI colors."""
        # Check environment variables
        if os.getenv('NO_COLOR'):
            return False
        if os.getenv('FORCE_COLOR'):
            return True

        # Check if stdout is a TTY
        if not hasattr(sys.stdout, 'isatty') or not sys.stdout.isatty():
            return False

        # Check TERM environment variable
        term = os.getenv('TERM', '').lower()
        if 'color' in term or term in ['xterm', 'xterm-256color', 'screen', 'tmux']:
            return True

        # Default to True for most modern terminals
        return True

    def _format_text(self, text, fore_color=None, back_color=None, bold=None, underline=None, italics=None):
        """Apply ANSI formatting to text."""
        if not self.supports_color:
            return text

        # Use instance defaults if not specified
        fore_color = fore_color or self.fore_color
        back_color = back_color or self.back_color
        bold = bold if bold is not None else self.bold
        underline = underline if underline is not None else self.underline
        italics = italics if italics is not None else self.italics

        codes = []

        # Add style codes
        if bold:
            codes.append(str(self.styles["bold"]))
        if underline:
            codes.append(str(self.styles["underline"]))
        if italics:
            codes.append(str(self.styles["italics"]))

        # Add foreground color
        if fore_color and fore_color.lower() in self.fg_colors:
            codes.append(str(self.fg_colors[fore_color.lower()]))

        # Add background color
        if back_color and back_color.lower() in self.bg_colors:
            codes.append(str(self.bg_colors[back_color.lower()]))

        if codes:
            return f"\033[{';'.join(codes)}m{text}\033[{self.styles['reset']}m"
        return text

    def print(self, text, speed=None, fore_color=None, back_color=None, bold=None, underline=None, italics=None, end='\n'):
        """
        Print text with typing effect and formatting.
        
        Args:
            text (str): Text to print
            speed (float): Typing speed override
            fore_color (str): Foreground color override
            back_color (str): Background color override
            bold (bool): Bold styling override
            underline (bool): Underline styling override
            italics (bool): Italic styling override
            end (str): String appended after the text (default: '\n')
        """
        speed = speed if speed is not None else self.speed
        formatted_text = self._format_text(text, fore_color, back_color, bold, underline, italics)

        # Simple approach: print each character with timing, but handle ANSI sequences properly
        i = 0
        while i < len(formatted_text):
            char = formatted_text[i]

            # Handle ANSI escape sequences
            if char == '\033' and i + 1 < len(formatted_text) and formatted_text[i + 1] == '[':
                # Find the end of the ANSI sequence
                j = i + 2
                while j < len(formatted_text) and formatted_text[j] not in ['m', 'H', 'J', 'K']:
                    j += 1
                if j < len(formatted_text):
                    j += 1  # Include the final character

                # Print the entire ANSI sequence at once
                print(formatted_text[i:j], end='', flush=True)
                i = j
            else:
                # Print regular character with typing effect
                print(char, end='', flush=True)
                # Add slight randomness to typing speed for more realistic effect
                actual_speed = speed + random.uniform(-speed * 0.3, speed * 0.3)
                time.sleep(max(0.001, actual_speed))
                i += 1

        print(end, end='', flush=True)

    def print_instant(self, text, fore_color=None, back_color=None, bold=None, underline=None, italics=None, end='\n'):
        """
        Print text instantly with formatting (no typing effect).
        
        Args:
            text (str): Text to print
            fore_color (str): Foreground color override
            back_color (str): Background color override
            bold (bool): Bold styling override
            underline (bool): Underline styling override
            italics (bool): Italic styling override
            end (str): String appended after the text (default: '\n')
        """
        formatted_text = self._format_text(text, fore_color, back_color, bold, underline, italics)
        print(formatted_text, end=end, flush=True)

    def print_success(self, text, speed=None):
        """Print success message in bright green."""
        self.print(text, speed=speed, fore_color="bright_green", bold=True)

    def print_error(self, text, speed=None):
        """Print error message in bright red."""
        self.print(text, speed=speed, fore_color="bright_red", bold=True)

    def print_warning(self, text, speed=None):
        """Print warning message in bright yellow."""
        self.print(text, speed=speed, fore_color="bright_yellow", bold=True)

    def print_info(self, text, speed=None):
        """Print info message in bright blue."""
        self.print(text, speed=speed, fore_color="bright_blue", bold=True)

    def print_ai_response(self, text, speed=None):
        """Print AI response with special formatting."""
        self.print(f"🤖 {text}", speed=speed, fore_color="bright_cyan", bold=True)

    def print_user_prompt(self, prompt=""):
        """
        Print user input prompt and return user input.
        
        Args:
            prompt (str): Prompt text to display
            
        Returns:
            str: User input
        """
        formatted_prompt = self._format_text(prompt, fore_color="bright_white", bold=True)
        return input(formatted_prompt)

    def clear_screen(self):
        """Clear the terminal screen."""
        if self.is_windows:
            os.system('cls')
        else:
            os.system('clear')

    def print_banner(self, text, char="=", width=60):
        """
        Print a banner with the given text.
        
        Args:
            text (str): Banner text
            char (str): Character to use for banner border
            width (int): Banner width
        """
        banner_line = char * width
        text_line = f"{char} {text.center(width-4)} {char}"

        self.print_instant(banner_line, fore_color="bright_magenta", bold=True)
        self.print_instant(text_line, fore_color="bright_white", bold=True)
        self.print_instant(banner_line, fore_color="bright_magenta", bold=True)

    def get_os_info(self):
        """
        Get detailed OS information.
        
        Returns:
            dict: Dictionary containing OS information
        """
        return {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "supports_color": self.supports_color
        }
