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
                 salary,
                 t_name,
                 published_at,
                 url
                 ):
        self.id = id
        self.name = name
        self.area = area
        self.salary = salary
        self.t_name = t_name
        self.published_at = published_at
        self.url = url
