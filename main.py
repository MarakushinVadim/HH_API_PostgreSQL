from src.DBManager import DBManager
from src.HH_API import HeadHunterAPI, Employer, Vacancy

if __name__ == '__main__':

    table = DBManager()
    table.create_db()
    table.create_tables()


    employers_id = ['3144945', '9280639', '68587', '1545815', '1729433', '4614421', '3127', '3776', '78638', '47858']
    for employer_id in employers_id:
        hh_api = HeadHunterAPI(employer_id)
        emp = hh_api.get_employers()
        vac = hh_api.get_vacancies()
        employer = Employer(emp['id'], emp['name'], emp['description'], emp['site_url'])
        vacancy_list = []

        table.add_employer(employer)


        for item in vac['items']:
            if item['salary'] is None:
                item['salary'] = {'from': None, 'to': None, 'currency': 'не указано', 'gross': True}
            else:
                pass

        for item in vac['items']:
            item['published_at'] = item['published_at'][0:10] + ' ' + item['published_at'][11:19]
            vacancy = Vacancy(
                item['id'],
                item['name'],
                item['area']['name'],
                item['salary']['from'],
                item['salary']['to'],
                item['salary']['currency'],
                item['type']['name'],  # тип вакансии(открытая/закрытая)(t_name)
                item['published_at'],
                item['alternate_url']
            )

            table.add_vacancy(employer, vacancy)
            # vacancy_list.append(vacancy)
            # print(vacancy.id, vacancy.name, vacancy.area, vacancy.s_from, vacancy.s_to, vacancy.s_currency, vacancy.t_name, vacancy.published_at, vacancy.url)


        print(vacancy_list)
