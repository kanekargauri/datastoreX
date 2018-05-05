import datastorex
import pytest

def test_t1():
    with pytest.raises(Exception) as e:
        datastorex.delete()

def test_t2():
    with pytest.raises(Exception) as e:
        args = ''
        datastorex.delete(args)

def test_t3():
    with pytest.raises(Exception) as e:
        args = {}
        datastorex.delete(args)

def test_t4():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {}}
        datastorex.delete(args)

def test_t5():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"tablename": "yoooo"}}
        datastorex.delete(args)

def test_t6():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql"}}
        datastorex.delete(args)

def test_t7():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234"}}
        datastorex.delete(args)

def test_t8():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "xxxxx", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234"},"tablename": "ohhlala"}
        datastorex.delete(args)

def test_t9():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "sqlite", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234"},"tablename": "ohhlala"}
        datastorex.delete(args)

def test_t10():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "ohhlala"}
        datastorex.delete(args)

def test_t11():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "yoooo"}
    datastorex.delete(args)

def test_t12():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes", "filter": [{"operand": "id", "operator": "=", "value": 23}]}
    assert None == datastorex.delete(args)

def test_t13():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306},"tablename": "test_all_datatypes", "filter": [{"operand": "id", "operator": "!=", "value": 23}, {"operand": "is_active", "operator": "=", "value": True}]}
    datastorex.delete(args)


