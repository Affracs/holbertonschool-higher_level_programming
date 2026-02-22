#!/usr/bin/python3
"""
Module that fetches and processes posts from JSONPlaceholder API
"""

import requests
import csv


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts and print the status code and titles
    """
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch all posts and save id, title, body to posts.csv
    """
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)