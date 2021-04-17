import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()

people = [
    ("Roald", "Amundsen", 5),
    ("Rosa", "Parks", 9),
    ("Henry", "Hudson", 5),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Bruhl", 3)
]

# c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    print("Inserting now")

# commit changes
conn.commit()
conn.close()