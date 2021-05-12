from logging import error
from os import write
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/index.html")
def home():
    return render_template('index.html')    

@app.route("/about.html")
def about():
    return render_template('about.html')    

@app.route("/works.html")
def works():
    return render_template('works.html')        


@app.route("/contact.html")
def contact():
    return render_template('contact.html')  

@app.route("/components.html")
def component():
    return render_template('components.html')      

# @app.route("/<string:page_name>")
# def html_page(page_name):
#     return render_template('login.html', error=error)   
 
@app.route("/thankyou.html")
def thanks():
    return render_template('thankyou.html')   

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"] 
        message = data["message"]  
        file = database.write(f'\n{email},{subject},{message}')  

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"] 
        message = data["message"]  
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        csv_writer.writerow([email,subject,message])             

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database.'    
    else:
        return 'something went wrong. Try Again!'        


