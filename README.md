# Enhanced-LLM-CLI

A feature-rich Python-based CLI tool that enhances interaction with LLMs using `ollama`. This tool is built for error handling, prompt engineering, command chaining, integrated logging, and fetching logs from various sources.

## Features
- **Prompt Engineering Framework:** Improves user queries by preprocessing inputs.
- **Error Message Handling:** Detects error messages and provides helpful suggestions.
- **Command Chaining:** Allows sequential task processing using `&&` (e.g., "task1 && task2").
- **Integrated Logging:** Stores interactions for future analysis.
- **Combining Data Sources:** Fetch logs from files or APIs using `--fetch`.

## Requirements
- Python 3.x
- `ollama`
- `click`
- `requests`

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python cli.py --task "Describe how transformers work"  
python cli.py --task "error: ModuleNotFoundError: No module named 'xyz'"  
python cli.py --task "task1 && task2" --chain
python cli.py --fetch "logs/interaction_logs.json"
python cli.py --fetch "https://example.com/logs"
```

Or, if made executable:
```bash
./cli.py
```

## Logs
All interactions are saved in the `logs/interaction_logs.json` file.

## License
MIT License