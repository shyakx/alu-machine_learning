#!/usr/bin/env python3
"""
GitHub User Location Script

This script fetches and prints the location of a specified GitHub user
using the GitHub API.

Usage:
    ./2-user_location.py <GitHub API URL>

Requirements:
    - Python 3.5
    - requests module

Author: Your Name
"""

import requests
import sys
import time

def get_user_location(api_url):
    """Fetch and print the location of a GitHub user."""
    response = requests.get(api_url)
    
    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_time = int(response.headers.get("X-RateLimit-Reset", time.time()))
        wait_time = int((reset_time - time.time()) / 60)
        print(f"Reset in {wait_time} min")
    else:
        user_data = response.json()
        print(user_data.get("location", "Not found"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
    else:
        get_user_location(sys.argv[1])
