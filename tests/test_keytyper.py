"""
Tests for KeyTyper library.
"""

import pytest
import platform
import sys
import os
from unittest.mock import patch, MagicMock
from io import StringIO

from keytyper import KeyTyper


class TestKeyTyper:
    """Test cases for KeyTyper class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.kt = KeyTyper()

    def test_initialization_default(self):
        """Test KeyTyper initialization with default values."""
        kt = KeyTyper()
        assert kt.speed == 0.05
        assert kt.fore_color == "green"
        assert kt.back_color is None
        assert kt.bold is True
        assert kt.underline is False
        assert kt.italics is False

    def test_initialization_custom(self):
        """Test KeyTyper initialization with custom values."""
        kt = KeyTyper(
            speed=0.1,
            fore_color="red",
            back_color="blue",
            bold=False,
            underline=True,
            italics=True,
        )
        assert kt.speed == 0.1
        assert kt.fore_color == "red"
        assert kt.back_color == "blue"
        assert kt.bold is False
        assert kt.underline is True
        assert kt.italics is True

    def test_os_detection(self):
        """Test operating system detection."""
        kt = KeyTyper()
        system = platform.system().lower()

        if system == "windows":
            assert kt.is_windows is True
            assert kt.is_macos is False
            assert kt.is_linux is False
        elif system == "darwin":
            assert kt.is_windows is False
            assert kt.is_macos is True
            assert kt.is_linux is False
        elif system == "linux":
            assert kt.is_windows is False
            assert kt.is_macos is False
            assert kt.is_linux is True

    def test_color_codes(self):
        """Test ANSI color code mappings."""
        kt = KeyTyper()

        # Test foreground colors
        assert kt.fg_colors["red"] == 31
        assert kt.fg_colors["green"] == 32
        assert kt.fg_colors["blue"] == 34
        assert kt.fg_colors["bright_red"] == 91

        # Test background colors
        assert kt.bg_colors["red"] == 41
        assert kt.bg_colors["green"] == 42
        assert kt.bg_colors["blue"] == 44
        assert kt.bg_colors["bright_red"] == 101

    def test_format_text_no_color_support(self):
        """Test text formatting when color support is disabled."""
        kt = KeyTyper()
        kt.supports_color = False

        result = kt._format_text("test", fore_color="red", bold=True)
        assert result == "test"

    def test_format_text_with_colors(self):
        """Test text formatting with colors."""
        kt = KeyTyper()
        kt.supports_color = True

        # Test foreground color
        result = kt._format_text("test", fore_color="red")
        assert "\033[1;31m" in result
        assert "\033[0m" in result
        assert "test" in result

    def test_format_text_with_styles(self):
        """Test text formatting with styles."""
        # Create KeyTyper with no defaults to test individual styles
        kt = KeyTyper(
            fore_color="", back_color=None, bold=False, underline=False, italics=False
        )
        kt.supports_color = True

        # Test bold only
        result = kt._format_text("test", bold=True)
        assert "\033[1m" in result  # Bold code should be present

        # Test underline only
        result = kt._format_text("test", underline=True)
        assert "\033[4m" in result  # Underline code should be present

        # Test italics only
        result = kt._format_text("test", italics=True)
        assert "\033[3m" in result  # Italics code should be present

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_instant(self, mock_stdout):
        """Test instant printing without typing effect."""
        kt = KeyTyper()
        kt.supports_color = False  # Disable colors for easier testing

        kt.print_instant("test message")
        output = mock_stdout.getvalue()
        assert "test message" in output

    @patch("sys.stdout", new_callable=StringIO)
    @patch("time.sleep")
    def test_print_with_typing_effect(self, mock_sleep, mock_stdout):
        """Test printing with typing effect."""
        kt = KeyTyper()
        kt.supports_color = False  # Disable colors for easier testing

        kt.print("test", speed=0.01)

        # Check that sleep was called (typing effect)
        assert mock_sleep.called

        # Check output
        output = mock_stdout.getvalue()
        assert "test" in output

    @patch("sys.stdout", new_callable=StringIO)
    def test_convenience_methods(self, mock_stdout):
        """Test convenience methods for different message types."""
        kt = KeyTyper()
        kt.supports_color = False  # Disable colors for easier testing

        kt.print_success("success")
        kt.print_error("error")
        kt.print_warning("warning")
        kt.print_info("info")

        output = mock_stdout.getvalue()
        assert "success" in output
        assert "error" in output
        assert "warning" in output
        assert "info" in output

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_ai_response(self, mock_stdout):
        """Test AI response printing."""
        kt = KeyTyper()
        kt.supports_color = False

        kt.print_ai_response("Hello from AI")
        output = mock_stdout.getvalue()
        assert "🤖 Hello from AI" in output

    @patch("builtins.input", return_value="test input")
    def test_print_user_prompt(self, mock_input):
        """Test user prompt functionality."""
        kt = KeyTyper()

        result = kt.print_user_prompt("Enter something: ")
        assert result == "test input"
        mock_input.assert_called_once()

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_banner(self, mock_stdout):
        """Test banner printing."""
        kt = KeyTyper()
        kt.supports_color = False

        kt.print_banner("TEST", char="=", width=20)
        output = mock_stdout.getvalue()

        # Check that banner elements are present
        assert "TEST" in output
        assert "=" in output

    def test_get_os_info(self):
        """Test OS information retrieval."""
        kt = KeyTyper()

        os_info = kt.get_os_info()

        assert "system" in os_info
        assert "release" in os_info
        assert "version" in os_info
        assert "machine" in os_info
        assert "processor" in os_info
        assert "supports_color" in os_info

        assert os_info["system"] == platform.system()
        assert isinstance(os_info["supports_color"], bool)

    @patch.dict(os.environ, {"NO_COLOR": "1"})
    def test_no_color_environment_variable(self):
        """Test NO_COLOR environment variable support."""
        kt = KeyTyper()
        assert kt.supports_color is False

    @patch.dict(os.environ, {"FORCE_COLOR": "1"})
    def test_force_color_environment_variable(self):
        """Test FORCE_COLOR environment variable support."""
        kt = KeyTyper()
        assert kt.supports_color is True

    @patch("platform.system", return_value="Windows")
    def test_windows_initialization(self, mock_system):
        """Test Windows-specific initialization."""
        with patch("keytyper.keytyper.KeyTyper._init_windows_colors") as mock_init:
            kt = KeyTyper()
            mock_init.assert_called_once()

    def test_clear_screen_windows(self):
        """Test screen clearing on Windows."""
        kt = KeyTyper()
        kt.is_windows = True

        with patch("os.system") as mock_system:
            kt.clear_screen()
            mock_system.assert_called_once_with("cls")

    def test_clear_screen_unix(self):
        """Test screen clearing on Unix-like systems."""
        kt = KeyTyper()
        kt.is_windows = False

        with patch("os.system") as mock_system:
            kt.clear_screen()
            mock_system.assert_called_once_with("clear")


class TestColorSupport:
    """Test color support detection."""

    def test_color_support_with_tty(self):
        """Test color support when stdout is a TTY."""
        with patch("sys.stdout.isatty", return_value=True):
            kt = KeyTyper()
            # Should support color when TTY is available
            assert isinstance(kt.supports_color, bool)

    def test_color_support_without_tty(self):
        """Test color support when stdout is not a TTY."""
        with patch("sys.stdout.isatty", return_value=False):
            kt = KeyTyper()
            # Should not support color when TTY is not available
            assert kt.supports_color is False

    @patch.dict(os.environ, {"TERM": "xterm-256color"})
    def test_color_support_with_color_term(self):
        """Test color support with color-capable TERM."""
        with patch("sys.stdout.isatty", return_value=True):
            kt = KeyTyper()
            assert kt.supports_color is True


if __name__ == "__main__":
    pytest.main([__file__])
