import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_script(topic):
    prompt = f"""
You are a viral YouTube Shorts writer.

Create a viral 60-second script about this topic: "{topic}".
Use the MrBeast style:
- Start with an insane hook (first 2 seconds)
- Build suspense quickly
- Use simple, intense words
- End with a punchline or crazy fact

Output in this format:
HOOK:
BODY:
ENDING:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=1.1,
        max_tokens=300
    )
    return response.choices[0].message.content
