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
                            salary_from int,
                            salary_to int,
                            salary_cur varchar,
                            vacancy_type varchar,
                            address text,
                            published_at timestamp,
                            url varchar
                        )''')
                cur.close()






table = DBManager()

table.create_db()


table.create_tables()