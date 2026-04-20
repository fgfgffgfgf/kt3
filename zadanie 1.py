def get_books(path):
    books = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('|')
            if len(parts) != 5:
                continue
            isbn, title, author, qty, price = parts
            try:
                qty = int(qty)
            except ValueError:
                qty = 0
            try:
                price = float(price)
            except ValueError:
                price = 0.0
            books.append([isbn, title, author, qty, price])
    return books 
