#!/usr/bin/env python

import sys, os
import openai
import pyperclip

openai.api_key = os.getenv('OPENAI_API_KEY')
if openai.api_key is None:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    sys.exit(1)

prompt = ' '.join(sys.argv[1:])
role = 'You are Ubuntu linux shell helper. Given a question, answer with just a shell command, nothing else.'

try:
    model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    
    chat_completion = openai.ChatCompletion.create(
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
    print("An error occurred:", str(e))
