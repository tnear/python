# logging — Logging facility for Python
# https://docs.python.org/3/library/logging.html

import logging

def logLevels():
    # there are 5 log levels:
    # 1. debug    (10)
    # 2. info     (20)
    # 3. warning  (30)
    # 4. error    (40)
    # 5. critical (50)

    logging.debug('debug message here')
    logging.info('info message here')
    logging.error('error message here')

def getLogger():
    logger = logging.getLogger()
    # verify current warning level (30)
    assert logger.level == logging.WARNING

def isEnabledFor():
    # checks what levels logging is enabled for
    assert logging.getLogger().isEnabledFor(logging.WARNING)
    assert not logging.getLogger().isEnabledFor(logging.DEBUG)

def main():
    logLevels()
    getLogger()
    isEnabledFor()

if __name__ == '__main__':
    main()
    print('Tests passed!')
