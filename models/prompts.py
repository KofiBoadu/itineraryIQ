

def prompt(numberOf_days, listsOf_interests,destination, budget):
    interests= ",".join(listsOf_interests)
    prompt= f"Create an itinerary for {numberOf_days}.My destination is {destination}. I am on a budget of USD{budget} and my interests are {interests} and can you suggest hotels with names within my budget each day with links attached to view the hotels"
    return prompt
