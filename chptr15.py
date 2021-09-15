# Databases

# Basic SQL commands

# Craetes table called 'Users' with columns name (text) and email (text)
# CREATE TABLE "Users" ("name" TEXT, "email" TEXT)
# VARCHAR(128) is characters up to 128 long
# CREATE TABLE "Users" ("name" VARCHAR(128), "email" VARCHAR(128))

# Adding information into the TABLE
# INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu')

# Delete information
# DELETE FROM Users WHERE email='ted@umich.edu'

# Update information
# UPDATE Users SET name="Charles" WHERE email='csev@umich.edu'

# Selecting data from the TABLE, * - all data
# SELECT * FROM Users
# SELECT * FROM Users WHERE email='csev@umich.edu'
# SELECT * FROM Users ORDER BY email
# SELECT * FROM Users ORDER BY name DESC

# SQL and Python

# import sqlite3
#
# # Opening database reqires two steps: connect and cursor
# # The connect operation makes a “connection” to the database stored in the
# # file emaildb.sqlite in the current directory.
# # If the file does not exist, it will be created.
# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor() # Similar to the open command with files
#
# # DROP TABLE command deletes the table and all of its contents from the database
# cur.execute('DROP TABLE IF EXISTS Counts')
#
# cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')
#
# fname = input('Enter file name:')
# if (len(fname) < 1): fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     email = pieces[1]
#     cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
#     # ? is a placeholder which is replaced by the touple (email,)
#     row = cur.fetchone()
#     if row is None:
#         cur.execute(''' INSERT INTO Counts (email, count)
#         VALUES (?,1)''',(email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
#         (email,))
#     conn.commit()
#
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
#
# for row in cur.execute(sqlstr):
#     print(str(row[0]),row[1])

# Assignment

# import sqlite3
# import re
#
# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()
# cur.execute('DROP TABLE IF EXISTS Counts')
#
# cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
#
#
# fname = input('Enter file name:')
# if (len(fname) < 1): fname = 'mbox.txt'
# fh = open(fname)
#
# for line in fh:
#     if not line.startswith('From: '): continue
#     x = re.search('\S+@+([A-z]+)',line)
#     # x = re.search('\S+@+(\S+)',line)
#     org = x.group(1)
#     # pieces = line.split('@')
#     # email = pieces[1]
#     # org = email
#     cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute(''' INSERT INTO Counts (org, count)
#         VALUES (?,1)''',(org,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
#         (org,))
# conn.commit()
#
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
#
# for row in cur.execute(sqlstr):
#     print(str(row[0]),row[1])


for integer in (-1,3,5):
    if integer < 0:
    	print("negative")
    else:
    	print("non-negative")
