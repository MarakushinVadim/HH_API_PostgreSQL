import json

import requests


class HeadHunterAPI:

    def __init__(self, employer_id):
        self.employer_id = employer_id

    def get_vacancies(self):
        vac_resp = requests.get(
            f'https://api.hh.ru/vacancies?employer_id={self.employer_id}')  # получаем список вакансий по id
        return json.loads(vac_resp.content.decode())

    def get_employers(self):
        employer_resp = requests.get(f'https://api.hh.ru/employers/{self.employer_id}')
        return json.loads(employer_resp.content.decode())


class Employer:

    def __init__(self, id, name, description, site_url):
        self.id = id
        self.name = name
        self.description = description
        self.site_url = site_url


class Vacancy:

    def __init__(self,
                 id,
                 name,
                 area,
                 s_from,
                 s_to,
                 s_currency,
                 t_name,
                 address,
                 published_at
                 ):
        self.id = id
        self.name = name
        self.area = area
        self.s_from = s_from
        self.s_to = s_to
        self.s_currency = s_currency
        self.t_name = t_name
        self.address = address
        self.published_at = published_at


employer_id = '68587'

hh_api = HeadHunterAPI(employer_id)  # создаем экземпляр класса HeadHunterAPI по id

content = hh_api.get_vacancies()  # наполняем данными с вакансиями по id
# item_content = content['items']
#
# # for i in item_content:
# #     print(i)
#
# print(content['items'][0])\
# print(content['items'][0])

emp = hh_api.get_employers()  # загружаем данные о компании по id
employer = Employer(emp['id'], emp['name'], emp['description'],
                    emp['site_url'])  # создаем обьект класса Employer на основании информации о компании

vacancy = Vacancy(
    content['items'][0]['id'],
    content['items'][0]['name'],
    content['items'][0]['area']['name'],
    content['items'][0]['salary']['from'],
    content['items'][0]['salary']['to'],
    content['items'][0]['salary']['currency'],
    content['items'][0]['type']['name'],  # тип вакансии(открытая/закрытая)(t_name)
    content['items'][0]['address'],
    content['items'][0]['published_at']
)
print(vacancy.id, vacancy.name, vacancy.area, vacancy.s_from, vacancy.s_to, vacancy.s_currency, vacancy.t_name,
      vacancy.address, vacancy.published_at, sep='\n')

# id работодателей:
#
# 3144945 - Ростелеком
# 9280639 - Бизнес цифра
# 68587 - Алабуга
# 1545815 - МедРокет
# 1729433 - ООО Диджитал Сектор Поддержка
# 4614421 - Ред Лаб
# 3127 - Мегафон
# 3776 - МТС
# 78638 - Тинькофф
# 47858 - ЦБ России
