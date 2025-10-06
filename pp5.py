# Program to enter initial balance, deposit amount, and withdraw amount

initial_balance = float(input("Enter initial balance: "))
deposit_amount = float(input("Enter deposit amount: "))

final_balance = initial_balance + deposit_amount
print(f"Balance after deposit: {final_balance:.2f}")

withdraw_amount = float(input("Enter withdraw amount: "))
final_balance -= withdraw_amount

print(f"Final balance after withdrawal: {final_balance:.2f}")