#!/usr/bin/env python3
# count_commit_messages.py
# Reads repo_commit_data.json and counts occurrences of the "commit_message" field.

import json
import sys
from typing import Any

FILENAME = sys.argv[1] if len(sys.argv) > 1 else "repo_commit_data.json"
KEY = "commit_message"

def count_key(obj: Any, key: str) -> int:
    """Recursively count occurrences of `key` in JSON object.
    If key's value is a list, each element in the list counts separately."""
    if isinstance(obj, dict):
        total = 0
        for k, v in obj.items():
            if k == key:
                if isinstance(v, list):
                    total += len(v)
                else:
                    total += 1
            # Always recurse into value to find nested occurrences
            total += count_key(v, key)
        return total
    elif isinstance(obj, list):
        return sum(count_key(item, key) for item in obj)
    else:
        return 0

def main():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {FILENAME}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {FILENAME}: {e}", file=sys.stderr)
        sys.exit(2)

    total = count_key(data, KEY)
    print(total)

if __name__ == "__main__":
    main()