
# Clara Agent Automation Pipeline

This project implements a zero-cost automation pipeline that converts demo call transcripts into structured account data and generates a draft configuration for a Clara AI voice agent.

The goal is to simulate how Clara agents can be configured automatically for service companies using information gathered during client conversations.

The system processes two types of inputs:

1. Demo call transcripts
2. Onboarding call updates

The demo call generates an initial agent configuration (v1), and the onboarding call updates that configuration to produce a refined version (v2).

---

## Problem Context

Clara is an AI voice assistant designed to handle inbound calls for service businesses such as:

- Fire protection companies  
- Sprinkler system contractors  
- Electrical service providers  
- HVAC and facility maintenance companies  

These businesses receive different types of calls including:

- Emergency service calls  
- Inspection scheduling requests  
- General service inquiries  
- After-hours support requests  

Each company has its own rules for defining emergencies, routing calls, and handling service requests. The purpose of this project is to automatically convert information from conversations into a structured AI agent configuration.

---

## How the Pipeline Works

The automation pipeline has two main stages.

### 1. Demo Call → Preliminary Agent (v1)

A demo call transcript is placed in:


dataset/demo_calls/


The script extracts relevant business information and generates a structured account memo.

Then an initial AI agent configuration is created.

Output is stored in:


outputs/accounts/<account_id>/v1/


Files generated:


memo.json
agent_spec.json


This represents the **first version of the agent configuration based only on demo call information.**

---

### 2. Onboarding Call → Agent Update (v2)

After the client decides to proceed, the onboarding call provides more precise operational information.

The onboarding script updates the existing configuration and produces a second version.

Output is stored in:


outputs/accounts/<account_id>/v2/


Files generated:


memo.json
changes.json


The `changes.json` file records what was modified between the demo and onboarding stages.

---

## Project Structure


clara-agent-automation
│
├── dataset
│ └── demo_calls
│
├── scripts
│ ├── extract_demo_data.py
│ ├── generate_agent_spec.py
│ └── update_agent_with_onboarding.py
│
├── outputs
│ └── accounts
│
├── workflows
│ └── pipeline_workflow.md
│
└── README.md


---

## Running the Project

Run the scripts in the following order:


python scripts/extract_demo_data.py
python scripts/generate_agent_spec.py
python scripts/update_agent_with_onboarding.py


These scripts will:

1. Extract structured data from the transcript
2. Generate the first agent configuration (v1)
3. Apply onboarding updates and generate version v2

---

## Key Features

- Fully zero-cost implementation
- Converts conversation transcripts into structured configuration data
- Automatically generates AI agent prompts
- Supports versioning between demo and onboarding stages
- Tracks configuration changes
- Simple and reproducible local setup

---

## Notes

This implementation focuses on demonstrating the automation workflow rather than production deployment. In a real system, this pipeline could be extended with:

- automatic speech-to-text transcription  
- database storage  
- direct integration with Retell APIs  
- automated workflow orchestration  

---

## Author

Bharatraj Bijarnia  
Computer Science and Engineering  
VIT Vellore
