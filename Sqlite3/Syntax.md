## Basics
* ```.quit```: quit sql
* ```sqlite3 test.db```: Create new data base:
* ```.headers on/off```: show headers
* ```CREATE TABLE contacts(name text, phone integer, email text);```: create a table name contact with <data_name, data_type>
* ```INSERT INTO contacts (name, phone, email) values('Tim', 8787878, 'tim@email.com');```: insert instance
* ```INSERT INTO contacts values('Tim', 8787878, "@email);```: quick add 
* ```INSERT INTO contacts (name, phone) values('Tim', 8787878);```: insert without email
* ```SELECT * FROM contacts;```: select all from contacts
* ```SELECT email FROM contacts;```: select 'email' column only
* ```SELECT * FROM contacts WHERE name="DUNG";```: select a single entry
---
## Modifying tables
* ```.backup newdatabackup```: back up the file.db to newdatabackup
* ```.restore newdatabackup```: restore
* ```UPDATE contacts SET email="@noob";```: set all email to '@noob'
* ```UPDATE contacts SET email="@noob" WHERE name="Lae"```: change email of "Lae" to "@noob"
* ```DELETE FROM contacts WHERE phone=917672282;```: delete a specified entry
---
## Listing
* ```.tables```: show all available tables in the file
* ```.schema [table_name]```: column structure of all/table_name
* ```.dump```: Historical steps of creating a table
