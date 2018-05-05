import datastorex
import MySQLdb
import pytest

def test_t1():
    with pytest.raises(Exception) as e:
        datastorex.insert()

def test_t2():
    with pytest.raises(Exception) as e:
        args = ''
        datastorex.insert(args)

def test_t3():
    with pytest.raises(Exception) as e:
        args = {}
        datastorex.insert(args)

def test_t4():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {}}
        datastorex.insert(args)

def test_t5():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"tablename": "yoooo"}}
        datastorex.insert(args)

def test_t6():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql"}}
        datastorex.insert(args)

def test_t7():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234"}}
        datastorex.insert(args)

def test_t8():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234"}, "tablename": "yoooo"}
        datastorex.insert(args)

def test_t9():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234"}, "tablename": "yoooo", "data_columns": ["attr9","attr1"]}
        datastorex.insert(args)

def test_t10():
    with pytest.raises(Exception) as e:
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "freedata", "user": "blah", "password": "blah blah", "port": "1234"}, "tablename": "yoooo", "data_columns": '', "values": ''}
        datastorex.insert(args)

def test_t11():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306}, "tablename": "yoooo", "data_columns": ["attr9","attr1"], "values": ["blah","blah"]}
    datastorex.insert(args)

def test_t12():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306}, "tablename": "test_all_datatypes", "data_columns": ["is_active","dob","dob_tz","name","id","height"], "values": [True,"2016-02-09","2016-02-15","ABC",23,15.678]}
    datastorex.insert(args)

def test_t13():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306}, "tablename": "test_all_datatypes", "data_columns": ["is_active","dob","dob_tz","name","id","height"], "values": [False,"2016-02-09","2016-02-15","abcdefghijklmnop###22323dsfsfs3423423433Zee",100000008,23232315.989]}
    datastorex.insert(args)

def test_t14():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306}, "tablename": "test_all_datatypes", "data_columns": ["is_active","dob","dob_tz","name","id","height"], "values": [False,"2016-02-09 23:59:59","2016-02-15 23:59:59","abcdefghijklmnop###22323dsfsfs3423423433Zee",100000008,23232315.989]}
    datastorex.insert(args)

def test_t15():
    with open('Deadpool_poster.jpg', 'rb') as f:
        photo = f.read()
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306}, "tablename": "test_all_datatypes", "data_columns": ["is_active","some_binary"], "values": [False, photo]}
        datastorex.insert(args)

def test_t16():
    with open('Deadpool_poster.jpg', 'rb') as f:
        photo = f.read()
        args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306}, "tablename": "test_all_datatypes", "data_columns": ["some_binary", "is_active","dob","dob_tz","name","id","height"], "values": [photo, False,"2016-02-09 23:59:59","2016-02-15 23:59:59","abcdefghijklmnop###22323dsfsfs3423423433Zee",100000008,23232315.989]}
        datastorex.insert(args)

def test_t17():
    args = {'connection_info': {"type": "mysql", "host": "localhost", "namespace": "testtest", "user": "testtest", "password": "testtest", "port": 3306}, "tablename": "test_all_datatypes", "data_columns": ["some_geo", "is_active","dob","dob_tz","name","id","height"], "values": [ST_GeomFromText('POINT(1 1)'), False,"2016-02-09 23:59:59","2016-02-15 23:59:59","abcdefghijklmnop###22323dsfsfs3423423433Zee",100000008,23232315.989]}
    datastorex.insert(args)

