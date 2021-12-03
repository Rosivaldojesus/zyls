import json
import requests


def service_url(service_name):
  return 'https://api.coinext.com.br:8443/AP/%s' % service_name


def call_get(service_name, **kwargs):
  res = requests.get(service_url(service_name), **kwargs)
  return json.loads(res.content)


def call_post(service_name, payload={}, **kwargs):
  res = requests.post(service_url(service_name),
                      json.dumps(payload), **kwargs)
  return json.loads(res.content)


def main():
  auth = call_get('authenticate', auth=('your-email', 'your-password'))
  if auth['Authenticated']:
    user_info = call_post('GetUserInfo', headers={
      'aptoken': auth['Token'],
      'Content-type': 'application/json'
    })
    print(user_info)


if __name__ == "__main__":
  main()