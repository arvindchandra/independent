

# Requires "requests" library # pip install requests
from multiprocessing import Pool
from requests import get

DOMAIN = 'ec2-3-86-207-211.compute-1.amazonaws.com'

def send_request(val):
   while True:
      response get (f'http://{DOMAIN}')
      data = response.json()
      print('Sent requeest') print(data)


if __name__ == '__main__':
   with Pool(150) as p:
      p.map(send_request, range (150))
