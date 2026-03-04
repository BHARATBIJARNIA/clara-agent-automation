This project builds a simple automation pipeline that converts demo call transcripts into an initial AI voice agent configuration and then updates that configuration after the onboarding call.

The goal is to simulate how Clara agents are configured for different service companies based on information gathered during client conversations.

The pipeline is implemented using Python scripts and local JSON storage so that the solution remains completely zero-cost and easy to reproduce.

Pipeline A – Demo Call to Preliminary Agent

A demo call transcript is placed in the folder:

dataset/demo_calls/

The script extract_demo_data.py reads the transcript and extracts the basic information that can be identified from the conversation.

A structured Account Memo JSON file is generated.
This file stores details such as company name, services, emergency definitions, and other operational information if available.

The script generate_agent_spec.py then creates a Retell Agent Draft Specification based on the extracted data.

The outputs are stored in the following structure:

outputs/accounts/<account_id>/v1/

Files created:

memo.json
agent_spec.json

Version v1 represents the agent configuration based only on demo call information.

Pipeline B – Onboarding Update

After a customer decides to move forward, an onboarding call provides more detailed configuration information.

The onboarding information is processed by the script:

update_agent_with_onboarding.py

The existing account memo is updated with the confirmed operational details.

A new version of the agent configuration is created.

Outputs are saved in:

outputs/accounts/<account_id>/v2/

Files created:

memo.json
changes.json

The changes.json file clearly records what information was updated during onboarding.

Versioning Approach

The project maintains two versions of the configuration:

v1 → Configuration generated from demo call
v2 → Configuration updated after onboarding

This ensures that the original demo assumptions remain preserved while the onboarding information is applied separately.

Handling Missing Information

During demo calls, not all operational details are always available.

To avoid making incorrect assumptions, any missing information is stored under:

questions_or_unknowns

This ensures that the system does not hallucinate or invent configuration details.

Running the Workflow

The pipeline can be executed using the following commands:

python scripts/extract_demo_data.py
python scripts/generate_agent_spec.py
python scripts/update_agent_with_onboarding.py

These scripts process the transcripts and generate the corresponding agent configuration files automatically.

Notes

This implementation focuses on demonstrating a reproducible automation workflow using only free tools. In a production environment, the system could be extended to integrate directly with Retell APIs and real transcription pipelines.