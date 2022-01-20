import psycopg2
from psycopg2 import Error
import model
import view
import datetime
import time


class Controller:
    def __init__(self):
        self.v = view.View()
        self.m = model.Model()

    def print(self, table_name):
        t_name = self.v.valid.check_table_name(table_name)
        if t_name:
            if t_name == 'Social_Network':
                self.v.print_sn(self.m.print_sn())
            elif t_name == 'User':
                self.v.print_user(self.m.print_user())
            elif t_name == 'Post':
                self.v.print_post(self.m.print_post())
            elif t_name == 'Comment':
                self.v.print_comment(self.m.print_comment())

    def delete(self, table_name, key_name, value):
        t_name = self.v.valid.check_table_name(table_name)
        k_name = self.v.valid.check_pk_name(table_name, key_name)
        if t_name and k_name:
            count = self.m.find(t_name, k_name, value)
            k_val = self.v.valid.check_pk(value, count)
            if k_val:
                if t_name == 'User' or t_name == 'Post':
                    try:
                        self.m.delete_data(table_name, key_name, k_val)
                    except (Exception, Error) as _ex:
                        self.v.sql_error(_ex)
                elif t_name == 'Comment':
                    
                    try:
                        self.m.delete_data(table_name, key_name, k_val)
                    except (Exception, Error) as _ex:
                        self.v.sql_error(_ex)
                else:
                    try:
                        self.m.delete_data(table_name, key_name, k_val)
                    except (Exception, Error) as _ex:
                        self.v.sql_error(_ex)
            else:
                self.v.deletion_error()

    def update_social_network(self, key: int, name: str, web_address: str):
        if self.v.valid.check_possible_keys('Social_Network', 'id_network', key):
            count_p = self.m.find('Social_Network', 'id_network', int(key))
            p_val = self.v.valid.check_pk(key, count_p)

        if p_val and self.v.valid.check_possible_keys('Social_Network', 'name', web_address):
            try:
                self.m.update_data_social_network(p_val, name, web_address)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.updation_error()

    def update_user(self, key: str, name: str, subscriptions: str, date: str, id_network: int):
        if self.v.valid.check_possible_keys('User', 'id_user', key):
            count_s = self.m.find('User', 'id_user', int(key))
            s_val = self.v.valid.check_pk(key, count_s)
        if self.v.valid.check_possible_keys('Social_Network', 'id_network', id_network):
            count_o = self.m.find('Social_Network', 'id_network', int(id_network))
            o_val = self.v.valid.check_pk(id_network, count_o)

        if s_val and o_val and self.v.valid.check_possible_keys('User', 'date', date):
            try:
                arr = [int(x) for x in date.split(sep='.')]
                self.m.update_data_user(s_val, name, subscriptions,
                                         datetime.datetime(arr[0], arr[1], arr[2],
                                                           arr[3], arr[4], arr[5]), o_val)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.updation_error()

    def update_post(self, key: str, id_user: int, id_network: int, likes: int, date: str):
        if self.v.valid.check_possible_keys('User', 'id_user', id_user):
            count_s = self.m.find('User', 'id_user', int(id_user))
            s_val = self.v.valid.check_pk(id_user, count_s)
        if self.v.valid.check_possible_keys('Post', 'id_post', key):
            count_c = self.m.find('Post', 'id_post', int(key))
            c_val = self.v.valid.check_pk(key, count_c)
        if self.v.valid.check_possible_keys('Social_Network', 'id_network', id_network):
            count_pc = self.m.find('Social_Network', 'id_network', int(id_network))
            pc_val = self.v.valid.check_pk(id_network, count_pc)

        if s_val and c_val and pc_val and self.v.valid.check_possible_keys('Post', 'date', date):
            try:
                arr = [int(x) for x in date.split(sep='.')]
                self.m.update_data_catalog(c_val, s_val, pc_val, likes, datetime.datetime(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]))
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.updation_error()

    def update_comment(self, key: str, id_user: int, id_post: int, likes: int, date: str, pid_comment: int):
        if self.v.valid.check_possible_keys('Shop', 'id_shop', key):
            count_s = self.m.find('Shop', 'id_shop', int(key))
            s_val = self.v.valid.check_pk(key, count_s)
        if self.v.valid.check_possible_keys('Post', 'id_post', id_post):
            count_o = self.m.find('Post', 'id_post', id_post)
            o_val = self.v.valid.check_pk(id_post, count_o)
        if self.v.valid.check_possible_keys('User', 'id_user', id_user):
            count_c = self.m.find('User', 'id_user', id_user)
            c_val = self.v.valid.check_pk(id_user, count_c)
        if self.v.valid.check_possible_keys('Comment', 'pid_comment', pid_comment):
            count_v = self.m.find('Comment', 'pid_comment', pid_comment)
            v_val = self.v.valid.check_pk(pid_comment, count_v)

        if s_val and o_val and c_val and v_val and self.v.valid.check_possible_keys('Comment', 'date', date):
            try:
                arr = [int(x) for x in date.split(sep='.')]
                self.m.update_data_shop(s_val, c_val, o_val, likes, datetime.datetime(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]), v_val)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.updation_error()

    def insert_social_network(self, key: str, name: str, web_address: str):
        if self.v.valid.check_possible_keys('Product', 'id_product', key):
            count_p = self.m.find('Product', 'id_product', int(key))[0]

        if (not count_p or count_p == (0,))\
                and self.v.valid.check_possible_keys('Social_Network', 'id_network', key):
            try:
                self.m.insert_data_product(int(key), name, web_address)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.insertion_error()

    def insert_user(self, key: str, name: str, subscriptions: str, date: str, id_network: int):
        if self.v.valid.check_possible_keys('Social_Network', 'id_network', id_network):
            count_s = self.m.find('Social_Network', 'id_network', int(id_network))
            s_val = self.v.valid.check_pk(id_network, count_s)
        if self.v.valid.check_possible_keys('User', 'id_user', key):
            count_o = self.m.find('User', 'id_user', int(key))[0]

        if (not count_o or count_o == (0,)) and s_val and self.v.valid.check_possible_keys('User', 'id_user', key) \
                and self.v.valid.check_possible_keys('User', 'date', date):
            try:
                arr = [int(x) for x in date.split(sep='.')]
                self.m.insert_data_order(int(key), name, s_val,
                                         datetime.datetime(arr[0], arr[1], arr[2],
                                                           arr[3], arr[4], arr[5]))
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.insertion_error()

    def insert_post(self, key: str, id_network: str, id_user: int, likes: int, date: str):
        if self.v.valid.check_possible_keys('User', 'id_user', id_user):
            count_s = self.m.find('User', 'id_user', int(id_user))
            s_val = self.v.valid.check_pk(id_user, count_s)
        if self.v.valid.check_possible_keys('Post', 'id_post', key):
            count_c = self.m.find('Post', 'id_post', int(key))[0]
        if self.v.valid.check_possible_keys('Social_Network', 'id_network', id_network):
            count_pc = self.m.find('Social_Network', 'id_network', int(id_network))
            pc_val = self.v.valid.check_pk(id_network, count_pc)

        if (not count_c or count_c == (0,)) and s_val and pc_val \
                and self.v.valid.check_possible_keys('Post', 'id_post', key)\
                and self.v.valid.check_possible_keys('Post', 'date', date):
            try:
                arr = [int(x) for x in date.split(sep='.')]
                self.m.insert_data_order(datetime.datetime(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]), int(key), s_val, likes, pc_val)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.insertion_error()

    def insert_comment(self, key: str, id_user: int, id_post: int, likes: int, date: str, pid_comment: int):
        if self.v.valid.check_possible_keys('Shop', 'id_shop', key):
            count_o = self.m.find('Shop', 'id_shop', int(key))[0]
        if self.v.valid.check_possible_keys('User', 'id_user', id_user):
            count_s = self.m.find('User', 'id_user', int(id_user))
            s_val = self.v.valid.check_pk(id_user, count_s)
        if self.v.valid.check_possible_keys('Post', 'id_post', id_post):
            count_c = self.m.find('Post', 'id_post', int(id_post))[0]
            c_val = self.v.valid.check_pk(id_post, count_c)
        if self.v.valid.check_possible_keys('Comment', 'pid_comment', pid_comment):
            count_pc = self.m.find('Comment', 'pid_comment', int(pid_comment))
            pc_val = self.v.valid.check_pk(pid_comment, count_pc)

        if (not count_o or count_o == (0,) and s_val and c_val and self.v.valid.check_possible_keys('Comment', 'id_comment', key)):
            try:
                arr = [int(x) for x in date.split(sep='.')]
                self.m.insert_data_shop(int(key), s_val, c_val, likes, datetime.datetime(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]), pc_val)
            except (Exception, Error) as _ex:
                self.v.sql_error(_ex)
        else:
            self.v.insertion_error()

    def search_two(self, table1_name: str, table2_name: str, table1_key: str, table2_key: str, search: str):
        t1_n = self.v.valid.check_table_name(table1_name)
        t2_n = self.v.valid.check_table_name(table2_name)
        if t1_n and self.v.valid.check_key_names(t1_n, table1_key) and t2_n \
                and self.v.valid.check_key_names(t2_n, table2_key):
            start_time = time.time()
            result = self.m.search_data_two_tables(table1_name, table2_name, table1_key, table2_key,
                                                   search)
            self.v.print_time(start_time)

            self.v.print_search(result)

    def search_three(self, table1_name: str, table2_name: str, table3_name: str,
                     table1_key: str, table2_key: str, table3_key: str, table13_key: str,
                     search: str):
        t1_n = self.v.valid.check_table_name(table1_name)
        t2_n = self.v.valid.check_table_name(table2_name)
        t3_n = self.v.valid.check_table_name(table3_name)
        if t1_n and self.v.valid.check_key_names(t1_n, table1_key) and self.v.valid.check_key_names(t1_n, table13_key) \
                and t2_n and self.v.valid.check_key_names(t2_n, table2_key) \
                and t3_n and self.v.valid.check_key_names(t3_n, table3_key) \
                and self.v.valid.check_key_names(t3_n, table13_key):
            start_time = time.time()
            result = self.m.search_data_three_tables(table1_name, table2_name, table3_name,
                                                     table1_key, table2_key, table3_key, table13_key,
                                                     search)
            self.v.print_time(start_time)
            self.v.print_search(result)

    def search_four(self, table1_name: str, table2_name: str, table3_name: str, table4_name: str,
                    table1_key: str, table2_key: str, table3_key: str, table13_key: str,
                    table4_key: str, table24_key: str,
                    search: str):
        t1_n = self.v.valid.check_table_name(table1_name)
        t2_n = self.v.valid.check_table_name(table2_name)
        t3_n = self.v.valid.check_table_name(table3_name)
        t4_n = self.v.valid.check_table_name(table2_name)
        if t1_n and self.v.valid.check_key_names(t1_n, table1_key) and self.v.valid.check_key_names(t1_n, table13_key) \
                and t2_n and self.v.valid.check_key_names(t2_n, table2_key) \
                and self.v.valid.check_key_names(t2_n, table24_key) \
                and t3_n and self.v.valid.check_key_names(t3_n, table3_key) \
                and self.v.valid.check_key_names(t3_n, table13_key) \
                and t4_n and self.v.valid.check_key_names(t4_n, table4_key) \
                and self.v.valid.check_key_names(t4_n, table24_key):

            start_time = time.time()
            result = self.m.search_data_all_tables(table1_name, table2_name, table3_name, table4_name,
                                                   table1_key, table2_key, table3_key, table13_key,
                                                   table4_key, table24_key,
                                                   search)
            self.v.print_time(start_time)
            self.v.print_search(result)
