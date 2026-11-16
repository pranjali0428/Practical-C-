n = int(input("Enter number of grocery items: "))
items = []
prices = []
total = 0
for i in range(n):
 name = input(f"\nEnter item {i+1} name: ")
 price = float(input("Enter price: "))
 items.append(name)
 prices.append(price)
 total += price
if total > 1000:
 discount = total * 0.10
else:
 discount = 0
final_bill = total - discount
print("\n----- Grocery Bill -----")
for i in range(n):
 print(items[i], ": Rs", prices[i])
print("\nTotal Bill : Rs", total)
print("Discount : Rs", discount)
print("Final Bill : Rs", final_bill)