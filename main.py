import requests
import itertools
import time
import random

# Set headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Function to check if a username is available on GitHub
def check_username_availability(username):
    url = f"https://github.com/{username}"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            return True  # Username is available
        elif response.status_code == 200:
            return False  # Username is already taken
        else:
            return None  # Unknown status
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {username}: {e}")
        return None

# Generate 4-letter combinations with at least 3 repeated letters
letters = 'abcdefghijklmnopqrstuvwxyz'
combinations = []

# Generate 4-letter combinations where one letter repeats 3 times and the other letter is different
for letter in letters:
    for other_letter in letters:
        if letter != other_letter:  # Ensure the two letters are different
            combinations.append(f"{letter}{letter}{letter}{other_letter}")
            combinations.append(f"{letter}{letter}{other_letter}{letter}")
            combinations.append(f"{letter}{other_letter}{letter}{letter}")
            combinations.append(f"{other_letter}{letter}{letter}{letter}")

print(f"Generated {len(combinations)} combinations.")

# Randomly shuffle the combinations to check random usernames
random.shuffle(combinations)

# Check availability for the first 1000 random usernames
available_usernames = []
total = len(combinations)
for idx, username in enumerate(combinations[:1000]):  # Limit to the first 1000 combinations
    if check_username_availability(username):
        print(f"[AVAILABLE] {username}")
        available_usernames.append(username)
    else:
        print(f"[TAKEN] {username}")

    # Print progress
    print(f"Processed {idx + 1}/1000 usernames.")

    time.sleep(1)  # Sleep for 1 second

# Optional: Save available usernames to a file
with open("available_usernames.txt", "w") as f:
    for name in available_usernames:
        f.write(name + "\n")

print(f"Done. Available usernames saved to 'available_usernames.txt'.")
