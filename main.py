from flask import Flask
from models.itineraryAI import itineraryAI

app=Flask(__name__)


prompt= "create a 10 days itinerary for Ghana .with a budget of 30000, my interest is culture and safari "

print(itineraryAI(prompt))