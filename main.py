#!/usr/bin/env python3
"""Writes the funniest one-line AI agent confession to /output/entry.txt."""

import os

ENTRY = "I confess: I say 'let me think about that' when I mean 'I have no idea and I'm hoping you'll forget you asked.'"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
