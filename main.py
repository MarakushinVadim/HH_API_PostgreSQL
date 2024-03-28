from src.DBManager import DBManager
from src.HH_API import HeadHunterAPI, Employer, Vacancy

if __name__ == '__main__':
    # Создаем базу данных и таблицы
    table = DBManager()
    table.create_db()
    table.create_tables()

    progress = 10

    print('Началась обработка данных, дождитесь окончания')
    # Начинаем перебирать список огранизаций и их вакансий
    employers_id = ['3144945', '9280639', '68587', '1545815', '1729433', '4614421', '3127', '3776', '78638', '47858']
    for employer_id in employers_id:
        hh_api = HeadHunterAPI(employer_id)
        emp = hh_api.get_employers()
        vac = hh_api.get_vacancies()
        employer = Employer(emp['id'], emp['name'], emp['description'], emp['site_url'])
        vacancy_list = []

        # Добавляем компанию в таблицу
        table.add_employer(employer)

        for item in vac['items']:

            # Редактируем значение Salary
            if item['salary'] is None:
                item['salary'] = {'from': 0, 'to': 0, 'currency': 'не указано', 'gross': True}

            if item['salary']['to'] is None:
                item['salary']['to'] = 0

            if item['salary']['from'] is None:
                item['salary']['from'] = 0

            if item['salary']['to'] >= item['salary']['from']:
                item['salary'] = item['salary']['to']

            elif item['salary']['to'] < item['salary']['from']:
                item['salary'] = item['salary']['from']

            item['published_at'] = item['published_at'][0:10] + ' ' + item['published_at'][11:19]
            vacancy = Vacancy(
                item['id'],
                item['name'],
                item['area']['name'],
                item['salary'],
                item['type']['name'],  # тип вакансии(открытая/закрытая)(t_name)
                item['published_at'],
                item['alternate_url']
            )

            # Добавляем вакансии в таблицу
            table.add_vacancy(employer, vacancy)

        print(f'{progress}%')
        progress += 10

    print('Данные загружены, спасибо за ожидание!')
    print()

    # Создаем 
    all_vacancy_count = table.get_companies_and_vacancies_count()
    all_vacancy = table.get_all_vacancies()
    avg_salary = table.get_avg_salary()
    higher_salary = table.get_vacancies_with_higher_salary()
    
    # Запускаем цикл
    while True:
        print(f'1. - список всех компаний и количество вакансий у каждой компании ''\n'
              f'2. - список всех вакансий''\n'
              f'3. - средняя зарплата по вакансиям''\n'
              f'4. - список всех вакансий, у которых зарплата выше средней по всем вакансиям''\n'
              f'5. - поиск по ключевому слову''\n'
              f'6. - выход')
        choice = input()
        if choice == '1':
            for vacancy in all_vacancy_count:
                print(f'Компания {vacancy[0]}; кол-во вакансий - {vacancy[1]}')

        elif choice == '2':
            for vacancy in all_vacancy:
                print(vacancy)

        elif choice == '3':
            print(f'Средняя зарплата по вакансиям - {avg_salary[0][0]}')

        elif choice == '4':
            for vacancy in higher_salary:
                print(vacancy)

        elif choice == '5':
            word = input("Введите ключевое слово для поиска ")
            keyword_vacancy = table.get_vacancies_with_keyword(word)
            for vacancy in keyword_vacancy:
                print(vacancy)

        elif choice == '6':
            break
