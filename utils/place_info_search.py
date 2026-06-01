import os
import JSON
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper


class GooglePlacesSearchTool:
    def __init__(self):
        self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=os.getenv("GOOGLE_API_KEY"))
        self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)
    
    def google_seearch_attraction(self, places: str) -> dict:
        """Search for attractions in a given location using Google Places API."""
        try:
            results = self.places_tool.run(f"""Search for top attractions places in {places}""")
            return results
        except Exception as e:
            return {"error": str(e)}
        
    def google_search_restaurant(self, places: str) -> dict:
        """Search for restaurants in a given location using Google Places API."""
        try:
            results = self.places_tool.run(f"""Search for top restaurant places in {places}""")
            return results
        except Exception as e:
            return {"error": str(e)}
        
    def google_search_activity(self, places: str) -> dict:
        """Search for activities in a given location using Google Places API."""
        try:
            results = self.places_tool.run(f"""Search for top activity places in {places}""")
            return results
        except Exception as e:
            return {"error": str(e)}
        
    def google_search_transportation(self, places: str) -> dict:
        """Search for transportation options in a given location using Google Places API."""
        try:
            results = self.places_tool.run(f"""Search for top transportation places in {places}""")
            return results
        except Exception as e:
            return {"error": str(e)}
        

class TavilyPlacesSearchTool:
    def __init__(self):
        self.tavily_search = TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))
    
    def tavily_search_attraction(self, places: str) -> dict:
        """Search for attractions in a given location using Tavily Search API."""
        try:
            results = self.tavily_search.run(f"""Search for top attractions places in {places}""")
            return results
        except Exception as e:
            return {"error": str(e)}
        
    def tavily_search_restaurant(self, places: str) -> dict:
        """Search for restaurants in a given location using Tavily Search API."""
        try:
            results = self.tavily_search.run(f"""Search for top restaurant places in {places}""")
            return results
        except Exception as e:
            return {"error": str(e)}
        
    def tavily_search_activity(self, places: str) -> dict:
        """Search for activities in a given location using Tavily Search API."""
        try:
            results = self.tavily_search.run(f"""Search for top activity places in {places}""")
            return results
        except Exception as e:
            return {"error": str(e)}
        
    def tavily_search_transportation(self, places: str) -> dict:
        """Search for transportation options in a given location using Tavily Search API."""
        try:
            results = self.tavily_search.run(f"""Search for top transportation places in {places}""")
            return results
        except Exception as e:
            return {"error": str(e)}