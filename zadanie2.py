def filtered_books(books, term):
    term_lower = term.lower()
    result = []
    for isbn, title, author, qty, price in books:
        if term_lower in title.lower():
            result.append([isbn, f"{title}, {author}", qty, price])
    return result
