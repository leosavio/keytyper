#!/usr/bin/env python3
"""
Basic usage examples for KeyTyper.

This script demonstrates the fundamental features of KeyTyper including
typing effects, colors, formatting, and convenience methods.
"""

from keytyper import KeyTyper
import time


def main():
    """Run basic usage examples."""
    # Create a KeyTyper instance
    kt = KeyTyper()

    # Clear screen and show banner
    kt.clear_screen()
    kt.print_banner("KEYTYPER BASIC EXAMPLES", char="=", width=60)
    print()

    # Basic typing effect
    kt.print("Welcome to KeyTyper! 🎉", fore_color="bright_green", bold=True)
    kt.print("This text appears with a typing effect...", speed=0.08)
    print()

    # Different colors
    kt.print("🔴 Red text", fore_color="red")
    kt.print("🟢 Green text", fore_color="green")
    kt.print("🔵 Blue text", fore_color="blue")
    kt.print("🟡 Yellow text", fore_color="yellow")
    kt.print("🟣 Magenta text", fore_color="magenta")
    kt.print("🔵 Cyan text", fore_color="cyan")
    print()

    # Bright colors
    kt.print("✨ Bright red", fore_color="bright_red")
    kt.print("✨ Bright green", fore_color="bright_green")
    kt.print("✨ Bright blue", fore_color="bright_blue")
    kt.print("✨ Bright yellow", fore_color="bright_yellow")
    print()

    # Text styles
    kt.print("Bold text", bold=True, fore_color="white")
    kt.print("Italic text", italics=True, fore_color="white")
    kt.print("Underlined text", underline=True, fore_color="white")
    kt.print(
        "Combined: Bold + Underline",
        bold=True,
        underline=True,
        fore_color="bright_cyan",
    )
    print()

    # Background colors
    kt.print("Text with red background", back_color="red", fore_color="white")
    kt.print("Text with blue background", back_color="blue", fore_color="white")
    kt.print(
        "Colorful combination",
        fore_color="bright_yellow",
        back_color="magenta",
        bold=True,
    )
    print()

    # Convenience methods
    kt.print_success("✅ This is a success message!")
    kt.print_error("❌ This is an error message!")
    kt.print_warning("⚠️ This is a warning message!")
    kt.print_info("ℹ️ This is an info message!")
    kt.print_ai_response("Hello! I'm an AI assistant. How can I help you?")
    print()

    # Speed variations
    kt.print("Very slow typing...", speed=0.15, fore_color="bright_red")
    kt.print("Normal speed typing", speed=0.05, fore_color="bright_green")
    kt.print("Fast typing!", speed=0.02, fore_color="bright_blue")
    kt.print_instant("Instant text (no typing effect)", fore_color="bright_magenta")
    print()

    # Interactive example
    kt.print("Let's try some interaction!", fore_color="bright_cyan", bold=True)
    name = kt.print_user_prompt("👤 What's your name? ")
    kt.print_success(f"Nice to meet you, {name}! 🤝")

    favorite_color = kt.print_user_prompt("🎨 What's your favorite color? ")
    kt.print(
        f"Great choice! {favorite_color} is a beautiful color! 🌈",
        fore_color=(
            favorite_color.lower()
            if favorite_color.lower() in kt.fg_colors
            else "white"
        ),
    )
    print()

    # OS Information
    kt.print(
        "System Information:", fore_color="bright_white", bold=True, underline=True
    )
    os_info = kt.get_os_info()
    kt.print_info(f"Operating System: {os_info['system']} {os_info['release']}")
    kt.print_info(f"Machine: {os_info['machine']}")
    kt.print_info(f"Color Support: {'Yes' if os_info['supports_color'] else 'No'}")
    print()

    # Final banner
    kt.print_banner("EXAMPLES COMPLETE", char="*", width=60)
    kt.print("Thanks for trying KeyTyper! 🚀", fore_color="bright_green", bold=True)


if __name__ == "__main__":
    main()
