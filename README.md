# GeminiHacker

GeminiHacker is a Python script designed to harness the power of a generative AI model for security research, bug bounty hunting, and vulnerability scanning. This README.md file provides detailed instructions on how to install, configure, and use the script effectively.

## Installation

1. **Clone the repository:**
   
```
git clone https://github.com/your_username/GeminiHacker.git
```


2. **Navigate to the project directory:**

```
cd GeminiHacker
```

3. **Install dependencies:**

```
pip install -r requirements.txt
```

4. **Obtain and configure API key:**

- Sign up for an API key from GenAI.
- Open `gemini_hacker.py` in a text editor.
- Locate the API key configuration section.
- Replace `'YOUR_API_KEY'` with your actual API key.

## Usage

1. **Run the script:**

```
python3 gemini_hacker.py
```

2. **Interacting with GeminiHacker:**

- Once the script is running, follow the on-screen prompts to interact with GeminiHacker.
- Use commands like `\help`, `\name`, `\version`, `\info`, and `\scanf $FILEPATH` to communicate with the AI model.
- To end the conversation, type `\end`.

## Commands

- `\help`: Display help menu.
- `\name`: Get the name of the AI model.
- `\version`: Get the version of the AI model.
- `\info`: Get information about GeminiHacker.
- `\scanf $FILEPATH`: Scan the specified file for vulnerabilities.

## Contributing

If you'd like to contribute to GeminiHacker, we welcome your input! Here's how you can get involved:

- **Open an issue:** If you encounter a bug or have a feature request, please open an issue on GitHub.

- **Submit a pull request:** If you'd like to contribute code improvements or new features, feel free to submit a pull request.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
