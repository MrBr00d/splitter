import sqlite3

conn = sqlite3.connect("data/transaction.db")
cursor = conn.cursor()

# cursor.execute("INSERT INTO groups (group_name) VALUES ('test_group');")
# cursor.execute("INSERT INTO participants (participant_name, group_id) VALUES ('Nick', 1);")
# cursor.execute("INSERT INTO participants (participant_name, group_id) VALUES ('Bob', 1);")
# cursor.execute("INSERT INTO participants (participant_name, group_id, balance) VALUES ('Alice', 1, 20);")
# conn.commit()

cursor.execute('SELECT * FROM participants;')

# Fetch all the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)
conn.close()