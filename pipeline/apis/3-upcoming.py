#!/usr/bin/env python3

import requests
import datetime
import pytz

def get_upcoming_launch():
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch data")
        return
    
    launches = response.json()
    
    if not launches:
        print("No upcoming launches found")
        return
    
    # Sort by date_unix (ascending)
    launches.sort(key=lambda x: x["date_unix"])
    upcoming_launch = launches[0]
    
    # Get required details
    launch_name = upcoming_launch["name"]
    launch_date = datetime.datetime.fromtimestamp(upcoming_launch["date_unix"], pytz.utc).isoformat()
    rocket_id = upcoming_launch["rocket"]
    launchpad_id = upcoming_launch["launchpad"]
    
    # Fetch rocket name
    rocket_response = requests.get(f"https://api.spacexdata.com/v4/rockets/{rocket_id}")
    rocket_name = rocket_response.json().get("name", "Unknown Rocket") if rocket_response.status_code == 200 else "Unknown Rocket"
    
    # Fetch launchpad details
    launchpad_response = requests.get(f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}")
    if launchpad_response.status_code == 200:
        launchpad_data = launchpad_response.json()
        launchpad_name = launchpad_data.get("name", "Unknown Launchpad")
        launchpad_locality = launchpad_data.get("locality", "Unknown Location")
    else:
        launchpad_name = "Unknown Launchpad"
        launchpad_locality = "Unknown Location"
    
    # Print formatted output
    print(f"{launch_name} ({launch_date}) {rocket_name} - {launchpad_name} ({launchpad_locality})")

if __name__ == "__main__":
    get_upcoming_launch()
