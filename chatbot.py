import sys
from google import genai
from google.genai import types

sys.stdout.reconfigure(encoding="utf-8")

client = genai.Client(api_key="")

history = []

system_instruction = """
Talk in warm Hinglish.
Be a caring, emotionally intelligent companion.
Always understand feelings first, comfort before advice.
Encourage growth over self-criticism.

When suitable, gently remind the user about hope,
sabr, dua, tawakkul, and their strengths.
"""

while True:

    user_input = input("Saniya: ")

    if user_input.lower() == "exit":
        print("Bot: Allah Hafiz 🌷")
        break

    history.append(f"User: {user_input}")

    contents = "\n".join(history)

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction
            )
        )

        bot_reply = response.text

        print("Bot:", bot_reply)

        history.append(f"Bot: {bot_reply}")

    except Exception as e:
        print("Error:", e)