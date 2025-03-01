#!/usr/bin/env python3
"""
Task 2: Consuming and processing data from an API using Python
 (JSONPlaceholder)
"""

import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints the status code
    plus the title of each post.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Parse JSON response
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")

def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file
    with columns (id, title, body).
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", "w", newline="", encoding="utf-8") as csv_file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })
        print("Posts saved to posts.csv")
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")

if __name__ == "__main__":
    # If you run this file directly, it will demonstrate the functionality.
    fetch_and_print_posts()
    fetch_and_save_posts()