#!/usr/bin/env python3

import sys
import os
import subprocess
from openai import OpenAI

def copy_to_clipboard(text):
    """
    Copy text to clipboard with fallback mechanisms for different environments
    """
    # Detect platform
    platform = sys.platform
    
    # Try using pyperclip first (works on most desktop environments)
    try:
        import pyperclip
        pyperclip.copy(text)
        return True
    except Exception:
        pass
    
    # Platform-specific fallbacks
    success = False
    try:
        if platform == 'darwin':  # macOS
            subprocess.run(['pbcopy'], input=text.encode('utf-8'), check=True)
            success = True
        elif platform == 'linux':
            # Try xclip (X11)
            try:
                subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode('utf-8'), check=True)
                success = True
            except (subprocess.SubprocessError, FileNotFoundError):
                # Try xsel (alternative X11)
                try:
                    subprocess.run(['xsel', '--clipboard', '--input'], input=text.encode('utf-8'), check=True)
                    success = True
                except (subprocess.SubprocessError, FileNotFoundError):
                    # Try wl-copy (Wayland)
                    try:
                        subprocess.run(['wl-copy'], input=text.encode('utf-8'), check=True)
                        success = True
                    except (subprocess.SubprocessError, FileNotFoundError):
                        pass
        elif platform == 'win32':  # Windows
            subprocess.run(['clip'], input=text.encode('utf-8'), check=True)
            success = True
    except Exception:
        pass
    
    return success

def main():
    if os.getenv('SHLLM_OPENAI_KEY') is None:
        print("Error: SHLLM_OPENAI_KEY environment variable is not set.")
        sys.exit(1)

    client = OpenAI(api_key=os.getenv('SHLLM_OPENAI_KEY'))

    prompt = ' '.join(sys.argv[1:])
    role = 'You are macOS shell helper. Given a question, answer with just a shell command, nothing else. Do not wrap it in markdown.'

    try:
        model = os.getenv('OPENAI_MODEL', 'gpt-4o')

        chat_completion = client.chat.completions.create(
            messages=[{"role": "system", "content": role},
                      {"role": "user", "content": prompt}],
            model=model
        )

        result_prompt = chat_completion.choices[0].message.content
        print("Command: " + result_prompt)
        
        copy_options = ['c', 'copy']
        run_options = ['r', 'run']
        
        while True:
            action = input(f"What would you like to do? [c]opy to clipboard, [r]un the command, [q]uit: ").lower()
            
            if action in copy_options:
                if copy_to_clipboard(result_prompt):
                    print("Command has been copied to the clipboard.")
                else:
                    print("Clipboard not available. Here's the command to copy manually:")
                    print(f"\n{result_prompt}\n")
                break
            elif action in run_options:
                print(f"Running: {result_prompt}")
                try:
                    subprocess.run(result_prompt, shell=True)
                except Exception as e:
                    print(f"Error running command: {str(e)}")
                break
            elif action in ['q', 'quit']:
                break
            else:
                print("Invalid option.")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()