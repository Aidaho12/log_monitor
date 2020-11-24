#!/usr/local/bin/python3

import sys
import os


def find_last_3(file_name, session_id, last_line):
    session_list = []

    with open(file_name, 'r') as f:
        for line_num, line in enumerate(f, 1):
            if session_id in line:
                session_list.append(line)
            elif last_line == line_num:
                break
    print(session_list[-4:])
    print(session_id)
    print(last_line)
    return session_list[-4:]


def find_error(file_name):
    with open(file_name, 'r') as f:
        for line_num, line in enumerate(f, 1):
            if "ERROR:" in line:
                session_id = line.split(' ')[2]
                session_list = find_last_3(file_name, session_id, line_num)
                for session_line in session_list:
                    write_to_file(session_line)

                write_to_file('----\n')


def write_to_file(line):
    with open('errors.txt', 'a') as w:
        w.write(line)


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except Exception:
        print('Provide file name')
        sys.exit()

    if not os.path.isfile(file_name):
        print('There is not file ' + file_name)
        sys.exit()

    find_error(file_name)
