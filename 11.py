a=input("Εισάγετε το e-mail σας για να παραλάβετε μια τυχαία μπύρα: ")
import requests
r = requests.get('https://api.punkapi.com/v2/beers/random')
txt=("Ορίστε η Μπύρα σας και όλες οι πληροφορίες γι' αυτή: " , r.text)
key = 'key-c2695dc0c1621c62a79a0249d8d32c3b'
sandbox = 'sandbox057545aa0bdb42d6b6b50b1b39b52233.mailgun.org'
recipient = a

request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key), data={
    'from': 'beer@example.com',
    'to': recipient,
    'subject': 'Ορίστε η Μπύρα σας',
    'text': txt
})

print ('Status: {0}'.format(request.status_code))
print ('Body:   {0}'.format(request.text))
