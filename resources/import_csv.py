import csv, sqlite3

#Connecting to sqlite
conn = sqlite3.connect('../sql_app.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS starbucks")
sql ='''
CREATE TABLE starbucks 
(id integer, 
starbucks_id VARCHAR(100),
name VARCHAR(100) , 
brand_name VARCHAR(100),
store_name,
phone_number VARCHAR(100),
ownership_time VARCHAR(100),
street1 VARCHAR(100),
street2 VARCHAR(100),
street3 VARCHAR(100),
city VARCHAR(100),
country_subdivision_code VARCHAR(100),
country_code VARCHAR(100),
postal_code VARCHAR(100),
longitude FLOAT,
latitude FLOAT,
timezone_offset VARCHAR(100),
timezone_id VARCHAR(100),
timezone_olsonid VARCHAR(100),
first_seen VARCHAR(100),
last_seen VARCHAR(100)
);'''
cursor.execute(sql)
print("Table created successfully........")

# Commit your changes in the database
conn.commit()

with open('stores.csv', 'r') as f: # `with` statement
    csvreader = csv.reader(f)
    to_db = []
    for idx, row in enumerate(csvreader):
        if idx > 0:
            pass
            to_db.append(row)

print(to_db)
cursor.executemany("""
            INSERT INTO starbucks (
            id, 
starbucks_id ,
name , 
brand_name,
store_name,
phone_number,
ownership_time ,
street1,
Street2,
Street3,
city,
country_subdivision_code,
country_code,
postal_code,
longitude,
latitude,
timezone_offset,
timezone_id ,
timezone_olsonid,
first_seen,
last_seen

            ) VALUES (""" + ("?," * 21)[0:-1]  + """);

            """, to_db)
conn.commit()
s = conn.execute("select * from starbucks").fetchall()
conn.close()
