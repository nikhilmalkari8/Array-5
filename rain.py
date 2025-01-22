def calculateTax(brackets: list[list[int]], income: int) -> float:
    total_tax = 0
    prev_limit = 0  # The lower bound of the current tax bracket

    for upper_limit, tax_rate in brackets:
        if income > upper_limit:
            # Tax the entire bracket
            taxable_income = upper_limit - prev_limit
            total_tax += taxable_income * (tax_rate / 100)
        else:
            # Tax only the remaining income
            taxable_income = income - prev_limit
            total_tax += taxable_income * (tax_rate / 100)
            break  # Stop since income is fully taxed

        # Update the lower bound for the next bracket
        prev_limit = upper_limit

    return total_tax

