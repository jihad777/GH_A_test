def reduced_price(amount, reduction):
    final_price = amount - amount*reduction
    assert reduction > 0
    assert reduction <= 1
    return final_price