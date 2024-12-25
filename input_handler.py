def get_source_data(choice):
    if choice == "1":
        print("Введите данные для книги одного автора.")
        return {
            "author": input("Автор (ФИО): ").strip(),
            "title": input("Название: ").strip(),
            "city": input("Город издания: ").strip(),
            "publisher": input("Издательство: ").strip(),
            "year": input("Год издания: ").strip(),
            "pages": input("Количество страниц: ").strip()
        }
    elif choice == "2":
        print("Введите данные для книги двух авторов.")
        return {
            "author1": input("Первый автор (ФИО): ").strip(),
            "author2": input("Второй автор (ФИО): ").strip(),
            "title": input("Название: ").strip(),
            "org": input("Организация: ").strip(),
            "city": input("Город издания: ").strip(),
            "publisher": input("Издательство: ").strip(),
            "year": input("Год издания: ").strip(),
            "pages": input("Количество страниц: ").strip()
        }
    elif choice == "3":
        print("Введите данные для статьи из журнала.")
        return {
            "author": input("Автор (ФИО): ").strip(),
            "title": input("Название статьи: ").strip(),
            "journal": input("Название журнала: ").strip(),
            "year": input("Год издания: ").strip(),
            "issue": input("Номер выпуска: ").strip(),
            "pages": input("Страницы: ").strip()
        }
    elif choice == "4":
        print("Введите данные для электронного ресурса.")
        return {
            "author": input("Автор (ФИО): ").strip(),
            "title": input("Название: ").strip(),
            "url": input("URL: ").strip(),
            "access_date": input("Дата обращения: ").strip()
        }
    else:
        return None