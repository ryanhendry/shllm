# shllm
  
A tool to generate shell commands from ChatGPT and quickly run them on your terminal.

Inspired by this [blog post](https://codeandlife.com/2024/02/10/linux-shell-ai-with-chatgpt/).

## Installation

```bash
pip install openai pyperclip
#Update for your file location and shell config. Restart terminal.
echo 'export PATH=$PATH:/Dev/shllm' >> ~/.zshrc
echo "export OPEN_API_KEY=your_api_key_here" >> ~/.zshrc
```

## Usage
    
```bash
shllm show how many gigabytes of free space I have left on my hard drive
Command to be copied to clipboard: df -h . | awk 'NR==2 {print $4}'
Do you want to copy this command to the clipboard? (y/n): y
Command has been copied to the clipboard.
```