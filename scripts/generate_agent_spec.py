import os
import json

BASE_DIR = "outputs/accounts"


def generate_agent():

    for account in os.listdir(BASE_DIR):

        memo_path = f"{BASE_DIR}/{account}/v1/memo.json"

        with open(memo_path) as f:
            memo = json.load(f)

        company = memo["company_name"] or "Service Company"

        prompt = f"""
You are an AI voice assistant for {company}.

Business Hours Flow:
1. Greet the caller.
2. Ask the reason for the call.
3. Collect caller name and phone number.
4. Transfer call if needed.
5. If transfer fails, log message and inform caller.
6. Ask if they need anything else.
7. Close the call politely.

After Hours Flow:
1. Greet caller.
2. Ask purpose of call.
3. Confirm if emergency.
4. If emergency collect name, phone, and address.
5. Attempt transfer.
6. If transfer fails reassure quick follow-up.
7. If non-emergency collect message.
8. Close the call.
"""

        agent = {
            "agent_name": f"{company} Assistant",
            "voice_style": "professional",
            "system_prompt": prompt,
            "version": "v1"
        }

        with open(f"{BASE_DIR}/{account}/v1/agent_spec.json", "w") as f:
            json.dump(agent, f, indent=4)

        print("Agent generated for:", account)


if __name__ == "__main__":
    generate_agent()