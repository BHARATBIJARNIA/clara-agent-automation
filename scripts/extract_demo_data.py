import os
import json
import uuid
INPUT_DIR = "dataset/demo_calls"
OUTPUT_DIR = "outputs/accounts"

def process_files():

    for file in os.listdir(INPUT_DIR):

        if not file.endswith(".txt"):
            continue

        path = os.path.join(INPUT_DIR, file)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        account_id = str(uuid.uuid4())[:8]

        memo = {
            "account_id": account_id,
            "company_name": "",
            "business_hours": "",
            "office_address": "",
            "services_supported": [],
            "emergency_definition": [],
            "emergency_routing_rules": "",
            "non_emergency_routing_rules": "",
            "call_transfer_rules": "",
            "integration_constraints": "",
            "after_hours_flow_summary": "",
            "office_hours_flow_summary": "",
            "questions_or_unknowns": [
                "Company name not identified",
                "Business hours missing",
                "Emergency definitions missing"
            ],
            "notes": "Generated from demo call transcript"
        }

        account_folder = f"{OUTPUT_DIR}/{account_id}/v1"
        os.makedirs(account_folder, exist_ok=True)

        with open(f"{account_folder}/memo.json", "w") as f:
            json.dump(memo, f, indent=4)

        print("Created account:", account_id)


if __name__ == "__main__":
    process_files()