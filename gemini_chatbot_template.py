# TODO:
# Migrate to google.genai SDK in a future mission.

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

print("🤖 Healthcare AI ready (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("AI: Bye 👋")
        break

    response = model.generate_content(user_input)

    print("AI:", response.text)
    print()