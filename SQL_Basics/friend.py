import sqlite3

connection = sqlite3.connect("my_friends.db")
#create cursur
c = connection.cursor()

people = [
    ("Ronaldo","Messi",5),
    ("dimaria","Messi",10),
    ("mbappe","Ronaldo",10),
    ("Ronaldo","dybala",7),
    ("Henry","Messi",4),
]

# for person in people:
#     c.execute("INSERT INTO friends VALUES (?,?,?)",person)
#     print("INSERTING NOW!")

average = 0 
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)",person)
    average += person[2]
print(average/len(people))

# commit changes
connection.commit()
connection.close()