from generator import generate_reference
from input_handler import get_source_data

def main():
    print("Программа для оформления списка литературы по ГОСТ Р 7.0.5-2008")
    while True:
        print("\nВыберите тип источника:")
        print("1. Книга одного автора")
        print("2. Книга двух авторов")
        print("3. Статья из журнала")
        print("4. Электронный ресурс")
        print("5. Выход")
        
        choice = input("Ваш выбор: ").strip()
        
        if choice not in {"1", "2", "3", "4", "5"}:
            print("Некорректный выбор, попробуйте снова.")
            continue
        
        if choice == "5":
            print("Выход из программы.")
            break
        
        source_data = get_source_data(choice)
        if source_data:
            reference = generate_reference(choice, source_data)
            print("\nСформированная ссылка:")
            print(reference)
        else:
            print("Ошибка при вводе данных. Попробуйте снова.")
            
if __name__ == "__main__":
    main()