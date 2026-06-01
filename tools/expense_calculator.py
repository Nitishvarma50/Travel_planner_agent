from utils.expense_calculator import Calculator
from typing import List, Dict, Any, Optional
from langchain.tools import tool


class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tooL_list = self.setup_tools()

    def setup_tools(self) -> List:
        """Set up the tools for the calculator."""
        @tool
        def estimate_total_hotel_cost(
            hotel_cost_per_night: str, total_days: float
        ) -> float:
            """Estimate the total hotel cost."""
            return self.calculator.multiply(float(hotel_cost_per_night), total_days)
        
        @tool
        def calculate_total_expense(
            *costs: float) -> float:
            """Calculate the total expense."""
            total = 0
            return self.calculator.calculate_total_expense(*costs)
        
        @tool
        def calculate_daily_budget(
            total_expense: float, total_days: int
        ) -> float:
            """Calculate the daily budget."""
            return self.calculator.calculate_daily_budget(total_expense, total_days)
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_budget]