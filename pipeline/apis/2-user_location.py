#!/usr/bin/env python3

"""Script that prints the location of a specific user"""


import requests
import sys
import time

def get_user_location(api_url):
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
