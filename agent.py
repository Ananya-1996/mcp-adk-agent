import google.generativeai as genai
import os
from tools import get_weather

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    tools=[get_weather]
)

def run_agent(city: str):
    prompt = f"""
    You are an intelligent assistant.

    Use the get_weather tool.
    Then suggest if meeting should be online or offline.

    City: {city}
    """

    response = model.generate_content(
        prompt,
        tool_config={"function_calling_config": "AUTO"}
    )

    return {"response": response.text}
