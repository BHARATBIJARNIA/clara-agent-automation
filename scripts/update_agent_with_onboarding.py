import os
import json

BASE_DIR = "outputs/accounts"
ONBOARDING_DIR = "dataset/onboarding_calls"


def update_accounts():

    for account in os.listdir(BASE_DIR):

        v1_memo = f"{BASE_DIR}/{account}/v1/memo.json"

        if not os.path.exists(v1_memo):
            continue

        with open(v1_memo) as f:
            memo = json.load(f)

        # simulate onboarding updates
        memo["business_hours"] = "Mon-Fri 8:00 AM - 6:00 PM"
        memo["emergency_definition"] = ["Fire alarm triggered", "Sprinkler leak"]

        v2_folder = f"{BASE_DIR}/{account}/v2"
        os.makedirs(v2_folder, exist_ok=True)

        with open(f"{v2_folder}/memo.json", "w") as f:
            json.dump(memo, f, indent=4)

        # create changelog
        change_log = {
            "changes": [
                "Added business hours",
                "Added emergency definitions"
            ],
            "reason": "Information confirmed during onboarding call"
        }

        with open(f"{v2_folder}/changes.json", "w") as f:
            json.dump(change_log, f, indent=4)

        print("Account updated to v2:", account)


if __name__ == "__main__":
    update_accounts()