#!/usr/bin/env python3
"""
GitHub User Location Scripts

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


def get_user_location(url):
    """Fetch and print GitHub user's location."""
    r = requests.get(url)
    if r.status_code == 404:
        print("Not found")
    elif r.status_code == 403:
        reset = int(r.headers.get("X-RateLimit-Reset", time.time()))
        print("Reset in {} min".format(int((reset - time.time()) / 60)))
    else:
        print(r.json().get("location", "Not found"))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
    else:
        get_user_location(sys.argv[1])
