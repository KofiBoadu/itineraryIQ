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



def extract_itinerary_details(itinerary_string):
    days = itinerary_string.split('Day')
    new_FormattedItinerary = []

    for day in days:
        if day.strip():  # avoid empty strings
            day_number, activities = day.split(':', 1)
            day_title = f'Day {day_number.strip()}'
            new_FormattedItinerary.append(f'{day_title}: {activities.strip()}')

    # Convert list of strings to single string
    new_FormattedItinerary = '\n'.join(new_FormattedItinerary)

    # Remove unwanted characters
    new_FormattedItinerary = new_FormattedItinerary.replace('#', '')
    new_FormattedItinerary = new_FormattedItinerary.replace('\\', '')

    return new_FormattedItinerary




def generate_prompt(numberOf_days, listsOf_interests,destination, budget):
    interests= ",".join(listsOf_interests)
    prompt= f"Create an itinerary for {numberOf_days} days.My destination is {destination}. I am on a budget of USD{budget} and my interests are {interests} and can you suggest hotels with names within my budget each day with links attached to view the hotels"
    return prompt


