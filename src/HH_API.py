import json

import requests


class HeadHunterAPI:

    def __init__(self, search_params,employer_id):
        self.search_params = search_params
        self.employer_id = employer_id

    def get_vacancies(self):

        vac_resp = requests.get('https://api.hh.ru/vacancies', self.search_params)  # получаем список вакансий по параметрам
        return json.loads(vac_resp.content.decode())

    def get_employers(self):

        employer_resp = requests.get(f'https://api.hh.ru/employers/{self.employer_id}', self.search_params)
        return json.loads(employer_resp.content.decode())


employer_id = '68587'
search_params = {
            'area': 113,  # Поиск в России
            'per_page': 100,  # Кол-во вакансий на 1 странице
            'employer_id': '68587'
        }



hh_api = HeadHunterAPI(search_params, employer_id)


content = hh_api.get_vacancies()
# item_content = content['items']
#
# # for i in item_content:
# #     print(i)
#
# print(content)

emp = hh_api.get_employers()

print(emp)

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