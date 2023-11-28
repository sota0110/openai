from openai import OpenAI
from config.openai_key import free_secret_key

def main():
    client = OpenAI(api_key = free_secret_key)
    messages = []

    while True:
        user_input = input("\n[Input](or 'exit'): ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        bot_response = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": bot_response})

        print(bot_response)

if __name__ == '__main__':
    main()