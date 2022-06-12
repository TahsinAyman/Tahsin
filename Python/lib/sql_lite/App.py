import sqlite3

with sqlite3.connect("databases\\db.sqlite3") as db:
    sql = db.cursor()
    
    input_data = [
        input("Enter User: "),
        input("Enter Password: "),
        input("Change User: "),
        input("Change Password: ")
    ]

    sql.execute("""
    UPDATE authentication 
    SET user = ?, password = ?
    WHERE user = ? AND password = ?
    """, [input_data[2], input_data[3], input_data[0], input_data[1]]
    )    
 
    db.commit()

