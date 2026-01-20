'''
signal - Set handlers for asynchronous events
https://docs.python.org/3/library/signal.html
'''

import signal
import time

def signal_handler(_sig, _frame):
    print('\nYou pressed Ctrl+C!')
    exit(0)

def sigint():
    # register SIGINT handler
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C to trigger the signal handler')
    while True:
        print('Working...')
        time.sleep(1)

def main():
    sigint()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
