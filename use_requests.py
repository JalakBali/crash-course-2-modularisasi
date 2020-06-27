import requests

url = 'https://detik.com'
try:
    respons = requests.get(url)
    if respons.status_code == 200:
            print(f'sukses, respons = {respons.status_code}')
            print(f'content {respons.text}')
    else:
        print(f'woops ada kesalahan request {respons.status_code}')
except Exception as e :
    print('there is an error',e)
print('program ended')
