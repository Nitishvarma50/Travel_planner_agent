import os
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from langchain.tools import tool

from utils.weather_info import WeatherForecastTool

class WeatherInfoTool:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENWEATHERMAP_API_KEY") or os.getenv("OPENWEATHER_API_KEY")
        if not api_key:
            raise ValueError("OPENWEATHERMAP_API_KEY not found in environment variables.")
        
        self.weather_service = WeatherForecastTool(api_key)
        self.weather_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        # Initialize any necessary resources or configurations for the tool
        # Set up the tools that will be used to fetch weather information
        @tool
        def get_current_weather(location: str) -> Dict[str, Any]:
            """Fetch the current weather for a given location."""
            weather_data = self.weather_service.get_current_weather(location)
            if weather_data:
                temp = weather_data.get("main", {}).get("temp","N/A")
                desc = weather_data.get("weather", [{}])[0].get("description", "N/A")
                return {"temperature": temp, "description": desc}
            return {"error": "Could not fetch weather data."}
        @tool
        def get_forecast(location: str) -> Dict[str, Any]:
            """Fetch the weather forecast for a given location."""
            forecast_data = self.weather_service.get_forecast(location)
            if forecast_data and "list" in forecast_data:
                forecasts = []
                for item in forecast_data["list"]:
                    item_list = item.get("list", [])
                    date = item.get("dt_txt", "N/A")
                    temp = item.get("main", {}).get("temp","N/A")
                    desc = item.get("weather", [{}])[0].get("description", "N/A")
                    forecasts.append({"temperature": temp, "description": desc})
                return {"forecasts": forecasts}
            return {"error": "Could not fetch forecast data."}
        return [get_current_weather, get_forecast]
    
