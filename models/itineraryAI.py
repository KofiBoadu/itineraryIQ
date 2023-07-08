from dotenv import load_dotenv
import os 
import openai 

load_dotenv()
api_key= os.getenv("API_KEY")

openai.api_key = api_key


def itineraryAI(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a travel itinerary creator ."},
            {"role": "user", "content": prompt},
        ]
    )
    chatGPT_feedback=response['choices'][0]['message']['content']
    return chatGPT_feedback



