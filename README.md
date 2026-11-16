# Practical No. 3: Grocery Billing System

## Title

Develop a C, C++, or Python program to input the names and prices of `n` grocery items, calculate the total bill, and apply a discount. If the total is greater than Rs. 1000, apply a 10% discount; otherwise, no discount is applied. Display the final bill after discount.

## Objectives

1. Understand how arrays or lists store multiple values.
2. Accept user input repeatedly using loops.
3. Calculate the total price of grocery items.
4. Use conditional statements to make decisions.
5. Apply a discount according to a condition.

## Theory

Billing systems calculate the amount a customer needs to pay and apply discounts when applicable. This practical uses lists to store item names and prices, a loop to accept each item's details, and an `if-else` statement to decide whether to apply a discount.

The total is the sum of all item prices. When the total exceeds Rs. 1000, the discount is 10% of the total. The final bill is the total minus the discount.

### Formulae

- **Total bill** = Sum of all item prices
- **Discount** = Total bill × 10 / 100, when total bill > Rs. 1000; otherwise Rs. 0
- **Final bill** = Total bill − Discount

### Input–Process–Output (IPO)

- **Input:** Number of items, item names, and item prices
- **Process:** Add prices, check discount eligibility, and calculate the final bill
- **Output:** Item details, total bill, discount, and final bill

## Algorithm

1. Start.
2. Input the number of grocery items, `n`.
3. Set the total bill to 0.
4. Repeat for each item:
   - Input the item's name and price.
   - Store the name and price.
   - Add the price to the total bill.
5. If the total bill is greater than Rs. 1000, calculate a 10% discount; otherwise, set the discount to 0.
6. Calculate the final bill by subtracting the discount from the total bill.
7. Display each item and its price.
8. Display the total bill, discount, and final bill.
9. Stop.



## Sample Output

```text
Enter number of grocery items: 4

Enter item 1 name: Rice
Enter price: 500

Enter item 2 name: Oil
Enter price: 350

Enter item 3 name: Sugar
Enter price: 250

Enter item 4 name: Tea
Enter price: 150

----- Grocery Bill -----
Rice : Rs 500.0
Oil : Rs 350.0
Sugar : Rs 250.0
Tea : Rs 150.0

Total Bill : Rs 1250.0
Discount   : Rs 125.0
Final Bill : Rs 1125.0
```

## Conclusion

The program accepts the names and prices of multiple grocery items, calculates their total, and applies a 10% discount when the total exceeds Rs. 1000. It demonstrates the use of lists, loops, arithmetic operations, and conditional statements in Python.

