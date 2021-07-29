import requests

# Checking and catching Error for Error

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    print(res.raise_for_status())
    with open('sampe_file.txt', 'wb') as file:
        # 10kilobytes is recommend for better memory management
        for chunks in res.iter_content(100000):
            file.write(chunks)
        file.close()
except Exception as exec:
    print('Check you connections %s' % (exec))
