import calculator
import discount
import tax
import invoice

# Input
item = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

# Calculations
subtotal = calculator.calculate_total(price, quantity)
discount_amount = discount.calculate_discount(subtotal)
amount_after_discount = subtotal - discount_amount
tax_amount = tax.calculate_tax(amount_after_discount)
final_amount = amount_after_discount + tax_amount

# Print Invoice
invoice.print_invoice(
    item,
    price,
    quantity,
    subtotal,
    discount_amount,
    tax_amount,
    final_amount
)