#write functions here, don't add input('') statements here!

def test_config():
    return True

def get_bonus_pay_amount(sales):
    if 0 < sales <= 499:
        bonus = sales * 0.05
        return bonus
    elif 499 < sales <= 900:
        bonus = sales * 0.06
        return bonus
    elif 900 < sales <= 1499:
        bonus = sales * 0.07
        return bonus
    elif 1499 < sales <= 1999:
        bonus = sales * 0.08
        return bonus
    else:
        raise ValueError("Invalid arguments")