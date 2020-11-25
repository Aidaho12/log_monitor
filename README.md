# Log Monitor

Log Monitor scans a log file and generates a report with all errors. 
The order of the errors follow the same order as the log file. 
Log Monitor uses "-----" as the separator between different sessions. 
For each error, the report also includes at most the last 3  messages for the same session before that error.


# Usage

```
./read_log.py 
usage: read_log.py [-h] [--output [OUTPUT]] [log_file]

Log monitoring

positional arguments:
  log_file           Log file for consuming (default: None)

optional arguments:
  -h, --help         show this help message and exit
  --output [OUTPUT]  Output file (default: error.txt)
```

### Output

Output looks like:

```
cat errors.txt

2019-4-1 13:33:45 [123] User1 goes to search page
2019-4-1 13:33:46 [123] User1 types in search text
2019-4-1 13:33:50 [123] User1 clicks search button
2019-4-1 13:33:54 [123] ERROR: Some exception occurred
----
2019-4-1 13:32:40 [190] User3 logs in
2019-4-1 13:33:49 [190] User3 runs some job
2019-4-1 13:33:57 [190] ERROR: Invalid input
----
```

# Testing

```
python3.8 -m unittest -v test_read_log.py
test_find_last_3 (test_read_log.TestRead) ... Compare list 1
['2019-4-1 13:33:45 [123] User1 goes to search page\n', '2019-4-1 13:33:46 [123] User1 types in search text\n', '2019-4-1 13:33:50 [123] User1 clicks search button\n', '2019-4-1 13:33:54 [123] ERROR: Some exception occurred\n']
[123]
9
Compare list 2
['2019-4-1 13:32:40 [190] User3 logs in\n', '2019-4-1 13:33:49 [190] User3 runs some job\n', '2019-4-1 13:33:57 [190] ERROR: Invalid input\n']
[190]
11
ok
test_write_to_file (test_read_log.TestRead) ... Check writable line 0
Check writable line 1
Check writable line 2
Check writable line 3
Check writable line 0
Check writable line 1
Check writable line 2
ok

----------------------------------------------------------------------
Ran 2 tests in 0.007s

OK
```
