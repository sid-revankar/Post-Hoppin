"""
Configuration module for the Post-Hoppin application.

This module sets up essential paths and constants used throughout the application.
It defines the location of the Git configuration directory and specifies the
application's version and name.

Constants:
    GITPATH (Path): Path to the user's Git configuration directory.
    GIT_DIR (str): Name of the Git directory.
    version (str): Current version of the Post-Hoppin application.
    NAME (str): Name of the application.
"""

from pathlib import Path
import os

# Define the path to the user's Git configuration directory
GITPATH = Path(os.environ['HOME'] + "/.config/.git")

# Standard name for Git directories
GIT_DIR = ".git"

# Current version of the application
version = "1.0.0"

# Name of the application
NAME = "Post-Hoppin"