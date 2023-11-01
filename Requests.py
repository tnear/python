# Requests is an elegant and simple HTTP library for Python
# https://requests.readthedocs.io/en/latest/

import requests
import http
import json

def get():
    url = 'https://www.w3schools.com/python/demopage.htm'
    response = requests.get(url)
    assert isinstance(response, requests.models.Response)

    # status
    assert response.status_code == 200
    assert response.status_code == http.HTTPStatus.OK

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

def session():
    # a session objects allows you to persist parameters across requests
    # for example, it allows reusing the TCP connection to improve performance

    # list of sites
    sites = ['https://httpbin.org/cookies', 'https://httpbin.org/cookies/set/sessioncookie/123']

    # download each in a session
    with requests.Session() as session:
        for site in sites:
            response = session.get(site)
            print(response)
            assert response.status_code == 200

def main():
    get()
    getParams()
    post()
    session()

if __name__ == '__main__':
    main()
    print('Tests passed!')
