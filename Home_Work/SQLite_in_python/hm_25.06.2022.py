import sqlite3


con = sqlite3.connect('wh.db')
cur = con.cursor()

task1 = cur.execute("SELECT (sum(salary)/count(salary)) FROM sotr;").fetchall()
task2 = cur.execute("SELECT name, salary FROM sotr ORDER BY salary DESC, name LIMIT 10;").fetchall()
task3 = cur.execute("SELECT count() FROM sotr WHERE status = 'Detailee';").fetchall()
task4 = cur.execute("SELECT count() FROM sotr WHERE position_title = 'STAFF ASSISTANT';").fetchall()
task5 = cur.execute("SELECT (sum(salary)/count()) FROM sotr WHERE position_title = 'STAFF ASSISTANT';").fetchall()
task6 = cur.execute("SELECT position_title FROM sotr GROUP BY position_title;").fetchall()
task7 = cur.execute("SELECT count(position_title), position_title FROM sotr GROUP BY position_title;").fetchall()

con.close()


