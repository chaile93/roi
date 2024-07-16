class RentalProperty:
    def __init__(self, income, expenses, down_payment, closing_costs, rehab_budget):
        self.income = income
        self.expenses = expenses
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget

    def calculate_cash_flow(self):
        total_income = sum(self.income.values())
        total_expenses = sum(self.expenses.values())
        cash_flow = total_income - total_expenses
        return cash_flow

    def calculate_roi(self):
        cash_flow = self.calculate_cash_flow()
        cash_on_cash = cash_flow / (self.down_payment + self.closing_costs + self.rehab_budget)
        roi_percentage = cash_on_cash * 100
        return roi_percentage

# Example usage
if __name__ == "__main__":
    # Example income and expenses dictionaries
    income = {
        'rental': 3000,
        'laundry': 100,
        'storage': 50,
        'misc': 50
    }
    
    expenses = {
        'tax': 500,
        'insurance': 100,
        'utilities': 200,
        'hoa': 0,
        'lawn_care': 50,
        'vacancy': 200,
        'property_management': 300,
        'mortgage': 1500
    }

    # Example financial details
    down_payment = 50000
    closing_costs = 10000
    rehab_budget = 2000

    # Create an instance of RentalProperty
    property1 = RentalProperty(income, expenses, down_payment, closing_costs, rehab_budget)

    # Calculate cash flow and ROI
    cash_flow = property1.calculate_cash_flow()
    roi = property1.calculate_roi()

    # Output results
    print(f"Monthly Cash Flow: ${cash_flow}")
    print(f"ROI (Cash on Cash): {roi:.2f}%")
