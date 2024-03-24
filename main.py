from src.HH_API import HeadHunterAPI, Employer, Vacancy

if __name__ == '__main__':

    employers_id = ['3144945', '9280639', '68587', '1545815', '1729433', '4614421', '3127', '3776', '78638', '47858']
    for employer_id in employers_id:
        hh_api = HeadHunterAPI(employer_id)
        emp = hh_api.get_employers()
        vac = hh_api.get_vacancies()
        employer = Employer(emp['id'], emp['name'], emp['description'], emp['site_url'])
        vacancy_list = []



        print(employer.id, employer.name, employer.description, employer.site_url, sep='\n')

        print(f'длинна {len(vac)}')

        for item in range(len(vac)):
            if vac['items'][item]['salary'] is None:
                vac['items'][item]['salary'] = {'from': None, 'to': None, 'currency': 'не указано', 'gross': True}
            else:
                pass

        for item in range(len(vac)):
            print(item)

            vacancy = Vacancy(
                vac['items'][item]['id'],
                vac['items'][item]['name'],
                vac['items'][item]['area']['name'],
                vac['items'][item]['salary']['from'],
                vac['items'][item]['salary']['to'],
                vac['items'][item]['salary']['currency'],
                vac['items'][item]['type']['name'],  # тип вакансии(открытая/закрытая)(t_name)
                vac['items'][item]['published_at'],
                vac['items'][item]['alternate_url']
            )
            vacancy_list.append(vacancy)
            print(vacancy.id, vacancy.name, vacancy.area, vacancy.s_from, vacancy.s_to, vacancy.s_currency, vacancy.t_name, vacancy.published_at, vacancy.url)

        print(vacancy_list)
