import json

def clean_text(text):
    return text.replace("\\n", "\n").replace("\\t", "\t")

# Load your JSON file
with open("repo_commit_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

output_txt = []

for item in data:
    commit_msg = clean_text(item.get("commit_message", "").strip())
    diff = clean_text(item.get("diff", "").strip())

    block = (
        "COMMIT_MESSAGE:\n"
        f"{commit_msg}\n\n"
        "DIFF:\n"
        f"{diff}\n"
        "----------------------------------------\n\n"
    )

    output_txt.append(block)

# Save as txt
with open("cleaned_dataset.txt", "w", encoding="utf-8") as f:
    f.writelines(output_txt)

print("TXT file created: cleaned_dataset.txt")
