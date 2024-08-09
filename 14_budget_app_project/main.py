import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        # Center category title and fill blank spaces with asterisks
        title = f'{self.name.center(30, "*")}\n'
        entries = ''
        for entry in self.ledger:
            # Get description and limit to 23 characters
            description = entry.get('description')[0:23]
            # Get amount and limit to 7 characters
            amount = "{:.2f}".format(entry.get('amount'))[0:7]
            # Create and align complete entry row
            entry = description.ljust(23) + str(amount).rjust(7)
            # Add all individual entries together
            entries += f'{entry}\n'
        # Get total balance and format to 2 decimal places
        total = f'Total: {"{:.2f}".format(self.get_balance())}'
        # Final output
        all_rows = f'{title}{entries}{total}'
        return all_rows

    def deposit(self, amount, description=''):
        # Add deposit to ledger
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        # Approve and process withdrawal if amount is valid
        if self.check_funds(amount):
            self.ledger.append({'amount': -abs(amount), 'description': description})
            return True
        # Reject withdrawal if amount is invalid
        else:
            print("Can't withdraw because amount is larger than balance.")
            return False

    def get_balance(self):
        balance = 0
        # Calculate and return current balance
        for entry in self.ledger:
            amount = entry.get('amount')
            balance += amount
        return balance

    def transfer(self, amount, category):
        # Approve and process transfer if amount is valid
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        # Reject transfer if amount is invalid
        else:
            print("Can't transfer because amount is larger than balance.")
            return False

    def check_funds(self, amount):
        # Approve if amount is smaller or equal to balance
        if self.get_balance() >= amount:
            return True
        # Reject if amount is greater than balance
        else:
            return False


def create_spend_chart(categories):
    total_spent = 0
    spent_per_category = []
    # Calculate total spent and spent per category
    for category in categories:
        category_spent = 0
        for entry in category.ledger:
            # Check only for withdrawals
            if entry.get('amount') < 0:
                category_spent += abs(entry.get('amount'))
                total_spent += abs(entry.get('amount'))
        spent_per_category.append(category_spent)

    # Calculate rounded down percentage spent by category to nearest 10
    percentages_spent = []
    for item in spent_per_category:
        rounded_item = math.floor((item / total_spent) * 10) * 10
        percentages_spent.append(rounded_item)

    # Chart title
    title = 'Percentage spent by category\n'
    # Final y-axis
    y_axis = ''
    for num in range(100, -1, -10):
        # Start of each row and right align
        row = f'{str(num).rjust(3)}| '
        # Add corresponding characters to row
        for percentage in percentages_spent:
            if num > percentage:
                row += '   '
            else:
                row += 'o  '
        # Add row to y-axis
        y_axis += f'{row}\n'
    # Calculate required number of dashes on x-axis
    number_of_dashes = len(percentages_spent) * 3 + 1
    # Final x-axis
    x_axis = f'    {number_of_dashes * "-"}\n'

    # Create list with all category names
    categories_list = []
    for category in categories:
        categories_list.append(category.name)

    # Final labels
    labels = ''
    # Calculate length of longest category name
    max_length = len(max(categories_list, key=len))
    index = 0
    # Keep iterating through category names until last charachter found
    while index < max_length:
        # Start of each new row
        row = f'     '
        for category in categories_list:
            # Continue if label is complete and add correct spacing
            if index >= len(category):
                row += '   '
                continue
            # Add character and correct spacing
            else:
                row += category[index] + '  '
        index += 1
        # Don't add line break if all labels are complete
        if index == max_length:
            row = row
        # Add line break to row if row is complete
        else:
            row += '\n'
        # Add row to labels
        labels += row

    # Final output
    return f'{title}{y_axis}{x_axis}{labels}'


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(200, clothing)
# print(food)

clothing = Category('Clothing')
clothing.deposit(500, 'deposit')
clothing.withdraw(75, 'sweater')
clothing.withdraw(50, 'withdraw')
clothing.transfer(20, food)
clothing.get_balance()

entertainment = Category('Entertainment')
entertainment.deposit(600, 'deposit')
entertainment.withdraw(40, 'movies')
entertainment.withdraw(50, 'laser game')
entertainment.transfer(20, clothing)
entertainment.get_balance()

# print(food)
# print(clothing)
# print(entertainment)

categories = [food, clothing, entertainment]

print(create_spend_chart(categories))