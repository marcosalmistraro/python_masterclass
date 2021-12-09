import sqlite3

# This simple script enters user-defined values in a new sqlite3 database
# The contacts are then displayed once the data-entry step is over


def db_display(query: str):
    cursor = db.cursor()
    cursor.execute(query)
    for contact in cursor.fetchall():
        print(contact)
    cursor.close()


db = sqlite3.connect("contacts.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS "
           "contacts(name TEXT, phone INTEGER, email TEXT)")

while True:
    prompt = input("Please enter the details of the contact "
                   "you wish to add to the database. "
                   "Enter to continue. "
                   "Q to quit the data-entry step.")

    if prompt == "q".casefold():
        break
    input_name = input("Enter the contact's name ")
    input_phone = int(input("Enter a phone number "))
    input_mail = input("Enter a mail address ")

    db.execute("INSERT INTO contacts "
               "VALUES ('{}', {}, '{}')".format(input_name, input_phone, input_mail))

while True:
    prompt_query = input("Enter a SQL query. "
                         "Q to quit the program.")
    if prompt_query == "q".casefold():
        break
    db_display(prompt_query)


db.commit()
db.close()
