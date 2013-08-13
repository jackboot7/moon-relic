#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlite3 import dbapi2 as s

TEMPLATE = \
"""<!DOCTYPE html>
<html>
  <head>
    <title>%s</title>
  </head>
  <body>
    <h1>%s</h1>
    <hr>
    <p>%s</p>
  </body>
</html>"""

def getData():
    print("1. getting data")    
    conn = s.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM languages")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


def saveTemplate(data):
    print ("2. saving templates")
    for i in data:
        name = "output/nr_" + ("%s" % i[0]) + ".html"
        f = open(name, 'w')
        f.write(TEMPLATE % i)
        f.close()
        print("2.%s saved file for %s" % (i[0], i[1]))