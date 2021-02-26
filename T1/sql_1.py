import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Rohitasw@2002",
            database=db_name

        )
        print(f"Connection to MySQL DB {db_name} successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# connection = create_connection("localhost", "root", "")

connection = create_connection("localhost", "root", "", "sm_app")





def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# create_database_query = "CREATE DATABASE sm_app"
# create_database(connection, create_database_query)

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT, 
  name TEXT NOT NULL, 
  age INT, 
  gender TEXT, 
  nationality TEXT, 
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

# execute_query(connection, create_users_table)


create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
  id INT AUTO_INCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY fk_user_id (user_id) REFERENCES users(id), 
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

# execute_query(connection, create_posts_table)


create_users = """
INSERT INTO
  `users` (`name`, `age`, `gender`, `nationality`)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""

# execute_query(connection, create_users)  

# sql = "INSERT INTO likes ( user_id, post_id ) VALUES ( %s, %s )"
# val = [(4, 5), (3, 4)]

# cursor = connection.cursor()
# cursor.executemany(sql, val)
# connection.commit()


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)



for user in users:
    print(user)


update_post_description = """
UPDATE
  posts
SET
  description = "The weather has become pleasant now"
WHERE
  id = 2
"""

execute_query(connection,  update_post_description)

delete_comment = "DELETE FROM comments WHERE id = 2"
# execute_query(connection, delete_comment)

select_users1 = "Desc users"
users1 = execute_read_query(connection, select_users1)

for user in users1:
    print(user)