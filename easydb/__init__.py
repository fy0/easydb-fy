import os
import sqlite3

class EasyDB:
    #conn = sqlite3.Connection
    def __init__(self, filename, schema = None, **kwargs):
        if not (os.path.exists(filename) or schema):
            raise Exception, "The specified database file does not exist, and you haven't provided a schema"
        self.conn = sqlite3.connect(filename)
        if schema:
            for table_name, fields in schema.items():
                query = u"CREATE TABLE %s (%s)" % (table_name, ", ".join(fields))
                self.query(query)
            self.conn.commit()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def query(self, *args, **kwargs):
        cursor = self.conn.cursor()
        result = cursor.execute(*args, **kwargs)
        ret = result.fetchall()
        if ret:return ret[0]
        return ret

    def commit(self):
        self.conn.commit()

