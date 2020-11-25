#!/usr/local/bin/python3

import sys
import os
import argparse


def find_last_3(file_name, session_id, last_line):
    session_list = []

    with open(file_name, 'r') as f:
        for line_num, line in enumerate(f):
            if session_id in line:
                session_list.append(line)
            elif last_line == line_num:
                break
                
    return session_list[-4:]


def find_error(file_name, output_file):
    with open(file_name, 'r') as f:
        for line_num, line in enumerate(f):
            if "ERROR:" in line:
                session_id = line.split(' ')[2]
                session_list = find_last_3(file_name, session_id, line_num)

                for session_line in session_list:
                    write_to_file(session_line, output_file)

                write_to_file('----\n', output_file)


def write_to_file(line, output_file):
    with open(output_file, 'a') as w:
        w.write(line)

    return line


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Log monitoring',
                                     prog='read_log.py',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('log_file', help='Log file for consuming', nargs='?', type=str)
    parser.add_argument('--output', help='Output file', nargs='?', default='error.txt', type=str)

    args = parser.parse_args()
    if args.log_file is None:
        parser.print_help()
        sys.exit()
    else:
        file_name = args.log_file
        output_file = args.output

    if not os.path.isfile(file_name):
        print('There is not file ' + file_name)
        sys.exit()

    find_error(file_name, output_file)
