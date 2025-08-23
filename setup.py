"""
Setup script for KeyTyper package.
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read the requirements
def read_requirements():
    requirements = []
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    return requirements

setup(
    name="keytyper",
    version="0.1.0",
    author="Leonardo Savio Ferreira",
    author_email="leosavio@leosavio.com",
    description="A powerful, cross-platform Python library for creating beautiful terminal output with typing effects, colors, and formatting",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/leosavio/keytyper",
    project_urls={
        "Bug Tracker": "https://github.com/leosavio/keytyper/issues",
        "Documentation": "https://github.com/leosavio/keytyper#readme",
        "Source Code": "https://github.com/leosavio/keytyper",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Shells",
        "Topic :: Terminals",
        "Topic :: Text Processing :: Markup",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Environment :: Console",
        "Natural Language :: English",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
            "twine>=3.0",
            "build>=0.7",
        ],
        "windows": [
            "colorama>=0.4.4",
        ],
    },
    keywords=[
        "terminal", "console", "typing", "animation", "colors", "formatting", 
        "ansi", "cross-platform", "cli", "text", "output", "print", "style"
    ],
    entry_points={
        "console_scripts": [
            # Add console scripts here if needed
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
