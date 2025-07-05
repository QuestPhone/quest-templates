import json
import os

def check_templates():
    # Load JSON data from all.json
    with open("all.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Folder where template JSON files should exist
    template_folder = "templates"

    # Track missing files
    missing_ids = []

    # Check each id
    for entry in data:
        file_name = f"{entry['id']}.json"
        file_path = os.path.join(template_folder, file_name)

        if not os.path.isfile(file_path):
            missing_ids.append(entry['id'])

    # Report
    if missing_ids:
        print("Missing template files for the following IDs:")
        for mid in missing_ids:
            print(f"- {mid}")
        return False
    else:
        print("✅ All template files are present.")
        return True

# Run the check
if __name__ == "__main__":
    result = check_templates()
