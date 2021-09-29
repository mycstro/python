#!/usr/bin/python
import logging
import csv
import fbconsole

logger = logging.getLogger('root')
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)


def authenticate():
    logger.debug('Authentication process')
    fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins']
    fbconsole.authenticate()


def postMessage(msg):
    logger.debug(msg)
    status = fbconsole.post('/me/feed', {'message': msg})
    print(status)


def main():
    authenticate();


if __name__ == '__main__':
    main()
    fbconsole.logout()
    postMessage("3rd test")