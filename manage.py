import os
import sys
from app import app, db

if len(sys.argv) < 2:
    print 'python %s <command>' % sys.argv[0]
    sys.exit(1)

if sys.argv[1] == 'initdb':
    try:
        db.create_all()
    except Exception, e:
        raise e
    else:
        print 'Succeeded'

elif sys.argv[1] == 'debug':
    app.debug = True
    app.run(port=9338)

elif sys.argv[1] == 'run':
    os.system("gunicorn -c confs/gunicorn.ini app:app")
