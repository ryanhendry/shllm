# shllm
  
Generate shell commands using natural langauge.

## Installation

```bash
echo "export SHLLM_OPENAI_KEY={{OpenAI API Key}}" >> ~/.zshrc
pipx install shllm
```

## Usage
```bash
shllm {{what you want to do}}
```
### Example
```bash
shllm show how many gigabytes of free space I have left on my hard drive
Command to be copied to clipboard: df -h . | awk 'NR==2 {print $4}'
Do you want to copy this command to the clipboard? (y/n): y
Command has been copied to the clipboard.
```