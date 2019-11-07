import time
file_test = open('text.txt', w)
file_test.write('First')
time.sleep(10)
file_test.write('Second')
file_test.close()