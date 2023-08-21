# api key# 1d6de7611f3d44f7bd155411232108

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, url_for, request, jsonify
import requests
apikey = "1d6de7611f3d44f7bd155411232108"

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('home.html')


@app.route('/weather_for_city', methods=['POST'])
def weather_for_city():
	isError=0
	if request.method == 'POST':
		city_name=request.form.get('city')
		  # send a GET request to another site
		response = requests.get("http://api.weatherapi.com/v1/current.json?key="+apikey+"&q="+city_name+"&aqi=yes")
		# get the JSON data from the response
		temp = response
		data=temp.json()
		if list(data.keys())[0]=='error' :
			print("yes")
			isError=1
		print(temp)
		print(temp.json())
		# Error handling
		return render_template('city_data.html',data=data,error=isError)

if __name__ == '__main__':
	app.run(debug=True)

  
