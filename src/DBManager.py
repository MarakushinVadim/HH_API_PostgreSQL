import psycopg2

class DBManager:


    def create_db(self):
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='Oblivion94$'
        )
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute('DROP DATABASE IF EXISTS hh_api')
        cur.execute('CREATE DATABASE hh_api')

        cur.close()
        conn.close()


    def create_tables(self):
        with psycopg2.connect(
            host='localhost',
            database='hh_api',
            user='postgres',
            password='Oblivion94$'
        ) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:

                cur.execute(f'''CREATE TABLE employer
                        (
                            employer_id int PRIMARY KEY,
                            employer_name varchar UNIQUE,
                            employer_url varchar,
                            employer_description text
                        );
                CREATE TABLE vacancy
                        (
                            vacancy_id int PRIMARY KEY,
                            vacancy_name varchar,
                            employer_name varchar REFERENCES employer(employer_name),
                            area varchar,
                            salary int,
                            vacancy_type varchar,
                            published_at timestamp,
                            url varchar
                        )''')
                cur.close()
        conn.close()


    def add_employer(self, employer):
        with psycopg2.connect(
                host='localhost',
                database='hh_api',
                user='postgres',
                password='Oblivion94$'
        ) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:

                cur.execute('INSERT INTO employer VALUES (%s, %s, %s, %s)', (employer.id, employer.name, employer.site_url, employer.description))

                cur.close()
        conn.close()


    def add_vacancy(self, employer, vacancy):
        with psycopg2.connect(
                host='localhost',
                database='hh_api',
                user='postgres',
                password='Oblivion94$'
        ) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:

                cur.execute('INSERT INTO vacancy VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (vacancy.id,
                                                                                                        vacancy.name,
                                                                                                        employer.name,
                                                                                                        vacancy.area,
                                                                                                        vacancy.salary,
                                                                                                        vacancy.t_name,
                                                                                                        vacancy.published_at,
                                                                                                        vacancy.url
                                                                                                        ))
                cur.close()
        conn.close()


    def get_companies_and_vacancies_count(self):
        with psycopg2.connect(
                host='localhost',
                database='hh_api',
                user='postgres',
                password='Oblivion94$'
        ) as conn:
            with conn.cursor() as cur:

                cur.execute('SELECT employer_name, COUNT (*) FROM vacancy GROUP BY employer_name')
                all_vacancy = cur.fetchall()
                cur.close()
        conn.close()
        return all_vacancy


    def get_all_vacancies(self):
        with psycopg2.connect(
                host='localhost',
                database='hh_api',
                user='postgres',
                password='Oblivion94$'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT employer_name, vacancy_name, salary, url  FROM vacancy')
                all_vacancy = cur.fetchall()
                cur.close()
        conn.close()
        return all_vacancy


    def get_avg_salary(self):
        with psycopg2.connect(
                host='localhost',
                database='hh_api',
                user='postgres',
                password='Oblivion94$'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT AVG(salary) FROM vacancy')
                avg_salary = cur.fetchall()
                cur.close()
        conn.close()
        return avg_salary


    def get_vacancies_with_higher_salary(self):
        with psycopg2.connect(
                host='localhost',
                database='hh_api',
                user='postgres',
                password='Oblivion94$'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM vacancy '
                            'WHERE salary > (SELECT AVG(salary) FROM vacancy) '
                            'ORDER BY salary DESC')
                vac = cur.fetchall()
                cur.close()
        conn.close()
        return vac


    def get_vacancies_with_keyword(self, word):
        with psycopg2.connect(
                host='localhost',
                database='hh_api',
                user='postgres',
                password='Oblivion94$'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM vacancy WHERE vacancy_name LIKE '%{word}%'")
                vac = cur.fetchall()
                cur.close()
        conn.close()
        return vac
