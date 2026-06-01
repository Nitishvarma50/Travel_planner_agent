import os
from dotenv import load_dotenv
from utils.currency_convertor import CurrencyConversionTool

class CurrencyConversionTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("EXCHANGE_RATE_API_KEY")
        self.currency_service  = CurrencyConversionTool(api_key=self.api_key)
        self.currency_convertor_tool = self.setup_tools()



    def setup_tools(self) -> list:
        """Set up the tools for currency conversion."""
        @tool
        def convert(from_currency: str, to_currency: str, amount: float) -> float:
            """Convert an amount from one currency to another."""
            return self.currency_service.convert_currency(from_currency, to_currency, amount)
        return [convert] 