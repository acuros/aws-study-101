import httplib
import random
import sys
import time
import urllib

def add_user(server):
    strings = 'abcdefghijklmnopqrstuvwxyz0123456789'
    username = ''.join([random.sample(strings, 1)[0] for x in xrange(20)])
    email_server = ''.join([random.sample(strings, 1)[0] for x in xrange(20)])
    email = '{0}@{1}.com'.format(username, email_server)
    body = urllib.urlencode(dict(username=username, email=email))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    

    started_at = time.time()
    conn = httplib.HTTPConnection(server, 80)
    conn.request('POST', '/add', body, headers)
    print conn.getresponse().status
    conn.close()


add_user(sys.argv[1])
