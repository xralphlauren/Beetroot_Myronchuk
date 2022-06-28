import sqlite3


con = sqlite3.connect('example.db')
cur = con.cursor()                  # курсор нужен для того, чтоб не обращаться с каждым запросом к БД,
                                    # а в курсоре накопить несколько запросов и потом через коннект залить данные к БД

# Create table
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()


con.close()