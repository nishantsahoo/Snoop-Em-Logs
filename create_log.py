import time

file_log = open("log_file.txt","w")
file_log.write('Step 1: First step completed\n')
file_log.close()

time.sleep(6)

file_log = open("log_file.txt","a+")
file_log.write('Step 2: Second step completed!')
file_log.close()

time.sleep(6)

file_status = open('status.txt', 'w')
file_status.write('True')
file_status.close()