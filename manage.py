import sys

if len(sys.argv) < 2:
    print 'python %s <command>' % sys.argv[0]
    sys.exit(1)

if sys.argv[1] == 'initdb':
    from app import db
    try:
        db.create_all()
    except Exception e:
        raise e
    else:
        print 'Succeeded'
