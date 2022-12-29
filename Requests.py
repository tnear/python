import json
import requests

def get():
    url = 'https://www.w3schools.com/python/demopage.htm'
    response = requests.get(url)
    assert isinstance(response, requests.models.Response)

    # status
    assert response.status_code == 200

    # content
    assert 'This is a Test Page' in response.text

    # url
    updatedUrl = response.url.replace(':443', '')
    assert updatedUrl == url

    # duration
    assert response.elapsed.microseconds > 1000

def getParams():
    url = 'http://httpbin.org/get'
    payload = {
        'website': 'dataquest.io',
        'courses': ['Python', 'SQL']
    }
    response = requests.get(url, params=payload)

    assert response.url == url + '?website=dataquest.io&courses=Python&courses=SQL'

def post():
    url = 'http://httpbin.org/post'
    payload = {
        'website': 'dataquest.io',
        'courses': ['Python', 'SQL']
    }

    response = requests.post(url, data=payload)
    assert isinstance(response, requests.models.Response)
    assert response.url == url

    # post data is inside form instead of url:
    var = json.loads(response.text)
    assert var['form']['courses'] == payload['courses']

def main():
    get()
    getParams()
    post()

if __name__ == '__main__':
    main()
    print('Tests passed!')
