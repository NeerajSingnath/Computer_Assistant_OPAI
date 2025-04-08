from openai import OpenAI

class AIInteraction:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def ask_openai(self, question):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error with OpenAI API: {e}")
            return "Sorry, I couldn't fetch an answer at the moment."