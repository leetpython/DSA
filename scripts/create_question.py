import os
from typing import List
import json

README_TEMPLATE = """# Question Name

## Intuition

- Assume the reader has already read the question description and knows how to solve questions on this platform.
- Give a ***very*** brief introduction to how the problem can be solved.
- Don't put anything condescending like "Classic DP".
- Be concise. If someone has forgotten how to solve the question, they should be able to recall the approach after reading this.

## Approach

- Use ordered & unordered lists, code blocks and any other markdown features liberally.
- Math is great! Break down mathematical formulas into easily understandable chunks that can be referenced later.
- Try to include a dry run / visualization of an example.
- Do not link to external images or videos, put them in an `assets/` directory within the question if needed.
- Bonus: Try to include examples of approaches that _seem_ intuitively correct but are actually _incorrect_.

## Complexity

- Just a couple of bullet points stating the time and space complexity.
"""


def create_question(
    platform_name: str,
    question_dir_name: str,
    name: str,
    id: str,
    url: str,
    difficulty: str,
    tags: List[str],
    keywords: List[str],
):
    dir_name = f"solutions/{platform_name}/{question_dir_name}"

    # Create directory
    os.makedirs(dir_name, exist_ok=True)

    # __init__.py
    with open(f"{dir_name}/__init__.py", "w") as f:
        f.write("")
    # README.md
    with open(f"{dir_name}/README.md", "w") as f:
        f.write(README_TEMPLATE)
    # metadata.json
    with open(f"{dir_name}/metadata.json", "w") as f:
        json.dump(
            {
                "name": name,
                "id": id,
                "url": url,
                "difficulty": difficulty,
                "tags": tags,
                "keywords": keywords,
            },
            f,
            indent=4,
        )


if __name__ == "__main__":
    create_question("leetcode", "something", "something", "", "", "", [], [])
