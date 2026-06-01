import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper

load_dotenv()

@tool
def multiply(a: float, b: float) -> float:
    """
    multiply two numbers together.
    Args:
        a (float): The first number to multiply.
        b (float): The second number to multiply.
        Returns:
        float: The product of the two numbers.
    """
    return a * b

@tool
def add(a: float, b: float) -> float:
    """
    add two numbers together.
    Args:
        a (float): The first number to add.
        b (float): The second number to add.
        Returns:
        float: The sum of the two numbers.
    """
    return a + b

@tool
def currency_conversion(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Convert an amount from one currency to another using the Alpha Vantage API.
    Args:
        amount (float): The amount of money to convert.
        from_currency (str): The currency code of the original currency (e.g., "USD").
        to_currency (str): The currency code of the target currency (e.g., "EUR").
    Returns:
        float: The converted amount in the target currency.
    """
    os.environ["ALPHAVANTAGE_API_KEY"] = os.getenv("ALPHAVANTAGE_API_KEY")
    alpha_vantage = AlphaVantageAPIWrapper()
    response = alpha_vantage.get_currency_exchange_rate(from_currency, to_currency)
    exchange_rate = float(response.get("5. Exchange Rate", 0))
    return amount * exchange_rate
