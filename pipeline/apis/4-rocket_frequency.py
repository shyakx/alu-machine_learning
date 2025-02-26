#!/usr/bin/env python3

import requests
from collections import Counter

def get_launches_per_rocket():
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch data")
        return
    
    launches = response.json()
    rocket_counts = Counter()
    
    for launch in launches:
        rocket_id = launch["rocket"]
        rocket_counts[rocket_id] += 1
    
    # Fetch rocket names
    rockets_url = "https://api.spacexdata.com/v4/rockets"
    rockets_response = requests.get(rockets_url)
    
    if rockets_response.status_code != 200:
        print("Failed to fetch rocket names")
        return
    
    rockets_data = rockets_response.json()
    rocket_names = {rocket["id"]: rocket["name"] for rocket in rockets_data}
    
    # Convert ID counts to name counts
    launch_counts = [(rocket_names[rid], count) for rid, count in rocket_counts.items() if rid in rocket_names]
    
    # Sort by count (desc), then by name (asc)
    launch_counts.sort(key=lambda x: (-x[1], x[0]))
    
    for name, count in launch_counts:
        print(f"{name}: {count}")

if __name__ == "__main__":
    get_launches_per_rocket()