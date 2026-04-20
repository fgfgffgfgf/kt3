def books_value_tuples(filtered):
    """
    filtered: list of [isbn, "title, author", quantity, price]
    returns: list of (isbn, quantity*price)
    """
    result = []
    for item in filtered:
        isbn = item[0]
        qty = item[2]
        price = item[3]
        result.append((isbn, qty * price))
    return result
