"""
calls validator
"""
from datastorex import mysql_dml
from datastorex import postgres_dml
from datastorex import mariadb_dml


MYSQL_ID = 'mysql'
POSTGRES_ID = 'postgres'
MARIADB_ID = 'mariadb'
SQLSERVER_ID = 'sqlserver'
ORACLE_ID = 'oracle'
MONGODB_ID = 'mongodb'
SQLITE_ID = 'sqlite'

SUPPORTED_DATASTORE_TYPES = [MYSQL_ID, POSTGRES_ID, MARIADB_ID]


def _validate_connection_info(args):
    try:
        if 'connection_info' not in args:
            raise Exception('connection info is mandatory')

        if not isinstance(args['connection_info'], dict):
            raise Exception('connection info should be a dictionary')

        if (args['connection_info'] is None or
                args['connection_info']['type'] is None or
                args['connection_info']['host'] is None or
                args['connection_info']['namespace'] is None or
                args['connection_info']['user'] is None or
                args['connection_info']['password'] is None or
                args['connection_info']['port'] is None):
            raise Exception('connection info details are missing')
    except Exception, err:
        raise err


def _validate_tablename(args):
    try:
        if args['tablename'] is None:
            raise Exception('tablename is mandatory')
    except Exception, err:
        raise err


def _validate_param_value(param_name, args):
    try:
        if param_name in args:
            if args[param_name] is None or args[param_name] == '':
                raise Exception('%s cannot be empty' % param_name)
            if not isinstance(args[param_name], int):
                if len(args[param_name]) == 0:
                    raise Exception('%s cannot be empty' % param_name)
    except Exception, err:
        raise err


def _validate_list_type_param(param_name, args):
    try:
        if param_name not in args:
            raise Exception('%s is mandatory' % param_name)

        if not isinstance(args[param_name], list):
            raise Exception('%s should be a list' % param_name)
    except Exception, err:
        raise err


def _validate_insert_param(args):
    try:
        _validate_connection_info(args)
        _validate_tablename(args)
        _validate_list_type_param('data_columns', args)
        _validate_list_type_param('values', args)
    except Exception, err:
        raise err


def _validate_update_param(args):
    try:
        _validate_connection_info(args)
        _validate_tablename(args)
        _validate_param_value('filter_columns', args)
        _validate_param_value('filter_values', args)
        _validate_list_type_param('set_columns', args)
        _validate_list_type_param('set_values', args)
    except Exception, err:
        raise err


def _validate_delete_param(args):
    try:
        _validate_connection_info(args)
        _validate_tablename(args)
        _validate_param_value('filter_columns', args)
        _validate_param_value('filter_values', args)
    except Exception, err:
        raise err


def _validate_select_param(args):
    try:
        _validate_connection_info(args)
        _validate_tablename(args)
        _validate_param_value('filter_columns', args)
        _validate_param_value('filter_values', args)
    except Exception, err:
        raise err


def process(method, param):
    """
    process method based upon params
    """
    try:
        if method == 'insert':
            _validate_insert_param(param)
        elif method == 'update':
            _validate_update_param(param)
        elif method == 'delete':
            _validate_delete_param(param)
        elif method == 'select':
            _validate_select_param(param)

        ds_type = param['connection_info']['type'].strip().lower()

        if ds_type not in SUPPORTED_DATASTORE_TYPES:
            raise Exception('Datastore type not supported')

        cmd = "%s_dml.%s(param)" % (ds_type, method)
        return eval(cmd)
    except Exception, err:
        raise err
