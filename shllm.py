#!/usr/bin/env python3

import sys
import os
import pyperclip
from openai import OpenAI

def main():
    if os.getenv('OPENAI_API_KEY') is None:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        sys.exit(1)

    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    prompt = ' '.join(sys.argv[1:])
    role = 'You are Ubuntu linux shell helper. Given a question, answer with just a shell command, nothing else. Do not wrap it in markdown.'

    try:
        model = os.getenv('OPENAI_MODEL', 'gpt-4o')

        chat_completion = client.chat.completions.create(
            messages=[{"role": "system", "content": role},
                      {"role": "user", "content": prompt}],
            model=model
        )

        result_prompt = chat_completion.choices[0].message.content
        print("Command to be copied to clipboard: " + result_prompt)
        confirm = input("Do you want to copy this command to the clipboard? (y/n): ")
        if confirm.lower() == 'y':
            pyperclip.copy(result_prompt)
            print("Command has been copied to the clipboard.")
        else:
            print("Operation cancelled by user.")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()