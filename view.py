import datetime
import time
import validator


class View:
    def __init__(self):
        self.valid = validator.Validator()

    def cannot_delete(self) -> None:
        print('this record is connected with another table, deleting will '
              'throw error')

    def sql_error(self, e) -> None:
        print("[INFO] Error while working with Postgresql", e)

    def insertion_error(self) -> None:
        print('Something went wrong (record with such id exists or inappropriate foreign key values)')

    def updation_error(self) -> None:
        print('Something went wrong (record with such id does not exist or inappropriate foreign key value)')

    def deletion_error(self) -> None:
        print('record with such id does not exist')

    def invalid_interval(self) -> None:
        print('invalid interval input')

    def print_time(self, start) -> None:
        print("--- %s seconds ---" % (time.time() - start))

    def print_search(self, result):
        print('search result:')
        for row in result:
            for i in range(0, len(row)):
                print(row[i])
            print('_____________________________________')

    def print_sn(self, table):
        print('Social_Network table:')
        for row in table:
            print('id_network:', row[0], '\tname:', row[1], '\tweb_address:', row[2])
            print('_____________________________________')

    def print_user(self, table):
        print('User table:')
        for row in table:
            print('id_user:', row[0], '\tname:', row[1], '\tsubscriptions:', row[2], '\tdate:', row[3], '\tid_network:', row[4])
            print('_____________________________________')

    def print_post(self, table):
        print('Post table:')
        for row in table:
            print('id_post:', row[1], '\tid_user:', row[2], '\tlikes:', row[3], '\tid_network:', row[4], '\tdate:', row[0])
            print('_____________________________________')

    def print_comment(self, table):
        print('Comment table:')
        for row in table:
            print('id_comment:', row[0], '\tid_user:', row[1], '\tid_post:', row[2], '\tlikes:', row[3], '\tdate:', row[4], '\tpid_comment:', row[5])
            print('_____________________________________')

    def proceed_search(self, search_num):
        search = ''
        for i in range(0, search_num):
            while True:
                search_type = input('specify the type of data you want to search for '
                                    '(numeric, string or date): ')
                if search_type == 'numeric' or search_type == 'string' or search_type == 'date':
                    break
            key = input('specify the name of key by which you`d like to perform search '
                        'in form: table_number.key_name: ')

            if search_type == 'numeric':
                a = input('specify the left end of search interval: ')
                b = input('specify the right end of search interval: ')
                if search == '':
                    search = self.numeric_search(a, b, key)
                else:
                    search += ' and ' + self.numeric_search(a, b, key)

            elif search_type == 'date':
                data = input('specify the left end of search interval '
                             'in form: year.month.day.hour.minute.second: ')
                datb = input('specify the right end of search interval '
                             'in form: year.month.day.hour.minute.second: ')
                if search == '':
                    search = self.date_search(data, datb, key)
                else:
                    search += ' and ' + self.date_search(data, datb, key)

            elif search_type == 'string':
                string = input('specify the string you`d like to search for: ')
                if search == '':
                    search = self.string_search(string, key)
                else:
                    search += ' and ' + self.string_search(string, key)
        return search

    def numeric_search(self, a: str, b: str, key: str):
        try:
            a, b = int(a), int(b)
        except ValueError:
            self.invalid_interval()
        else:
            return f"{a}<{key} and {key}<{b}"

    def date_search(self, a: str, b: str, key: str):
        try:
            arr = [int(x) for x in a.split(sep='.')]
            brr = [int(x) for x in b.split(sep='.')]
        except Exception:
            print(Exception)
            self.invalid_interval()
        else:
            return f"{key} BETWEEN \'{datetime.datetime(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])}\' " \
                   f"AND \'{datetime.datetime(brr[0], brr[1], brr[2], brr[3], brr[4], brr[5])}\'"

    def string_search(self, string: str, key: str):
        return f"{key} LIKE \'{string}\'"

    def get_search_num(self):
        return input('specify the number of attributes you`d like to search by: ')

    def invalid_search_num(self):
        print('should be number different from 0')

    def argument_error(self):
        print('no required arguments specified')

    def wrong_table(self):
        print('wrong table name')

    def no_command(self):
        print('no command name specified, type help to see possible commands')

    def wrong_command(self):
        print('unknown command name, type help to see possible commands')