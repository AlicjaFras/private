import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config['OPENAI_API_KEY']

def bold(text):
    blue_start = "\033[1m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end
    
def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end

def red(text):
    blue_start = "\033[31m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end

def main():
    parser = argparse.ArgumentParser(description="Simple Comandline Chatbot with GPT3.5")
    parser.add_argument("--personality", type=str, help="A brief summary of a chatbot personality", default="friendly chatbot")

    args = parser.parse_args()

    initial_prompt = f"You are a chatbot. Your personality is: {args.personality}"
    messages = [{'role': 'system', 'content': initial_prompt}]
    while True:
        try:
            user_input = input(blue('You: '))
            messages.append({'role':'user', 'content': user_input})
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=messages
            )
            messages.append(response.choices[0].message.to_dict())
            print(bold(red("Assistant: ")), response.choices[0].message.content)

        except KeyboardInterrupt:
            print('Exiting...')
            break

if __name__ == "__main__":
    main()