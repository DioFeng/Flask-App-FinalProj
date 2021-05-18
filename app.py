from flask import Flask
from flask import request
import pyowm


app = Flask(__name__)

owm = pyowm.OWM('9a856135b892d5d0987604d83c5ae8b6')


@app.route('/')
def main():
    html = '<html><body>'
    html += '<form method="POST" action="form_input">\n'
    html += 'City🌄: <input type="text" name="city" />\n'
    html += '<p>\n'
    html += 'Country🎆: <input type="text" name="country" />\n'
    html += '<p>\n'
    html += '<input type="submit" value="submit" />\n'
    html += '</form>\n'
    html += '</body></html>'
    return html


def getWeather(city, country):
    location = city+','+country
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    return w.get_temperature('fahrenheit')


@app.route('/form_input', methods=['POST'])
def form_input():
    city = request.form['city']
    country = request.form['country']
    temperature = getWeather(city, country)
    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += 'City: '+city+'<br>Country: '+country+'\n'
    html += '<p>Max temp: 🌡️'+str(temperature['temp_max'])+' F🌡️\n'
    html += '<p>Current temp: 🌡️'+str(temperature['temp'])+' F🌡️\n'
    html += '<p>Minimum temp: 🌡️'+str(temperature['temp_min'])+' F🌡️\n'
    html += '</body>\n'
    html += '</html>\n'
    return html


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
