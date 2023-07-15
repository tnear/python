# http — HTTP modules
# https://docs.python.org/3/library/http.html

import http

def status():
    assert http.HTTPStatus.OK == 200
    assert http.HTTPStatus.NOT_FOUND == 404

def main():
    status()

if __name__ == '__main__':
    main()
    print('Tests passed!')
