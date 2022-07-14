# Standard libraries
import io
import json
# Local imports 
from weather_report import WeatherReport
# WebAssembly 
import pyodide


def download_report(forecast_day: int) -> WeatherReport:
    if forecast_day == 0:
        resp: io.StringIO = pyodide.open_url('/weather/data')
        forecast = json.loads(resp.read())
    else:
        resp: io.StringIO = pyodide.open_url(f'/weather/data/{forecast_day}')
        forecast = json.loads(resp.read()) 
    return WeatherReport(**forecast)

def update_geolocation(lat: float, lon: float):
    try:
        resp: io.StringIO = pyodide.open_url(f'/weather/data/lat/{lat}/lon/{lon}')
        return True
    # Figure out correct exception and/or read of the error code
    except Exception as e:
        print(e)
        return False