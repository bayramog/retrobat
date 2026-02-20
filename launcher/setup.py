"""
RetroBat Emulator Launcher - macOS Edition
Setup configuration
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text() if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    requirements = [
        line.strip()
        for line in requirements_file.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="retrobat-launcher",
    version="1.0.0-alpha",
    author="RetroBat macOS Team",
    author_email="bayramog@users.noreply.github.com",
    description="Emulator launcher for RetroBat on macOS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bayramog/retrobat",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "retrobat-launcher=launcher.__main__:main",
        ],
    },
)
