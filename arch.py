programs_list = {
    "1": "filezilla",
    "2": "firefox",
    "3": "chrome",
    "4": "discord",
    "5": "teams",
    "6": "notepad++",
    "7": "paint",
    "8": "vlc",
    "9": "winrar",
    "10": "winzip",
}


def start():
    print(f"Добро пожаловать в быструю установку программ в Arch Linux!\n"
          f"Нажмите: 0 - вывести список программ, 1 - Досуг, 2 - Браузеры, 3 - видео")

    spisok = input("Введите вариант: ")

    if spisok == "0":
        install()
    elif spisok == "1":
        print("Досуг")
    elif spisok == "2":
        print("Браузеры")
    elif spisok == "3":
        print("Видео")


def install():
    print(programs_list)
    print(f'\n\nЕсть несколько выриантов выбора программ..\n'
          f'Выбор тех программ которые будут установлены - 1-3 3-4 6 8 12-15...\n'
          f'Устонавить все кроме - !1-3 !4 !6 !8 !12...\n'
          f'Такой вариант вызывает ошибку - 1 2 !4...')
    progs = input("Выберите программы: ")

    progs = progs.split(" ")
    #has_exclamation = any(p.startswith('!') for p in progs)
    all_exclamation = all(p.startswith('!') for p in progs)
    all_numbers = all(not p.startswith('!') for p in progs)

    if all_numbers:
        proverka = "esti"

    elif all_exclamation:
        proverka = "nety"
    else:
        proverka = "error"

    print(f"Результат проверки: {proverka}")
    sorted_list = vibor_prog(progs)
    print(sorted_list)
    print("a")


def vibor_prog(progs):
    selected_numbers = set()  # Используем множество для уникальных значений

    for prog in progs:
        if '-' in prog:  # Если есть диапазон
            start, end = map(int, prog.split('-'))
            selected_numbers.update(range(start, end + 1))  # Добавляем диапазон
        else:
            selected_numbers.add(int(prog))  # Добавляем отдельное число

    return sorted(selected_numbers)  # Возвращаем отсортированный список


install()
