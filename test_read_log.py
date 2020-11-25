#!/usr/local/bin/python3

import unittest
import read_log

file_name = 'log.txt'
session_id1 = '[123]'
session_id2 = '[190]'
line_num1 = 9
line_num2 = 11
comparing_list1 = ['2019-4-1 13:33:45 [123] User1 goes to search page\n', '2019-4-1 13:33:46 [123] User1 types in search text\n', '2019-4-1 13:33:50 [123] User1 clicks search button\n', '2019-4-1 13:33:54 [123] ERROR: Some exception occurred\n']
comparing_list2 = ['2019-4-1 13:32:40 [190] User3 logs in\n', '2019-4-1 13:33:49 [190] User3 runs some job\n', '2019-4-1 13:33:57 [190] ERROR: Invalid input\n']


class TestRead(unittest.TestCase):
    def test_find_last_3(self):
        print('Compare list 1')
        self.assertListEqual(read_log.find_last_3(file_name, session_id1, line_num1), comparing_list1)

        print('Compare list 2')
        self.assertListEqual(read_log.find_last_3(file_name, session_id2, line_num2), comparing_list2)

    def test_write_to_file(self):
        for l in range(len(comparing_list1)):
            print('Check writable line ' + str(l))
            self.assertMultiLineEqual(read_log.write_to_file(comparing_list1[l], 'error.txt'), comparing_list1[l])

        for l in range(len(comparing_list2)):
            print('Check writable line ' + str(l))
            self.assertMultiLineEqual(read_log.write_to_file(comparing_list2[l], 'error.txt'), comparing_list2[l])
