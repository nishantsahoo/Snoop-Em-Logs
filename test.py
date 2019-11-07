import time
file_test = open('text.txt', 'w')
file_test.write('First')
file_test.close()
time.sleep(10)
file_test = open('text.txt', 'w')
file_test.write('Second')
file_test.close()