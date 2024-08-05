from sys import argv
import json
from rich import print as rich_print
from create_question import create_question

if __name__ == "__main__":
    argc = len(argv)

    # (scriptname, question number)
    if argc != 2:
        rich_print("[red]Expected 1 argument: Leetcode question number[/]")
        exit(1)

    question_number = int(argv[1])
    
    with open("environment/per-question-metadata.json", "r") as f:
        data = json.load(f)
    
    for question_info in data:
        if question_info["id"] == question_number:
            print(question_info)
            create_question(
                "leetcode",
                question_info["title_slug"],
                question_info["title"],
                question_info["title_slug"],
                f"https://leetcode.com/problems/{question_info['title_slug']}/",
                question_info["difficulty"].capitalize(),
                question_info["topics"],
                []
            )
            break
