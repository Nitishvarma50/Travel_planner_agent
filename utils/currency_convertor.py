import requests

class CurrencyConversionTool:
    def __init__(self,api_key: str):
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

    def convert_currency(self, from_currency: str, to_currency: str, amount: float) -> float:
        """Convert an amount from one currency to another."""
        try:
            url = f"{self.base_url}{from_currency}"
            response = requests.get(url)
            data = response.json()
            if data["result"] == "success":
                exchange_rate = data["conversion_rates"].get(to_currency)
                if exchange_rate:
                    return amount * exchange_rate
                else:
                    raise ValueError(f"Currency code {to_currency} not found.")
            else:
                raise RuntimeError("Failed to fetch exchange rates.")
        except Exception as e:
            raise RuntimeError(f"Error during currency conversion: {e}")
