# filename: chatbot.py

import openai

openai.api_key = 'your-api-key'

def ask_gpt3(question):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=question,
      temperature=0.5,
      max_tokens=100
    )
    return response.choices[0].text.strip()

while True:
    question = input("You: ")
    if question.lower() == "quit":
        break
    answer = ask_gpt3(question)
    print("Bot: ", answer)