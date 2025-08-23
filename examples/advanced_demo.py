#!/usr/bin/env python3
"""
Advanced demonstration of KeyTyper features.

This script showcases more sophisticated usage patterns including
custom configurations, complex formatting, and practical applications.
"""

from keytyper import KeyTyper
import time
import random


def simulate_loading():
    """Simulate a loading process with progress indicators."""
    kt = KeyTyper(speed=0.03, fore_color="bright_blue")

    kt.print_banner("LOADING SIMULATION", char="=", width=50)

    tasks = [
        "Initializing system...",
        "Loading configuration...",
        "Connecting to database...",
        "Fetching user data...",
        "Processing information...",
        "Finalizing setup...",
    ]

    for i, task in enumerate(tasks, 1):
        kt.print(f"[{i}/{len(tasks)}] {task}", fore_color="cyan")

        # Simulate progress bar
        progress = ""
        for j in range(20):
            progress += "█"
            kt.print_instant(
                f"\r[{'█' * j}{'░' * (19-j)}] {(j+1)*5}%",
                fore_color="bright_green",
                end="",
            )
            time.sleep(0.05)

        print()  # New line after progress bar

        # Random success or warning
        if random.random() > 0.8:
            kt.print_warning(f"⚠️ Minor issue detected in {task.lower()}")
        else:
            kt.print_success(f"✅ {task} completed successfully")

        print()

    kt.print_success("🎉 All tasks completed successfully!")


def demonstrate_chat_interface():
    """Demonstrate a chat-like interface."""
    kt = KeyTyper()

    kt.print_banner("CHAT INTERFACE DEMO", char="-", width=60)

    # Simulate a conversation
    messages = [
        ("user", "Hello! Can you help me with KeyTyper?"),
        (
            "ai",
            "Of course! I'd be happy to help you with KeyTyper. What would you like to know?",
        ),
        ("user", "How do I change the typing speed?"),
        (
            "ai",
            "You can change the typing speed by setting the 'speed' parameter. For example: kt.print('text', speed=0.1)",
        ),
        ("user", "That's great! What about colors?"),
        (
            "ai",
            "KeyTyper supports 16 colors plus bright variants. You can use fore_color and back_color parameters.",
        ),
        ("user", "Perfect! Thanks for the help!"),
        ("ai", "You're welcome! Enjoy using KeyTyper! 🚀"),
    ]

    for role, message in messages:
        if role == "user":
            kt.print(
                f"👤 User: {message}", fore_color="bright_white", bold=True, speed=0.04
            )
        else:
            kt.print_ai_response(message)

        time.sleep(0.5)  # Pause between messages
        print()


def color_palette_demo():
    """Demonstrate all available colors."""
    kt = KeyTyper()

    kt.print_banner("COLOR PALETTE", char="🎨", width=50)

    # Regular colors
    kt.print("Regular Colors:", fore_color="white", bold=True, underline=True)
    regular_colors = [
        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white",
    ]

    for color in regular_colors:
        kt.print_instant(f"  {color.capitalize():<10}", fore_color=color, end="")
        kt.print_instant(f" Background", fore_color="white", back_color=color)

    print()

    # Bright colors
    kt.print("Bright Colors:", fore_color="white", bold=True, underline=True)
    bright_colors = [
        "bright_black",
        "bright_red",
        "bright_green",
        "bright_yellow",
        "bright_blue",
        "bright_magenta",
        "bright_cyan",
        "bright_white",
    ]

    for color in bright_colors:
        display_name = color.replace("bright_", "").capitalize()
        kt.print_instant(f"  Bright {display_name:<10}", fore_color=color, end="")
        kt.print_instant(f" Background", fore_color="black", back_color=color)

    print()


def style_combinations_demo():
    """Demonstrate different style combinations."""
    kt = KeyTyper()

    kt.print_banner("STYLE COMBINATIONS", char="✨", width=50)

    combinations = [
        {"text": "Bold Red", "fore_color": "red", "bold": True},
        {"text": "Italic Blue", "fore_color": "blue", "italics": True},
        {"text": "Underlined Green", "fore_color": "green", "underline": True},
        {
            "text": "Bold + Italic",
            "fore_color": "magenta",
            "bold": True,
            "italics": True,
        },
        {
            "text": "Bold + Underline",
            "fore_color": "cyan",
            "bold": True,
            "underline": True,
        },
        {
            "text": "All Styles",
            "fore_color": "bright_yellow",
            "bold": True,
            "italics": True,
            "underline": True,
        },
        {
            "text": "Colorful Background",
            "fore_color": "bright_white",
            "back_color": "blue",
            "bold": True,
        },
    ]

    for combo in combinations:
        kt.print(
            f"  {combo['text']}", **{k: v for k, v in combo.items() if k != "text"}
        )

    print()


def interactive_customization():
    """Let user customize their own message."""
    kt = KeyTyper()

    kt.print_banner("INTERACTIVE CUSTOMIZATION", char="🛠️", width=50)

    # Get user preferences
    message = kt.print_user_prompt("📝 Enter your message: ")

    kt.print("Available colors:", fore_color="bright_white", bold=True)
    colors = list(kt.fg_colors.keys())
    for i, color in enumerate(colors[:8]):  # Show first 8 colors
        kt.print_instant(f"  {i+1}. {color}", fore_color=color)

    color_choice = kt.print_user_prompt("🎨 Choose a color (1-8): ")
    try:
        selected_color = colors[int(color_choice) - 1]
    except (ValueError, IndexError):
        selected_color = "white"
        kt.print_warning("Invalid choice, using white")

    # Style options
    bold_choice = (
        kt.print_user_prompt("💪 Make it bold? (y/n): ").lower().startswith("y")
    )
    underline_choice = (
        kt.print_user_prompt("📏 Add underline? (y/n): ").lower().startswith("y")
    )

    speed_choice = kt.print_user_prompt("⚡ Typing speed (0.01-0.2, default 0.05): ")
    try:
        speed = float(speed_choice)
        speed = max(0.01, min(0.2, speed))  # Clamp between 0.01 and 0.2
    except ValueError:
        speed = 0.05
        kt.print_warning("Invalid speed, using default (0.05)")

    print()
    kt.print("Here's your customized message:", fore_color="bright_cyan", bold=True)
    kt.print(
        message,
        fore_color=selected_color,
        bold=bold_choice,
        underline=underline_choice,
        speed=speed,
    )


def main():
    """Run all advanced demonstrations."""
    kt = KeyTyper()

    kt.clear_screen()
    kt.print_banner("KEYTYPER ADVANCED DEMO", char="🚀", width=60)

    demos = [
        ("Loading Simulation", simulate_loading),
        ("Chat Interface", demonstrate_chat_interface),
        ("Color Palette", color_palette_demo),
        ("Style Combinations", style_combinations_demo),
        ("Interactive Customization", interactive_customization),
    ]

    for i, (name, demo_func) in enumerate(demos, 1):
        kt.print(
            f"\n{i}. {name}", fore_color="bright_yellow", bold=True, underline=True
        )
        input("Press Enter to continue...")
        print()

        demo_func()

        if i < len(demos):
            input("\nPress Enter for next demo...")
            kt.clear_screen()

    kt.print_banner("DEMO COMPLETE", char="🎉", width=60)
    kt.print(
        "Thanks for exploring KeyTyper's advanced features! 🌟",
        fore_color="bright_green",
        bold=True,
    )


if __name__ == "__main__":
    main()
