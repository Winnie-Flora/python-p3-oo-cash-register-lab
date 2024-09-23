#!/usr/bin/env python3

# lib/cash_register.py

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0
    
    def add_item(self, title, price, quantity=1):
        # Add the item's price * quantity to the total
        self.total += price * quantity
        # Track the last transaction
        self.last_transaction_amount = price * quantity
        
        # Add the items to the items list (track each item individually)
        for _ in range(quantity):
            self.items.append(title)
    
    def apply_discount(self):
    # Apply discount only if a discount exists
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            # Print the total after applying discount
            message = f"After the discount, the total comes to ${int(self.total)}."
            print(message)
            return message
        else:
            # If no discount is available
            message = "There is no discount to apply."
            print(message)
            return message

    
    def void_last_transaction(self):
        # Subtract the last transaction from the total
        self.total -= self.last_transaction_amount
        # Optionally, you could remove the last items added (depending on how detailed you need the log)
        # No need to update the last transaction after this since we are voiding it

###Sample inputs
register = CashRegister(20)
register.add_item("apple", 1.00, 3)  # Adds 3 apples for a total of $3.00
print(register.total)  # Should print 3.00
register.apply_discount()  # Applies 20% discount and updates total
register.add_item("banana", 2.00, 2)  # Adds 2 bananas for a total of $4.00
print(register.total)  # Should print total after adding bananas
register.void_last_transaction()  # Removes the last added bananas
print(register.total)  # Total after voiding should reflect removal of bananas



