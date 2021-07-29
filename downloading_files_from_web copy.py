import requests
import sys
import csv

res = requests.get('https://filesamples.com/samples/document/txt/sample1.txt')
if res.status_code == 200 or requests.codes.ok == True:
    print(len(res.text))
    # writing the file to a csv file.
    with open('test.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(res.text)

        file.close()
else:
    raise Exception("Failed to established connection")


# Checking and catching Error for Error

res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    print(res.raise_for_status())
except Exception as exec:
    print('Check you connections %s' % (exec))
