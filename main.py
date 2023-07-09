from flask import Flask, render_template,request
from models.itineraryAI import itineraryAI

app=Flask(__name__)


prompt= "create a 10 days itinerary for Ghana .with a budget of 30000, my interest is culture and safari "

@app.route("/",methods=["GET"])
def home_page():
    if request.method=="GET":
        return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True) 
    

