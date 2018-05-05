import datastorex
import datetime
import pytest

def test_t1():
    with pytest.raises(Exception) as e:
        datastorex.update()

def test_t2():
    with pytest.raises(Exception) as e:
        args = ''
        datastorex.update(args)

def test_t3():
    with pytest.raises(Exception) as e:
        args = {}
        datastorex.update(args)

def test_t4():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {}}
        datastorex.update(args)

def test_t5():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"tablename": "yoooo"}}
        datastorex.update(args)

def test_t6():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql"}}
        datastorex.update(args)

def test_t7():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234"}}
        datastorex.update(args)

def test_t8():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "xxxxx", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234"},"tablename": "ohhlala"}
        datastorex.update(args)

def test_t9():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "sqlite", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234"},"tablename": "ohhlala"}
        datastorex.update(args)

def test_t10():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "ohhlala"}
        datastorex.update(args)

def test_t11():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "yoooo"}
        datastorex.update(args)

def test_t12():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "yoooo","set_columns": [ "attr2" ]}
        datastorex.update(args)

def test_t13():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "yoooo","set_columns": [ "attr1" ], "set_values": ["hello world %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]}
        datastorex.update(args)

def test_t14():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "yoooo","set_columns": [ "attr1", "ATTR9" ], "set_values": ["hello world %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "blah %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]}
        datastorex.update(args)

def test_t15():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "yoooo","set_columns": [ "aTTr9", "Attr1" ], "set_values": ["hello world %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "blah %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]}
        datastorex.update(args)

def test_t16():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","set_columns": [ "", "" ]}
        datastorex.update(args)

def test_t17():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","set_columns": [ "name" ], "set_values": ["hello world %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")], "filter": [{"operand": "id", "operator": "=", "value": 23}]}
    datastorex.update(args)

def test_t18():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","set_columns": [ "name" ], "set_values": ["hello world %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")], "filter": [{"operand": "id", "operator": "!=", "value": 23}]}
    datastorex.update(args)

def test_t19():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "dob_tz"], "limit" : "10"}
        datastorex.update(args)
    
def test_t20():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name", "height", "is_active", "dob", "dob_tz"], "limit" : "2"}
        datastorex.update(args)

def test_t21():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name", "height", "is_active", "dob", "dob_tz"], "limit": "5", "offset": 20, "order_by": "id"}
        datastorex.update(args)

def test_t22():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name", "height", "is_active", "dob", "dob_tz"], "limit": "5", "offset": 20, "order_by": "id desc"}
        datastorex.update(args)

def test_t23():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "is_active", "operator": "=", "value": True }]}
        datastorex.update(args)

def test_t24():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "is_active", "operator": "!=", "value": True }]}
        datastorex.update(args)

def test_t25():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "is_active", "operator": "in", "value": [True, True] }]}
        datastorex.update(args)

def test_t26():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "is_active", "operator": "not in", "value": [True, True] }]}
        datastorex.update(args)

def test_t27():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "height", "operator": "=", "value": 10.23 }]}
        datastorex.update(args)

def test_t28():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "height", "operator": "!=", "value": 10.23 }]}
        datastorex.update(args)

def test_t29():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "height", "operator": "<", "value": 10.23 }]}
        datastorex.update(args)

def test_t30():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "height", "operator": "<=", "value": 10.23 }]}
        datastorex.update(args)

def test_t31():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "height", "operator": ">", "value": 10.23 }]}
        datastorex.update(args)

def test_t32():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "height", "operator": ">=", "value": 10.23 }]}
        datastorex.update(args)

def test_t33():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "height", "operator": "between", "value": [10.23,10.55] }]}
        datastorex.update(args)

def test_t34():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "height", "operator": "between", "value": [10.23,11] }]}
        datastorex.update(args)

def test_t35():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "height", "operator": "in", "value": [10.23,11,12.45,1,-89] }]}
        datastorex.update(args)

def test_t36():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "height", "operator": "not in", "value": [10.23,11,12.45,1,-89] }]}
        datastorex.update(args)

def test_t37():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "id", "operator": "=", "value": 10.23 }]}
        datastorex.update(args)

def test_t38():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "id", "operator": "!=", "value": 10.23 }]}
        datastorex.update(args)

def test_t39():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "id", "operator": ">", "value": 10.23 }]}
        datastorex.update(args)

def test_t40():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "id", "operator": ">=", "value": 10.23 }]}
        datastorex.update(args)

def test_t41():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "id", "operator": "<", "value": 10.23 }]}
        datastorex.update(args)

def test_t42():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "id", "operator": "<=", "value": 10.23 }]}
        datastorex.update(args)

def test_t43():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "id", "operator": "between", "value": [10,20] }]}
        datastorex.update(args)

def test_t44():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "id", "operator": "in", "value": [10,20] }]}
        datastorex.update(args)

def test_t45():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "id", "operator": "not in", "value": [10,20] }]}
        datastorex.update(args)

def test_t46():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "id", "operator": ">", "value": 10 }, { "operand": "is_active", "operator": "=", "value": True }]}
        datastorex.update(args)

def test_t47():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "name", "operator": "=", "value": "Yoooo" }]}
        datastorex.update(args)

def test_t48():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "name", "operator": "!=", "value": "Yooo" }]}
        datastorex.update(args)

def test_t49():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "name", "operator": "<", "value": "Yooo" }]}
        datastorex.update(args)

def test_t50():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "name", "operator": "<=", "value": "Yooo" }]}
        datastorex.update(args)

def test_t51():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "name", "operator": ">", "value": "Yooo" }]}
        datastorex.update(args)

def test_t52():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "name", "operator": ">=", "value": "Yooo" }]}
        datastorex.update(args)

def test_t53():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "name", "operator": "between", "value": ["A","B"] }]}
        datastorex.update(args)

def test_t54():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "name", "operator": "in", "value": ["A","B"] }]}
        datastorex.update(args)

def test_t55():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "name", "operator": "not in", "value": ["A","B"] }]}
        datastorex.update(args)

def test_t56():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name", "dob"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "dob", "operator": "=", "value": "2016-01-02" }]}
        datastorex.update(args)

def test_t57():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name", "dob"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "dob", "operator": "!=", "value": "2016-02-09 23:59:59" }]}
        datastorex.update(args)

def test_t58():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name", "dob"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "dob", "operator": "<", "value": "2016-02-09 23:59:59" }]}
        datastorex.update(args)

def test_t59():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name", "dob"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "dob", "operator": "<=", "value": "2016-02-09 23:59:59" }]}
        datastorex.update(args)

def test_t60():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name", "dob"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "dob", "operator": ">", "value": "2016-02-09 23:59:59" }]}
        datastorex.update(args)

def test_t61():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name", "dob"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "dob", "operator": ">=", "value": "2016-02-09 23:59:59" }]}
        datastorex.update(args)

def test_t62():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name", "dob"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "dob", "operator": "between", "value": ["2016-02-01", "2016-02-09 23:59:59"] }]}
        datastorex.update(args)

def test_t63():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name", "dob"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "dob", "operator": "in", "value": ["2016-02-01", "2016-02-09 23:59:59"] }]}
        datastorex.update(args)

def test_t64():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","update_fields": [ "id", "name", "dob"], "limit": "5", "offset": 20, "order_by": "id", "filter": [{ "operand": "dob", "operator": "not in", "value": ["2016-02-01", "2016-02-09 23:59:59"] }]}
        datastorex.update(args)

