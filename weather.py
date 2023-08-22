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
    isError = "n"
    if request.method == 'POST':
        city_name = request.form.get('city')
        # send a GET request to another site
        response = requests.get(
            "http://api.weatherapi.com/v1/forecast.json?key="+apikey+"&q="+city_name+"&days=4")
        # get the JSON data from the response
        temp = response
        data = temp.json()
        if list(data.keys())[0] == 'error':
            print("yes")
            isError = "y"
        print(temp)
        print(temp.json())
        print(isError)
        # Error handling
        return render_template('city_data.html', data=data, error=isError)


@app.route('/automatic_location', methods=['POST'])
def get_location():
    isError = "n"
    if request.method == 'POST':
        # print(request.remote_addr) #use to get the current ip address on which site is running
        d = request.json
        response = requests.get("http://api.weatherapi.com/v1/forecast.json?key=" +
                                apikey+"&q="+str(d['latitude'])+","+str(d['longitude'])+"&days=4")
        temp = response
        data = temp.json()
        if list(data.keys())[0] == 'error':
            print("yes")
            isError = "y"
        print(temp)
        print(temp.json())
        print(isError)
        return render_template('city_data.html', data=data, error=isError)


if __name__ == '__main__':
    app.run(debug=True)
