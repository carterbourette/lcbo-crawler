#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Author      : Carter Bourette
# Description : ..
#               ...
#----------------------------------------------------------------------------
#
import mysql.connector

USERNAME = 'root'
USERPASS = 'sys'
DATABASE = 'beerlist'

class Database:

    def __init__(self, DBErrorHandler = None):
        self.conn = None
        self.cursor = None
        self.err = None
        self.is_error = False
        self.last_run = None
        self.error_handler = DBErrorHandler

    def __del__(self):
        self.close()

    # -------------------------------------------
    # Purpose: Connect to the MySQL database.
    # Passed-in: n/a.
    def connect(self):
        try:
            # TODO: Review auth_plugin parmams for PROD dbs
            self.conn = mysql.connector.connect(user=USERNAME, password=USERPASS, database=DATABASE, auth_plugin='mysql_native_password')
        except mysql.connector.Error as err:
            self._error_handler(err)

    # -------------------------------------------
    # Purpose: Purpose.
    # Passed-in: Passed-in.
    def commit(self):
        try:
            self.conn.commit()
        except Exception as err:
            self.conn.rollback()
            self._error_handler()

    # -------------------------------------------
    # Purpose: start a mysql transaction.
    # Passed-in: n/a.
    def begin_transaction(self, internal=False):
        self.is_error = False
        if self.conn == None:
            self.connect()

        # Connection options - set autocommit
        if internal: self.conn.autocommit = True
        else:        self.conn.autocommit = False

        try:
            self.cursor = self.conn.cursor(dictionary=True)
        except Exception as err:
            self._error_handler(err)


    # -------------------------------------------
    # Purpose: end the mysql transaction.
    # Passed-in: n/a.
    def end_transaction(self):
        self.commit()
        self.cursor.close()
        self.cursor = None


    # -------------------------------------------
    # Purpose: Run an sql query.
    # Passed-in: query statement and any arguments.
    def query(self, query, args = ()):
        self.is_error = False
        # NOTE: this is to get rid of the nasty one item issue w/Python
        # see: https://stackoverflow.com/questions/7992559/what-is-the-syntax-rule-for-having-trailing-commas-in-tuple-definitions
        if type(args) is not tuple: args = (args,)

        # Check to see if we are in a transaction
        if self.cursor is None: self.begin_transaction(True)
        try:
            # Execute the given sql
            if args is ():
                self.last_run = query
                self.cursor.execute(query)
            else:
                self.last_run = query % args
                self.cursor.execute(query, args)
        except Exception as err:
            self.conn.rollback()
            self._error_handler(err)


    # -------------------------------------------
    # Purpose: Get all of the requested results.
    # Passed-in: n/a.
    def fetch_results(self):
        try:
            return self.cursor.fetchall()
        except mysql.connector.InterfaceError as err:
            return []

    # -------------------------------------------
    # Purpose: Get all of the requested results.
    # Passed-in: n/a.
    def fetch_all(self):
        try:
            return self.cursor.fetchall()
        except mysql.connector.InterfaceError as err:
            return []

    # -------------------------------------------
    # Purpose: Get one of the requested results.
    # Passed-in: n/a.
    def fetch_one(self):
        return self.cursor.fetchone()

    # -------------------------------------------
    # Purpose: Get one of the requested results.
    # Passed-in: n/a.
    def fetch_result(self):
        return self.cursor.fetchone()

    # -------------------------------------------
    # Purpose: Check to see if an error occured.
    # Passed-in: n/a.
    def error(self):
        return self.is_error

    # -------------------------------------------
    # Purpose: Return what went wrong.
    # Passed-in: n/a.
    def read_error(self):
        return self.err

    # -------------------------------------------
    # Purpose: Close the database connection.
    # Passed-in: n/a.
    def close(self):
        if self.conn is not None:
            try:    self.conn.close()
            except: pass

    # -------------------------------------------
    # Purpose: Set internal error flags and utilize custom error handler if available.
    # Passed-in: The error msg as defined by an exception.
    def _error_handler(self, err):
        self.err = err
        self.is_error = True
        if self.error_handler is not None: self.error_handler.handle(self)


class DBExplodeOnError:

    def handle(self, instance):
        print('Error:')
        print(instance.read_error())
        print('Query:')
        print(instance.last_run)
        exit(1)
