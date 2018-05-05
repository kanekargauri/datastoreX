import datastorex
import pytest

def test_t1():
    with pytest.raises(Exception) as e:
        datastorex.select()

def test_t2():
    with pytest.raises(Exception) as e:
        args = ''
        datastorex.select(args)

def test_t3():
    with pytest.raises(Exception) as e:
        args = {}
        datastorex.select(args)

def test_t4():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {}}
        datastorex.select(args)

def test_t5():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"tablename": "yoooo"}}
        datastorex.select(args)

def test_t6():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql"}}
        datastorex.select(args)

def test_t7():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234"}}
        datastorex.select(args)

def test_t8():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "xxxxx", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234"},"tablename": "ohhlala"}
        datastorex.select(args)

def test_t9():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "sqlite", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234"},"tablename": "ohhlala"}
        datastorex.select(args)

def test_t10():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "ohhlala"}
        datastorex.select(args)

def test_t11():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "yoooo"}
    datastorex.select(args)

def test_t12():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "yoooo","select_fields": [ "attr2" ], "limit": "2"}
        datastorex.select(args)

def test_t13():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "yoooo","select_fields": [ "attr1" ], "limit": "2"}
    datastorex.select(args)

def test_t14():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "yoooo","select_fields": [ "attr1", "ATTR9" ], "limit": "2"}
    datastorex.select(args)

def test_t15():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "yoooo","select_fields": [ "aTTr9", "Attr1" ], "limit": "2"}
    datastorex.select(args)

def test_t16():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "", "" ], "limit": "2"}
        datastorex.select(args)

def test_t17():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name", "height", "is_active"], "limit" : "10"}
    datastorex.select(args)

def test_t18():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "dob"], "limit" : "10"}
    datastorex.select(args)

def test_t19():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "dob_tz"], "limit" : "10"}
    datastorex.select(args)

def test_t20():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name", "height", "is_active", "dob", "dob_tz"], "limit" : "2"}
    datastorex.select(args)

def test_t21():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name", "height", "is_active", "dob", "dob_tz"], "limit": "5", "offset": "20", "order_by": "id"}
    datastorex.select(args)

def test_t22():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name", "height", "is_active", "dob", "dob_tz"], "limit": "5", "offset": "20", "order_by": "id desc"}
    datastorex.select(args)

def test_t23():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "is_active", "operator": "=", "value": True }]}
    datastorex.select(args)

def test_t24():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "is_active", "operator": "!=", "value": True }]}
    datastorex.select(args)

def test_t25():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "is_active", "operator": "in", "value": [True, True] }]}
    datastorex.select(args)

def test_t26():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "is_active", "operator": "not in", "value": [True, True] }]}
    datastorex.select(args)

def test_t27():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "height", "operator": "=", "value": 10.23 }]}
    datastorex.select(args)

def test_t28():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "height", "operator": "!=", "value": 10.23 }]}
    datastorex.select(args)

def test_t29():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "height", "operator": "<", "value": 10.23 }]}
    datastorex.select(args)

def test_t30():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "height", "operator": "<=", "value": 10.23 }]}
    datastorex.select(args)

def test_t31():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "height", "operator": ">", "value": 10.23 }]}
    datastorex.select(args)

def test_t32():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "height", "operator": ">=", "value": 10.23 }]}
    datastorex.select(args)

def test_t33():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "height", "operator": "between", "value": [10.23,10.55] }]}
    datastorex.select(args)

def test_t34():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "height", "operator": "between", "value": [10.23,11] }]}
    datastorex.select(args)

def test_t35():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "height", "operator": "in", "value": [10.23,11,12.45,1,-89] }]}
    datastorex.select(args)

def test_t36():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "height", "operator": "not in", "value": [10.23,11,12.45,1,-89] }]}
    datastorex.select(args)

def test_t37():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "id", "operator": "=", "value": 10.23 }]}
    datastorex.select(args)

def test_t38():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "id", "operator": "!=", "value": 10.23 }]}
    datastorex.select(args)

def test_t39():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "id", "operator": ">", "value": 10.23 }]}
    datastorex.select(args)

def test_t40():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "id", "operator": ">=", "value": 10.23 }]}
    datastorex.select(args)

def test_t41():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "id", "operator": "<", "value": 10.23 }]}
    datastorex.select(args)

def test_t42():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "id", "operator": "<=", "value": 10.23 }]}
    datastorex.select(args)

def test_t43():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "id", "operator": "between", "value": [10,20] }]}
    datastorex.select(args)

def test_t44():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "id", "operator": "in", "value": [10,20] }]}
    datastorex.select(args)

def test_t45():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "id", "operator": "not in", "value": [10,20] }]}
    datastorex.select(args)

def test_t46():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "id", "operator": ">", "value": 10 }, { "operand": "is_active", "operator": "=", "value": True }]}
    datastorex.select(args)

def test_t47():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "name", "operator": "=", "value": "Yoooo" }]}
    datastorex.select(args)

def test_t48():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "name", "operator": "!=", "value": "Yooo" }]}
    datastorex.select(args)

def test_t49():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "name", "operator": "<", "value": "Yooo" }]}
    datastorex.select(args)

def test_t50():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "name", "operator": "<=", "value": "Yooo" }]}
    datastorex.select(args)

def test_t51():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "name", "operator": ">", "value": "Yooo" }]}
    datastorex.select(args)

def test_t52():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "name", "operator": ">=", "value": "Yooo" }]}
    datastorex.select(args)

def test_t53():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "name", "operator": "between", "value": ["A","B"] }]}
    datastorex.select(args)

def test_t54():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "name", "operator": "in", "value": ["A","B"] }]}
    datastorex.select(args)

def test_t55():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "name", "operator": "not in", "value": ["A","B"] }]}
    datastorex.select(args)

def test_t56():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name", "dob"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "dob", "operator": "=", "value": "2016-01-02" }]}
    datastorex.select(args)

def test_t57():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name", "dob"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "dob", "operator": "!=", "value": "2016-02-09 23:59:59" }]}
    datastorex.select(args)

def test_t58():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name", "dob"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "dob", "operator": "<", "value": "2016-02-09 23:59:59" }]}
    datastorex.select(args)

def test_t59():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name", "dob"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "dob", "operator": "<=", "value": "2016-02-09 23:59:59" }]}
    datastorex.select(args)

def test_t60():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name", "dob"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "dob", "operator": ">", "value": "2016-02-09 23:59:59" }]}
    datastorex.select(args)

def test_t61():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name", "dob"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "dob", "operator": ">=", "value": "2016-02-09 23:59:59" }]}
    datastorex.select(args)

def test_t62():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name", "dob"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "dob", "operator": "between", "value": ["2016-02-01", "2016-02-09 23:59:59"] }]}
    datastorex.select(args)

def test_t63():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name", "dob"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "dob", "operator": "in", "value": ["2016-02-01", "2016-02-09 23:59:59"] }]}
    datastorex.select(args)

def test_t64():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes","select_fields": [ "id", "name", "dob"], "limit": "5", "offset": "20", "order_by": "id", "filter": [{ "operand": "dob", "operator": "not in", "value": ["2016-02-01", "2016-02-09 23:59:59"] }]}
    datastorex.select(args)

def test_t65():
    args = {'order_by': '', 'connection_info': {'namespace': 'testtest', 'host': 'localhost', 'user': 'testtest', 'password': 'testtest', 'type': 'mysql', 'port': '3306'}, 'tablename': 'category', 'filter': [], 'limit': '', 'offset': '', 'select_fields': []}
    datastorex.select(args)
