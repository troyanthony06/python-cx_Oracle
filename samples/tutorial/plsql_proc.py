#------------------------------------------------------------------------------
# plsql_proc.py (Section 5.2)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright (c) 2017, 2020, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

import cx_Oracle
import db_config

con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
cur = con.cursor()

myvar = cur.var(int)
cur.callproc('myproc', (123, myvar))
print(myvar.getvalue())
