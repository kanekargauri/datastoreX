import MySQLdb
import itertools
import json
import MySQLdb.converters

# TODO 
# parameter names should be insensitive
# db connection pool
# db connection close finally - dont like the current implementation
# test for special characters
# test for unicodes
# test for multilingual
 

def _db_connect(args):
    try:
        conv = MySQLdb.converters.conversions.copy()
        conv[246] = float
        conv[10]  = str
        conv[11]  = str
        conv[12]  = str
        conv[7]  = str

        db = MySQLdb.connect(host   = args['host'], 
                             user   = args['user'], 
                             db     = args['namespace'], 
                             passwd = args['password'],
                             port   = int(args['port']))
        db.converter = conv
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        return db, cursor
    except Exception, e:
        raise e    


def _db_disconnect(dbpointer):
    dbpointer.close()
 

def _filter_condition_builder(args):
    try:
        temp = []
        for i in args['filter']:
            stmt = ' 1 = 1 '
            if i['operator'] == 'between':
                if isinstance(i['value'][0], str):
                    stmt = " %s between '%s' AND '%s' " % ( i['operand'], i['value'][0], i['value'][1] )
                else:
                    stmt = ' %s between %s AND %s ' % ( i['operand'], i['value'][0], i['value'][1] )
            elif i['operator'] in ('in', 'not in'):
                if isinstance(i['value'][0], int):
                    x = ",".join(format(x, "d") for x in i['value'])
                elif isinstance(i['value'][0], float):
                    x = ",".join(format(x, "10.10f") for x in i['value'])
                elif isinstance(i['value'][0], bool):
                    x = ",".join(format(x, "%r") for x in i['value'])
                else: 
                    x = ','.join(str('"%s"' %x) for x in i['value'])
                stmt = ' %s %s (%s) ' % ( i['operand'], i['operator'], x )
            else:
                if isinstance(i['value'], str):
                    stmt = " %s %s '%s' " % ( i['operand'], i['operator'], i['value'] )
                else:
                    stmt = ' %s %s %s ' % ( i['operand'], i['operator'], i['value'] )
            temp.append(stmt)

        return " AND ".join(map(str, temp))
    except Exception, e:
        raise e


def _form_insert_sql(args):
    try:
        cols = ",".join(map(str, args['data_columns']))
        vals = '%s' % str(tuple(args['values']))
        sql = 'INSERT INTO %s (%s) VALUES %s' % (args['tablename'], cols, vals)
        return sql
    except Exception, e:
        raise e


def insert(args):
    try:
        sql = _form_insert_sql(args)
        (db, c) = _db_connect(args['connection_info'])
        x = c.execute(sql)
        db.commit()
        return c.lastrowid
    except MySQLdb.Warning, e:
        raise e
    except MySQLdb.Error, e:
        raise e
    except Exception, e:
        raise e
    #finally:
    #    _db_disconnect(db)


def _form_update_sql(args):
    try:
        sql = 'UPDATE %s SET ' % (args['tablename'])

        # set condition
        x = zip(args['set_columns'], args['set_values'])

        temp = []
        for i in x:
            if isinstance(i[1], str):
                temp.append("%s = '%s'" % (i[0], i[1]))
            else:
                temp.append("%s = %s" % (i[0], i[1]))

        x   = ",".join(map(str, temp))
        sql = "%s %s" % (sql, x)

        # where condition
        x = ''
        if 'filter' in args:
            x = _filter_condition_builder(args)
        sql = "%s WHERE %s" % (sql, x)

        return sql
    except Exception, e:
        raise e


def update(args):
    try:
        sql = _form_update_sql(args)
        (db, c) = _db_connect(args['connection_info'])
        c.execute(sql)
        db.commit()
    except Exception, e:
        raise e
    finally:
        _db_disconnect(db)


def _form_delete_sql(args):
    try:
        sql = 'DELETE FROM %s ' % (args['tablename'])

        # where condition
        if 'filter' in args:
            x = _filter_condition_builder(args)
            sql = "%s WHERE %s" % (sql, x)

        return sql
    except Exception, e:
        raise e


def delete(args):
    try:
        sql = _form_delete_sql(args)
        (db, c) = _db_connect(args['connection_info'])
        c.execute(sql)
        db.commit()
    except Exception, e:
        raise e
    finally:
        _db_disconnect(db)


def _form_select_sql(args):
    try:
        x = ' * '
        if 'select_fields' in args and len(args['select_fields']) > 0:
            x = ",".join(map(str, args['select_fields']))
        sql = 'SELECT %s FROM %s WHERE ' % (x, args['tablename'])

        # where condition
        x = ' 1 = 1 '
        if 'filter' in args and len(args['filter']) > 0:
            x = _filter_condition_builder(args)
        sql = "%s %s" % (sql, x)

        # order by condition
        x = '1'
        if 'order_by' in args and len(args['order_by']) > 0:
            x = args['order_by']
        sql = "%s ORDER BY %s" % (sql, x)

        # limit condition
        x = ' 20 '
        if 'limit' in args and len(args['limit']) > 0:
            x = args['limit']
        sql = "%s LIMIT %s" % (sql, x)

        # offset condition
        x = ' 0 '
        if 'offset' in args and len(args['offset']) > 0:
            x = args['offset']
        sql = "%s OFFSET %s" % (sql, x)

        return sql
    except Exception, e:
        raise e


def select(args):
    try:
        sql = _form_select_sql(args)
        (db, c) = _db_connect(args['connection_info'])
        c.execute(sql)
        data = c.fetchall()
        return json.dumps(data)
    except Exception, e:
        raise e
    #finally:
    #    _db_disconnect(db)


