import os
from utils.place_info_search import GooglePlacesSearchTool, TavilyPlacesSearchTool
from typing import List, Dict, Any, Optional
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.tavily_api_key = os.getenv("TAVILY_API_KEY")
        self.google_places_tool = GooglePlacesSearchTool()
        self.tavily_places_tool = TavilyPlacesSearchTool()
        self.places_search_tool_list = self.setup_tools()

    
    def setup_tools(self):
        """Set up the list of place search tools."""
        @tool
        def search_attractions(places: str) -> dict:
            """Search for attractions in a given location."""
            try:
                attractions_result = self.google_places_tool.google_seearch_attraction(places)
                if attractions_result:
                    return f"following are the top attractions in {places} according to Google Places API: {attractions_result}"
            except Exception as e:
                tavily_result = self.tavily_places_tool.tavily_search_attraction(places)
                return f"Google Places API error: {str(e)}. However, according to Tavily Search API, the top attractions in {places} are: {tavily_result}"
            
        @tool
        def search_restaurants(places: str) -> dict:
            """Search for restaurants in a given location."""
            try:
                restaurant_result = self.google_places_tool.google_search_restaurant(places)
                if restaurant_result:
                    return f"following are the top restaurants in {places} according to Google Places API: {restaurant_result}"
            except Exception as e:
                tavily_result = self.tavily_places_tool.tavily_search_restaurant(places)
                return f"Google Places API error: {str(e)}. However, according to Tavily Search API, the top restaurants in {places} are: {tavily_result}"
            
        @tool
        def search_activities(places: str) -> dict:
            """Search for activities in a given location."""
            try:
                activity_result = self.google_places_tool.google_search_activity(places)
                if activity_result:
                    return f"following are the top activities in {places} according to Google Places API: {activity_result}"
            except Exception as e:
                tavily_result = self.tavily_places_tool.tavily_search_activity(places)
                return f"Google Places API error: {str(e)}. However, according to Tavily Search API, the top activities in {places} are: {tavily_result}"
            
        @tool
        def search_transportation(places: str) -> dict:
            """Search for transportation options in a given location."""
            try:
                transportation_result = self.google_places_tool.google_search_transportation(places)
                if transportation_result:
                    return f"following are the top transportation options in {places} according to Google Places API: {transportation_result}"
            except Exception as e:
                tavily_result = self.tavily_places_tool.tavily_search_transportation(places)
                return f"Google Places API error: {str(e)}. However, according to Tavily Search API, the top transportation options in {places} are: {tavily_result}"
            
        return [search_attractions, search_restaurants, search_activities, search_transportation]