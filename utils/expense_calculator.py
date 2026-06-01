


class Calculator:
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """
        Multiply two numbers together.
        Args:
            a (float): The first number to multiply.
            b (float): The second number to multiply.
            Returns:
            float: The product of the two numbers.
        """
        return a * b
    
    @staticmethod
    def calculate_total_expense(expenses: list) -> float:
        """
        Calculate the total expense from a list of expenses.
        Args:
            expenses (list): A list of individual expenses (float).
            Returns:
            float: The total expense.
        """
        return sum(expenses)
    
    @staticmethod
    def calculate_daily_budget(total_expense: float, days: int) -> float:
        """
        Calculate the daily budget based on total expense and number of days.
        Args:
            total_expense (float): The total expense for the trip.
            days (int): The number of days for the trip.
            Returns:
            float: The daily budget.
        """
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")
        return total_expense / days
    