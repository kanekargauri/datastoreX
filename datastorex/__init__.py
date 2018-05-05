import screen
import os

# insert
def insert(args=None):
    try:
        if args == None:
            print 'ERROR: parameter not specified'
            raise Exception('parameter not specified')

        return screen.process('insert', args)
    except Exception, e:
        log.error(e)
        raise e 
    

# update
def update(args=None):
    try:
        if args == None:
            print 'ERROR: parameter not specified'
            raise Exception('parameter not specified')

        screen.process('update', args)
    except Exception, e:
        log.error(e)
        raise e 


# delete
def delete(args=None):
    try:
        if args == None:
            print 'ERROR: parameter not specified'
            raise Exception('parameter not specified')

        screen.process('delete', args)
    except Exception, e:
        log.error(e)
        raise e 


# select
def select(args=None):
    try:
        if args == None:
            print 'ERROR: parameter not specified'
            raise Exception('parameter not specified')

        return screen.process('select', args)
    except Exception, e:
        log.error(e)
        raise e 
