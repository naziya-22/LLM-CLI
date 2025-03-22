import click
import ollama
import os
import json
from datetime import datetime
import requests


LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


# Enhanced prompt processing function

def generate_response(prompt):
    try:
        response = ollama.chat(
            model="llama3.2:latest",
            messages=[{"role": "user", "content": prompt}]
        )
        response_content = response['message']['content'].strip() if 'message' in response else "No response generated."
        log_interaction(prompt, response_content)
        return response_content
    except Exception as e:
        return f"An error occurred: {e}"


# Save interactions for analysis

def log_interaction(prompt, response):
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "response": response
    }
    with open(f"{LOG_DIR}/interaction_logs.json", "a") as f:
        f.write(json.dumps(log_data) + "\n")


# Fetch logs from API or file

def fetch_logs(source):
    if source.startswith("http"):
        try:
            response = requests.get(source)
            return response.text if response.status_code == 200 else f"Failed to fetch logs from URL. Status code: {response.status_code}"
        except Exception as e:
            return f"An error occurred while fetching logs: {e}"
    else:
        if os.path.exists(source):
            with open(source, 'r') as file:
                return file.read()
        else:
            return "File not found."


@click.command()
@click.option('--task', prompt='Enter your task', help='Task you want the LLM to assist you with.')
@click.option('--chain', is_flag=True, help='Enable command chaining.')
@click.option('--fetch', help='Fetch logs from URL or file.')
def main(task, chain, fetch):
    """
   CLI - Interact with LLM for assistance.
    """
    if fetch:
        logs = fetch_logs(fetch)
        click.echo(f"Logs fetched:\n{logs}")
        return

    click.echo("Processing your request...")

    if chain:
        tasks = task.split("&&")  # Allow command chaining using '&&'
        responses = []
        for t in tasks:
            if "error:" in t.lower():
                t = f"Explain and suggest a solution for the error: {t.strip()}"
            response = generate_response(t.strip())
            responses.append(response)
        click.echo("\n".join(responses))
    else:
        if "error:" in task.lower():
            task = f"Explain and suggest a solution for the error: {task}"
        response = generate_response(task)
        click.echo(response)


if __name__ == "__main__":
    main()