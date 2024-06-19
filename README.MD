# Simple File Analyzer

This Python script scans a directory for files and analyzes their contents using a local OpenAI language model.

## Requirements

* **Local LLM:** Make sure you have a language model running on your machine (e.g., using LM Studio).
* **Python:** Install `openai` library (`pip install openai`).

## Usage

1. Run `python main.py`.
2. Enter the directory you want to scan.
3. The script will analyze each file and print results to the console. 

## Customization

Edit `main.py` to:

* Point to your local language model address (usually `http://localhost:5000/v1`).
* Change the model name in the script.
* Adjust the instructions given to the model to fit your analysis needs.
