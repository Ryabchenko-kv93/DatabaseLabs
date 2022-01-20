import datetime


class Validator:
    def __init__(self):
        self.error = ''
        self.er_flag = False

    def check_table_name(self, arg: str):
        if arg in ['Social_Network', 'User', 'Post', 'Comment']:
            return arg
        else:
            self.er_flag = True
            self.error = f'table {arg} does not exist in the database'
            print(self.error)
            return False

    def check_pkey_value(self, arg: str, min_val: int, max_val: int):
        try:
            value = int(arg)
        except ValueError:
            self.er_flag = True
            self.error = f'{arg} is not correct primary key value'
            print(self.error)
            return 0
        else:
            if min_val <= value <= max_val:
                return value
            else:
                self.er_flag = True
                self.error = f'{arg} is not existing primary key value'
                print(self.error)
                return 0

    def check_pk_name(self, table_name: str, key_name: str):
        if table_name == 'Social_Network' and key_name == 'id_network' \
                or table_name == 'User' and key_name == 'id_user' \
                or table_name == 'Post' and key_name == 'id_post' \
                or table_name == 'Comment' and key_name == 'id_comment':
            return key_name
        else:
            self.er_flag = True
            self.error = f'key {key_name} is not a primary key of table {table_name}'
            print(self.error)
            return False

    def check_pk(self, val, count):
        try:
            value = int(val)
        except ValueError:
            self.er_flag = True
            self.error = f'{val} is not correct primary key value'
            print(self.error)
            return 0
        else:
            if count and not count == (0,):
                return value
            else:
                return 0

    def check_key_names(self, table_name: str, key: str):
        if table_name == 'Social_Network' and key in ['id_network', 'name', 'web_address']:
            return True
        elif table_name == 'User' and key in ['id_user', 'name', 'subscriptions', 'date', 'id_network']:
            return True
        elif table_name == 'Post' and key in ['date', 'id_post', 'id_user', 'likes', 'id_network']:
            return True
        elif table_name == 'Comment' and key in ['id_comment', 'id_user', 'id_post', 'likes', 'date', 'pid_comment']:
            return True
        else:
            self.er_flag = True
            self.error = f'{key} is not correct name for {table_name} table'
            print(self.error)
            return False

    def check_possible_keys(self, table_name: str, key: str, val):
        if table_name == 'Social_Network':
            if key in ['id_network']:
                try:
                    value = int(val)
                except ValueError:
                    self.er_flag = True
                    self.error = f'{val} is not correct key value'
                    print(self.error)
                    return False
                else:
                    return True
            elif key in ['name', 'web_address']:
                return True
            else:
                self.er_flag = True
                self.error = f'{key} is not correct name for Social_Network table'
                print(self.error)
                return False
        elif table_name == 'User':
            if key in ['id_user', 'id_network']:
                try:
                    value = int(val)
                except ValueError:
                    self.er_flag = True
                    self.error = f'{val} is not correct key value'
                    print(self.error)
                    return False
                else:
                    return True
            elif key in ['name', 'subscriptions']:
                return True
            elif key == 'date':
                try:
                    arr = [int(x) for x in val.split(sep='.')]
                    datetime.datetime(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
                except TypeError:
                    self.er_flag = True
                    self.error = f'{val} is not correct date value'
                    print(self.error)
                    return False
                else:
                    return True
            else:
                self.er_flag = True
                self.error = f'{key} is not correct name for User table'
                print(self.error)
                return False
        elif table_name == 'Post':
            if key in ['id_post', 'id_user', 'id_network']:
                try:
                    value = int(val)
                except ValueError:
                    self.er_flag = True
                    self.error = f'{val} is not correct key value'
                    print(self.error)
                    return False
                else:
                    return True
            elif key == 'likes':
                return True
            elif key == 'date':
                try:
                    arr = [int(x) for x in val.split(sep='.')]
                    datetime.datetime(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
                except TypeError:
                    self.er_flag = True
                    self.error = f'{val} is not correct date value'
                    print(self.error)
                    return False
                else:
                    return True
            else:
                self.er_flag = True
                self.error = f'{key} is not correct name for Post table'
                print(self.error)
                return False
        elif table_name == 'Comment':
            if key in ['id_comment', 'id_user', 'id_post', 'pid_comment']:
                try:
                    value = int(val)
                except ValueError:
                    self.er_flag = True
                    self.error = f'{val} is not correct key value'
                    print(self.error)
                    return False
                else:
                    return True
            elif key == 'likes':
                return True
            elif key == 'date':
                try:
                    arr = [int(x) for x in val.split(sep='.')]
                    datetime.datetime(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
                except TypeError:
                    self.er_flag = True
                    self.error = f'{val} is not correct date value'
                    print(self.error)
                    return False
                else:
                    return True
            else:
                self.er_flag = True
                self.error = f'{key} is not correct name for Comment table'
                print(self.error)
                return False
