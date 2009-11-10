import sys
import pyiidbi

conn = pyiidbi.connect(database='test')
cur  = conn.cursor()
cur.execute("select * from iitables")
print cur.fetchall()
cur.close()
conn.rollback()
