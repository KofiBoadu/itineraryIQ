from flask import Flask, render_template,request
from models.itineraryAI import itineraryAI
from models.prompts import generate_prompt 

app=Flask(__name__)



@app.route("/",methods=["GET","POST"])
def home_page():
    if request.method=="POST":
        destination=request.form["destination"]
        number_OfStayDays=int(request.form["days"])
        travelers_budget= int(request.form["budget"])
        travelers_interest= request.form.getlist("interests")
    
        prompts= generate_prompt(number_OfStayDays,travelers_interest,destination,travelers_budget)
        final_itinerary= itineraryAI(prompts)

       
    return render_template("index.html",final_itinerary=final_itinerary)

   






if __name__=="__main__":
    app.run(debug=True) 
    

