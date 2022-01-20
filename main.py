import controller as con
from psycopg2 import Error
import sys

c = con.Controller()

try:
    command = sys.argv[1]
except IndexError:
    c.v.no_command()
else:
    if command == 'print_table':
        try:
            name = sys.argv[2]
        except IndexError:
            c.v.argument_error()
        else:
            c.print(name)

    elif command == 'delete_record':
        try:
            args = {"name": sys.argv[2], "key": sys.argv[3], "val": sys.argv[4]}
        except IndexError:
            c.v.argument_error()
        else:
            c.delete(args["name"], args["key"], args["val"])

    elif command == 'update_record':
        try:
            args = {"name": sys.argv[2], "key": sys.argv[3]}
            if args["name"] == 'Social_Network':
                args["name"], args["web_address"] = \
                    sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]
            elif args["name"] == 'User':
                args["name"], args["subscriptions"], args["date"], args["id_network"] = \
                    sys.argv[4], sys.argv[5], sys.argv[6]
            elif args["name"] == 'Post':
                args["date"], args["id_user"], args["likes"], args["id_network"] = \
                    sys.argv[4], sys.argv[5], sys.argv[6]
            elif args["name"] == 'Comment':
                args["id_user"], args["id_post"], args["likes"], args["date"], args["pid_comment"] = \
                    sys.argv[4], sys.argv[5]
            else:
                c.v.wrong_table()
        except IndexError:
            c.v.argument_error()
        else:
            if args["name"] == 'Social_Network':
                c.update_social_network(args["name"], args["web_address"])
            elif args["name"] == 'User':
                c.update_user(args["name"], args["subscriptions"], args["date"], args["id_network"])
            elif args["name"] == 'Post':
                c.update_post(args["date"], args["id_user"], args["likes"], args["id_network"])
            elif args["name"] == 'Comment':
                c.update_comment(args["id_user"], args["id_post"], args["likes"], args["date"], args["pid_comment"])

    elif command == 'insert_record':
        try:
            args = {"name": sys.argv[2], "key": sys.argv[3]}
            if args["name"] == 'Social_Network':
                args["name"], args["web_address"] = \
                    sys.argv[4], sys.argv[5]
            elif args["name"] == 'User':
                args["name"], args["subscriptions"], args["date"], args["id_network"] = \
                    sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]
            elif args["name"] == 'Post':
                args["id_user"], args["likes"], args["date"], args["id_network"] = \
                    sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]
            elif args["name"] == 'Comment':
                args["id_user"], args["id_post"], args["likes"], args["date"], args["pid_comment"] = \
                    sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]
            else:
                c.v.wrong_table()
        except IndexError:
            c.v.argument_error()
        else:
            if args["name"] == 'Social_Network':
                c.insert_social_network(args["key"], args["name"], args["web_address"])
            elif args["name"] == 'User':
                c.insert_user(args["key"], args["name"], args["subscriptions"], args["date"], args["id_network"])
            elif args["name"] == 'Post':
                c.insert_post(args["key"], args["id_user"], args["likes"], args["date"], args["id_network"])
            elif args["name"] == 'Comment':
                c.insert_comment(args["key"], args["id_user"], args["id_post"], args["date"], args["pid_comment"])


    elif command == 'search_records':
        if len(sys.argv) in [6, 9, 12]:
            search_num = c.v.get_search_num()
            try:
                search_num = int(search_num)
            except ValueError:
                c.v.invalid_search_num()
            else:
                if search_num > 0:
                    if len(sys.argv) == 6:
                        args = {"table1_name": sys.argv[2], "table2_name": sys.argv[3],
                                "key1_name": sys.argv[4], "key2_name": sys.argv[5]}
                        c.search_two(args["table1_name"], args["table2_name"], args["key1_name"], args["key2_name"],
                                     c.v.proceed_search(search_num))
                    elif len(sys.argv) == 9:
                        args = {"table1_name": sys.argv[2], "table2_name": sys.argv[3], "table3_name": sys.argv[4],
                                "key1_name": sys.argv[5], "key2_name": sys.argv[6], "key3_name": sys.argv[7],
                                "key13_name": sys.argv[8]}
                        c.search_three(args["table1_name"], args["table2_name"], args["table3_name"],
                                       args["key1_name"], args["key2_name"], args["key3_name"], args["key13_name"],
                                       c.v.proceed_search(search_num))
                    elif len(sys.argv) == 12:
                        args = {"table1_name": sys.argv[2], "table2_name": sys.argv[3], "table3_name": sys.argv[4],
                                "table4_name": sys.argv[5],
                                "key1_name": sys.argv[6], "key2_name": sys.argv[7], "key3_name": sys.argv[8],
                                "key13_name": sys.argv[9], "key4_name": sys.argv[10], "key24_name": sys.argv[11]}
                        c.search_four(args["table1_name"], args["table2_name"], args["table3_name"],
                                      args["table4_name"],
                                      args["key1_name"], args["key2_name"], args["key3_name"], args["key13_name"],
                                      args["key4_name"], args["key24_name"], c.v.proceed_search(search_num))
                else:
                    c.v.invalid_search_num()
        else:
            c.v.argument_error()
    else:
        c.v.wrong_command()
