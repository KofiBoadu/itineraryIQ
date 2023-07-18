from flask import Flask, render_template, request, send_from_directory,redirect, url_for,abort
from models.itineraryAI import itineraryAI, generate_prompt, extract_itinerary_details
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
import os 
from reportlab.lib.units import inch
import re


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/PDF/'

@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        destination = request.form["destination"]
        number_OfStayDays = int(request.form["days"])
        travelers_budget = int(request.form["budget"])
        travelers_interest = request.form.getlist("interests")

        prompts = generate_prompt(number_OfStayDays, travelers_interest, destination, travelers_budget)
        final_itinerary = itineraryAI(prompts)
        
        filename = f"{destination}_itinerary.pdf"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        doc = SimpleDocTemplate(filepath, pagesize=letter)
        styles = getSampleStyleSheet()
        Story = [Spacer(1, 1)]
        
        extracted_itinerary = re.split(r'(Day \d+:)', final_itinerary)

        for i in range(1, len(extracted_itinerary), 2):
            para = Paragraph("<b>"+extracted_itinerary[i]+"</b>", styles["Heading2"])
            Story.append(para)
            Story.append(Spacer(1, 0.2*inch))
            para = Paragraph(extracted_itinerary[i+1], styles["BodyText"])
            Story.append(para)
            Story.append(Spacer(1, 0.5*inch))

        doc.build(Story)

        return render_template("index.html", filename=filename)

    return render_template("index.html", filename=None)






@app.route("/download/<path:filename>")
def download_pdf(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    
    except FileNotFoundError:
        abort(404)

        





if __name__ == '__main__':
    app.run(debug=True)



