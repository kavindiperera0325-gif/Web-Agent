
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def get_ai_response(prompt_history):
    """Sends conversation history to Gemini."""

    api_key = os.environ.get("GOOGLE_API_KEY")

    if not api_key:
        return "Error: GOOGLE_API_KEY not found."

    try:
        client = genai.Client(api_key=api_key)

        # Convert chat history into plain text
        conversation = ""

        for message in prompt_history[-6:]:
            if message.type == "human":
                role = "User"
            else:
                role = "Assistant"

            conversation += f"{role}: {message.content}\n"

        response = client.interactions.create(
            model="gemini-3.8-flash",
            input=conversation
        )

        return response.output_text

    except Exception as e:
        return f"Error connecting to Gemini: {e}"

