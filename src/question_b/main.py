#add import

import question_b

def main():
    sales = int(input("Please enter the sales amount: $"))
    result = question_b.get_bonus_pay_amount(sales)
    print(f"The bonus is ${result}")

main()