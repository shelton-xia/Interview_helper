import base64
from openai import OpenAI
from .config import OPENAI_API_KEY

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def query_gpt4(image_path):
    """
    Query GPT-4 API using the screenshot image and get the coding solution.
    """
    client = OpenAI(api_key=OPENAI_API_KEY)
    encoded_string = encode_image_to_base64(image_path)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a software engineer expert with great coding skills in Python."},
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "This is a screenshot of a coding problem. Please provide two solutions:\n"
                            "1. Optimized solution with explanation and time complexity.\n"
                            "2. Solution without external packages.\n"
                            "Explain line by line and provide a test case demonstration."
                        )
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_string}"
                        }
                    }
                ]
            }
        ],
        max_tokens=2000
    )
    return response.choices[0].message.content
