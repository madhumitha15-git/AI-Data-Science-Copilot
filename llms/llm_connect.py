from groq import Groq
import os
from dotenv import load_dotenv

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_insight(data):

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": f"""
Analyze this ML result:

{data}

Give:
1. Model Summary
2. Important Insights
3. Recommendations
"""
            }
        ]

    )

    return response.choices[0].message.content