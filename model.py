import datetime
import psycopg2 as ps


class Model:
    def __init__(self):
        self.conn = None
        try:
            self.conn = ps.connect(
                database="socNetwork",
                user='postgres',
                password="1111",
                host='localhost',
                port="5432",
            )
        except(Exception, ps.DatabaseError) as error:
            print("[INFO] Error while working with Postgresql", error)

    def request(self, req: str):
        try:
            cursor = self.conn.cursor()
            print(req)
            cursor.execute(req)
            self.conn.commit()
            return True
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            print(error)
            self.conn.rollback()
            return False

    def get(self, req: str):
        try:
            cursor = self.conn.cursor()
            print(req)
            cursor.execute(req)
            self.conn.commit()
            return cursor.fetchall()
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            print(error)
            self.conn.rollback()
            return False

    def get_el(self, req: str):
        try:
            cursor = self.conn.cursor()
            print(req)
            cursor.execute(req)
            self.conn.commit()
            return cursor.fetchone()
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            print(error)
            self.conn.rollback()
            return False

    def count(self, table_name: str):
        return self.get_el(f"select count(*) from public.\"{table_name}\"")

    def find(self, table_name: str, key_name: str, key_value: int):
        return self.get_el(f"select count(*) from public.\"{table_name}\" where {key_name}={key_value}")

    def max(self, table_name: str, key_name: str):
        return self.get_el(f"select max({key_name}) from public.\"{table_name}\"")

    def min(self, table_name: str, key_name: str):
        return self.get_el(f"select min({key_name}) from public.\"{table_name}\"")

    def print_sn(self) -> None:
        return self.get(f"SELECT * FROM public.\"Social_Network\"")

    def print_user(self) -> None:
        return self.get(f"SELECT * FROM public.\"User\"")

    def print_post(self) -> None:
        return self.get(f"SELECT * FROM public.\"Post\"")

    def print_comment(self) -> None:
        return self.get(f"SELECT * FROM public.\"Comment\"")

    def delete_data(self, table_name: str, key_name: str, key_value) -> None:
        self.request(f"DELETE FROM public.\"{table_name}\" WHERE {key_name}={key_value};")

    def update_data_social_network(self, key_value: int, name: str, web_address: str) -> None:
        self.request(f"UPDATE public.\"Social_Network\" SET name=\'{name}\', web_address=\'{web_address}\' WHERE id_network={key_value};")

    def update_data_user(self, key_value: int, name: str, subscriptions: str, date: datetime.datetime, id_network: int) -> None:
        self.request(f"UPDATE public.\"User\" SET name=\'{name}\', subscriptions=\'{subscriptions}\', "
                     f"date=\'{date}\', id_network={id_network} WHERE id_order={key_value};")

    def update_data_post(self, key_value: int, id_user: int, id_network: int, likes: int, date: datetime.datetime) -> None:
        self.request(f"UPDATE public.\"Post\" SET id_user={id_user}, id_network={id_network}, "
                     f"likes={likes}, date=\'{date}\' WHERE id_order={key_value};")

    def update_data_comment(self, key_value: int, id_user: int, id_post: int, likes: int, date: datetime.datetime, pid_comment: int) -> None:
        self.request(f"UPDATE public.\"Comment\" SET id_user={id_user}, id_post={id_post}, likes={likes} "
                     f"date=\'{date}\', pid_comment={pid_comment} WHERE id_shop={key_value};")

    def insert_data_social_network(self, id_network: int, name: str, web_address: str) -> None:
        self.request(f"insert into public.\"Social_Network\" (id_network, name, web_address) "
                     f"VALUES ({id_network}, \'{name}\', \'{web_address}\');")

    def insert_data_user(self, id_user: int, name: str, subscriptions: int, date: datetime.datetime, id_network: int) -> None:
        self.request(f"insert into public.\"User\" (id_user, name, subscriptions, date, id_network) "
                     f"VALUES ({id_user}, \'{name}\', \'{subscriptions}\', \'{date}\', {id_network});")

    def insert_data_post(self, id_post: int, id_user: int, likes: int, id_network: int, date: datetime.datetime) -> None:
        self.request(f"insert into public.\"Post\" (id_post, id_user, likes, id_network, date) "
                     f"VALUES ({id_post}, {id_user}, {likes}, {id_network}, \'{date}\');")

    def insert_data_comment(self, id_comment: int, id_user: int, id_post: int, likes: int, date: datetime.datetime, pid_comment: int) -> None:
        self.request(f"insert into public.\"Comment\" (id_comment, id_user, id_post, likes, date, pid_comment) "
                     f"VALUES ({id_comment}, {id_user}, {id_post}, {likes}, {date}, {pid_comment});")

    def search_data_two_tables(self, table1_name: str, table2_name: str, table1_key, table2_key,
                               search: str):
        return self.get(f"select * from public.\"{table1_name}\" as one inner join public.\"{table2_name}\" as two "
                        f"on one.\"{table1_key}\"=two.\"{table2_key}\" "
                        f"where {search}")

    def search_data_three_tables(self, table1_name: str, table2_name: str, table3_name: str,
                                 table1_key, table2_key, table3_key, table13_key,
                                 search: str):
        return self.get(f"select * from public.\"{table1_name}\" as one inner join public.\"{table2_name}\" as two "
                        f"on one.\"{table1_key}\"=two.\"{table2_key}\" inner join public.\"{table3_name}\" as three "
                        f"on three.\"{table3_key}\"=one.\"{table13_key}\""
                        f"where {search}")

    def search_data_all_tables(self, table1_name: str, table2_name: str, table3_name: str, table4_name: str,
                               table1_key, table2_key, table3_key, table13_key,
                               table4_key, table24_key,
                               search: str):
        return self.get(f"select * from public.\"{table1_name}\" as one inner join public.\"{table2_name}\" as two "
                        f"on one.\"{table1_key}\"=two.\"{table2_key}\" inner join public.\"{table3_name}\" as three "
                        f"on three.\"{table3_key}\"=one.\"{table13_key}\" inner join public.\"{table4_name}\" as four "
                        f"on four.\"{table4_key}\"=two.\"{table24_key}\""
                        f"where {search}")

