from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class ChatGPTClient:
    """A class to interact with OpenAI's ChatGPT API."""
    
    def __init__(self, model="gpt-4o-mini"):
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY")
    
    def api_call(self, prompt: str):
        try:
            client = OpenAI(api_key=self.api_key)
            response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                    {"role": "developer", "content": "You are a helpful assistant."},
                    {
                        "role": "user",
                        "content": prompt
                    }
            ],
            store=True)
            return response.choices[0].message.content
        except Exception as e:
            return f"Error as {str(e)}"

def chatgpt_command():
    client = ChatGPTClient()
    prompt = input("Enter your prompt for ChatGPT: ").strip()
    response = client.api_call(prompt)
    print("\nChatGPT Response:\n " + response)
    print("\n")