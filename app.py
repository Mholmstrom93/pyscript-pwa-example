# Standard library imports
from pathlib import Path
# Third party imports 
import flask
# Local imports 
from static.python.backend.weather_backend_api import WeatherBackendAPI

app = flask.Flask(__name__)
ws_backend = WeatherBackendAPI.setup()


@app.get('/')
def index():
    return flask.render_template('index.html')


@app.get('/weather/data')
def weather_data():
    data = ws_backend.get_forecast_data()
    return flask.jsonify(data)


@app.get('/weather/data/<forecast_day>')
def weather_data_weekday(forecast_day):
    data = ws_backend.get_forecast_data(int(forecast_day))
    return flask.jsonify(data)


@app.get(f'/weather/data/lat/<lat>/lon/<lon>')
def update_geolocation(lat, lon):
    ws_backend.provider.update_geolocation(lat, lon)
    print(ws_backend.provider)
    return flask.Response(status=200)


@app.get('/serviceWorker.js')
def worker():
    app.logger.info('serviceWorker.js just started!')
    js = Path(__file__).parent / 'static' / 'js' / 'serviceWorker.js'
    text = js.read_text()
    resp = flask.make_response(text)
    resp.content_type = 'application/javascript'
    resp.headers['Service-Worker-Allowed'] = '/'

    return resp

