# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-11-27

First release on PyPI.

### Packaging and release
- Python 3.11 to 3.15 (the versions CPython still supports); 3.8 to 3.10 are no longer supported.
- `pyproject.toml` only (`setup.py` removed), SPDX license expression `MIT`.
- Published from GitHub Actions with Trusted Publishing and PEP 740 attestations: tag `vX.Y.Z`
  to PyPI, `vX.Y.Z-rc.N` to TestPyPI. Tests on Linux, macOS and Windows; zizmor, CodeQL,
  Dependabot and secret scanning.

### Added
- Initial release of KeyTyper
- Cross-platform terminal text formatting
- Simulated typing effects with customizable speed
- Rich text formatting (colors, bold, italic, underline)
- Automatic OS detection and optimization
- Support for Windows, macOS, and Linux
- ANSI color support with 16 colors plus bright variants
- Convenience methods for success, error, warning, and info messages
- Banner printing functionality
- Screen clearing capability
- User input prompts with formatting
- Comprehensive OS information detection
- Zero required dependencies (uses only Python standard library)
- Optional colorama support for enhanced Windows compatibility

### Features
- ✨ Simulated typing effect with realistic timing variations
- 🎨 Rich formatting with foreground and background colors
- 🖥️ Cross-platform compatibility (Windows, macOS, Linux)
- 🔍 Automatic OS detection and optimization
- 🌈 Full ANSI color support (16 colors + bright variants)
- 🚀 Easy-to-use API with intuitive methods
- ⚡ High performance with efficient ANSI sequence handling
- 🛡️ Safe implementation without problematic system dependencies
- 📦 Lightweight package with minimal dependencies
- 🎯 Specialized methods for different message types

### Technical Details
- Python 3.11+ support
- Type hints for better IDE support
- Comprehensive error handling
- Automatic terminal capability detection
- Fallback support for terminals without color support
- Memory efficient implementation
- Thread-safe operations
