Day 40 – Your First GitHub Actions Workflow Objective

Create and run your first GitHub Actions workflow to understand the basics of CI/CD automation.

Task 1: Repository Setup
Steps Performed
Created a public GitHub repository named github-actions-practice
Cloned the repository locally
git clone https://github.com/<your-username>/github-actions-practice.git
cd github-actions-practice
Created workflow directory
mkdir -p .github/workflows

Task 2: Hello Workflow
Workflow File

File: .github/workflows/hello.yml

name: Hello Workflow

on:
  push:
    branches:
      - main

jobs:
  greet:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Print Message
        run: echo "Hello from GitHub Actions!"
Verification
Pushed workflow to GitHub
Opened the Actions tab
Observed workflow execution
Verified successful completion (green check mark)

Task 3: Understanding Workflow Anatomy
on:

Defines the event that triggers the workflow.

Example:

on:
  push

This workflow runs whenever code is pushed.

jobs:

Contains one or more jobs that GitHub Actions will execute.

jobs:
runs-on:

Specifies the runner environment where the job executes.

runs-on: ubuntu-latest
steps:

A list of actions or commands executed sequentially.

steps:
uses:

Runs a pre-built GitHub Action.

uses: actions/checkout@v4
run:

Executes shell commands on the runner.

run: echo "Hello"
name:

Provides a readable name for a workflow or step.

name: Checkout Code

Task 4: Enhanced Workflow

Updated workflow:

name: Hello Workflow

on:
  push:
    branches:
      - main

jobs:
  greet:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Print Hello Message
        run: echo "Hello from GitHub Actions!"

      - name: Print Date and Time
        run: date

      - name: Print Branch Name
        run: echo "Branch: ${{ github.ref_name }}"

      - name: List Repository Files
        run: ls -la

      - name: Print Runner OS
        run: echo "Operating System: $RUNNER_OS"
Output Observed
Current date and time displayed
Branch name displayed
Repository files listed
Runner OS shown as Linux

Task 5: Break the Pipeline
Added Failing Step
- name: Intentional Failure
  run: exit 1
Observation
Workflow failed
Failed step displayed a red X
Error logs clearly showed the command that caused failure
How to Read Errors
Open Actions tab
Select failed workflow run
Click failed job
Expand failed step
Read error message and exit code
What Does a Failed Pipeline Look Like?
Red X icon
Workflow marked as Failed
Logs highlight the failing step
Exit code indicates failure reason
Fix

Removed the failing command and pushed again.

Result: Workflow passed successfully.

Repository Structure
github-actions-practice/
└── .github/
    └── workflows/
        └── hello.yml

Key Learnings
GitHub Actions automates CI/CD workflows.
Every push can trigger automated jobs.
Workflows are written in YAML.
Jobs run on GitHub-hosted runners.
Logs help troubleshoot failures quickly.
CI/CD pipelines provide immediate feedback on code changes.
