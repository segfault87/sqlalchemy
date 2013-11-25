# mysql/umysqldb.py
# Copyright (C) 2005-2013 the SQLAlchemy authors and contributors <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""

.. dialect:: mysql+umysqldb
    :name: umysqldb 
    :dbapi: umysqldb
    :connectstring: mysql+umysqldb://<user>:<password>@<host>[:<port>]/<dbname>
    :url: http://sourceforge.net/projects/mysql-python


An identical dialect to mysqldb except for using umysqldb as backend instead of MySQLdb.

"""

from .base import (MySQLDialect, MySQLExecutionContext,
                                            MySQLCompiler, MySQLIdentifierPreparer)
from ...connectors.mysqldb import (
                        MySQLDBExecutionContext,
                        MySQLDBCompiler,
                        MySQLDBIdentifierPreparer,
                        MySQLDBConnector
                    )


class MySQLExecutionContext_mysqldb(MySQLDBExecutionContext, MySQLExecutionContext):
    pass


class MySQLCompiler_mysqldb(MySQLDBCompiler, MySQLCompiler):
    pass


class MySQLIdentifierPreparer_mysqldb(MySQLDBIdentifierPreparer, MySQLIdentifierPreparer):
    pass


class MySQLDialect_umysqldb(MySQLDBConnector, MySQLDialect):
    driver = 'umysqldb'
    execution_ctx_cls = MySQLExecutionContext_mysqldb
    statement_compiler = MySQLCompiler_mysqldb
    preparer = MySQLIdentifierPreparer_mysqldb

    @classmethod
    def dbapi(cls):
        return __import__('umysqldb')

dialect = MySQLDialect_umysqldb
