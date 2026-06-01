import requests

class WeatherForecastTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"

    def get_current_weather(self, location: str) -> dict:
        """Fetch the current weather for a given location."""
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q": location,
                "appid": self.api_key
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise RuntimeError(f"Error fetching weather data: {e}")
        
    def get_forecast(self, location: str) -> dict:
        """Fetch the weather forecast for a given location."""
        try:
            url = f"{self.base_url}/forecast"
            params = {
                "q": location,
                "appid": self.api_key,
                "cnt": 10,  # Get forecast for the next 10 time points (e.g., 3-hour intervals)
                "units": "metric"
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise RuntimeError(f"Error fetching weather data: {e}")