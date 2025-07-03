#!/usr/bin/env python3
"""
EA Exam Practice Application
A comprehensive Enrolled Agent exam preparation tool with 1000+ practice questions
covering Individual Tax, Business Tax, and Ethics & Procedures.

Features:
- Practice Mode: Unlimited time study with all 1000 questions
- Simulation Exam: Official 3-part exam structure matching real EA exam
- Progress tracking and performance analytics
- Export functionality for flagged questions and incorrect answers
- Official exam structure with Prometric testing details

Author: EA Exam Prep Team
License: MIT
Version: 1.0.0
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def check_requirements():
    """Check if required dependencies are available."""
    required_commands = ['node', 'npm']
    missing = []
    
    for cmd in required_commands:
        try:
            subprocess.run([cmd, '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            missing.append(cmd)
    
    if missing:
        print(f"Missing required dependencies: {', '.join(missing)}")
        print("Please install Node.js and npm to run this application.")
        return False
    return True

def install_dependencies():
    """Install npm dependencies."""
    print("Installing dependencies...")
    try:
        subprocess.run(['npm', 'install'], check=True)
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        return False

def start_application():
    """Start the EA Exam Practice application."""
    print("Starting EA Exam Practice Application...")
    print("This will open the application in your default web browser.")
    print("Press Ctrl+C to stop the application.")
    
    try:
        subprocess.run(['npm', 'run', 'dev'], check=True)
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start application: {e}")

def show_help():
    """Display help information."""
    help_text = """
EA Exam Practice Application

DESCRIPTION:
    A comprehensive study tool for the Enrolled Agent (EA) Special Enrollment Examination.
    Features 1000+ practice questions across three exam parts with official exam simulation.

EXAM STRUCTURE:
    Part 1: Individual Tax (400 questions)
    Part 2: Business Tax (400 questions) 
    Part 3: Ethics & Procedures (200 questions)

FEATURES:
    • Practice Mode: Study all questions with unlimited time
    • Simulation Exam: Official 3-part timed exam experience
    • Progress tracking with detailed analytics
    • Question flagging and review system
    • Export functionality for study materials
    • Official EA exam structure and requirements

USAGE:
    python enrolled_agent_app.py [command]

COMMANDS:
    start       Start the application (default)
    install     Install dependencies only
    help        Show this help message

REQUIREMENTS:
    • Node.js (v18 or higher)
    • npm (Node Package Manager)
    • Modern web browser

STUDY GUIDANCE:
    • Recommended study time: 150-300 hours
    • Complete all three parts within 2-year window
    • 75% passing score required per part
    • Questions cover tax years 2021-2023

For more information, visit the GitHub repository or check the README.md file.
    """
    print(help_text)

def main():
    """Main application entry point."""
    print("EA Exam Practice Application v1.0.0")
    print("=" * 50)
    
    # Parse command line arguments
    command = sys.argv[1] if len(sys.argv) > 1 else 'start'
    
    if command == 'help':
        show_help()
        return
    
    # Check if we're in the right directory
    if not Path('package.json').exists():
        print("Error: package.json not found. Please run this script from the project root directory.")
        return
    
    # Check requirements
    if not check_requirements():
        return
    
    if command == 'install':
        install_dependencies()
        return
    
    if command == 'start':
        # Install dependencies if node_modules doesn't exist
        if not Path('node_modules').exists():
            if not install_dependencies():
                return
        
        start_application()
        return
    
    print(f"Unknown command: {command}")
    print("Use 'python enrolled_agent_app.py help' for usage information.")

if __name__ == "__main__":
    main()