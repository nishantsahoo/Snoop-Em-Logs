import time

def str_to_bool(s):
    if s == 'True':
         return True
    elif s == 'False':
         return False

while not str_to_bool(open('status.txt', 'r').read()):
	file_log = open('log_file.txt', 'r')
	for each_log in file_log:
		print(each_log)	
	time.sleep(5)