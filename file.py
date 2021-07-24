from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def helloworld():
	return render_template('index.html')
@app.route("/<string:page>")
def home(page):
	return render_template(page)
def database(data):
	email=data["Email"]
	subject=data["Subject"]
	message=data["Message"]
	with open("database.csv", newline="", mode="a")as myfile:
		datacsv=csv.writer(myfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		datacsv.writerow([email,subject,message])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		data = request.form.to_dict()
		database(data)
		return redirect("./thankyou.html")
	else:
		return "something went wrong"