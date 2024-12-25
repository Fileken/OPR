def generate_reference(choice, data):
    if choice == "1":
        return f"{data['author']} {data['title']}. {data['city']}: {data['publisher']}, {data['year']}. {data['pages']} с."
    elif choice == "2":
        return f"{data['author1']}, {data['author2']} {data['title']} / {data['org']}. {data['city']}: {data['publisher']}, {data['year']}. {data['pages']} с."
    elif choice == "3":
        return f"{data['author']} {data['title']} // {data['journal']}. {data['year']}. № {data['issue']}. С. {data['pages']}."
    elif choice == "4":
        return f"{data['author']} {data['title']} [Электронный ресурс]. - Режим доступа: {data['url']} (дата обращения: {data['access_date']})."
    else:
        return "Неизвестный тип источника."