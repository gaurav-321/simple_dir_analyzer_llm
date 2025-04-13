# 📌 Simple Directory Analyzer LLM

✨ **Description**  
Simple Directory Analyzer LLM is a Python program that scans a directory for files, analyzes their contents using a local OpenAI language model, and prints results to the console. This tool is particularly useful for detecting suspicious text related to treasure hunts, gifts, secrets, awards, or prizes.

🚀 **Features**
- **Directory Scanning**: Automatically scans all files within a specified directory.
- **Content Analysis**: Utilizes an OpenAI language model to analyze file contents.
- **Suspicious Text Detection**: Identifies and prints suspicious text related to prizes, treasures, gifts, secrets, awards, or prizes.

🛠️ **Installation**
To install the required dependencies, run:
```bash
pip install openai
```

Ensure you have an OpenAI API key. You can obtain one by signing up on [OpenAI's website](https://beta.openai.com/signup/).

📦 **Usage**  
Here’s how to use the program:

### Example 1: Scanning a Directory for Suspicious Text
```python
import os
from main import send_msg_to_gpt

# Replace 'your_directory_path' with your actual directory path
dir_name = 'your_directory_path'

# Walk through the directory and analyze each file
for root, dirs, files in os.walk(dir_name):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            send_msg_to_gpt(content)
```

### Example 2: Analyzing a Single File
```python
from main import send_msg_to_gpt

file_path = 'path/to/your/file.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()
    send_msg_to_gpt(content)
```

🔧 **Configuration**  
- **OpenAI API Key**: Set your OpenAI API key in the environment variable `OPENAI_API_KEY`.

🧪 **Tests**  
To run tests, ensure you have a test directory and files. You can use the following command to run tests:
```bash
python -m unittest discover
```

📁 **Project Structure**
```
simple_dir_analyzer_llm/
├── main.py
└── README.md
```

🙌 **Contributing**  
Contributions are welcome! Please follow these guidelines:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Make your changes and commit them (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

📄 **License**  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance! 😊