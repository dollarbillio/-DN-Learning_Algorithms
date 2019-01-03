## Basics
* ```.quit```: quit sql
* ```sqlite3 test.db```: Create new data base:
* ```.headers on/off```: show headers
* ```CREATE TABLE contacts(name text, phone integer, email text);```: create a table name contact with <data_name, data_type>
* ```INSERT INTO contacts (name, phone, email) values('Tim', 8787878, 'tim@email.com');```: insert instance
* ```INSERT INTO contacts values('Tim', 8787878, "@email);```: quick add 
* ```INSERT INTO contacts (name, phone) values('Tim', 8787878);```: insert without email
* ```SELECT col1, col2 FROM table```: select many columns
* ```SELECT * FROM contacts;```: select all from contacts
* ```SELECT email FROM contacts;```: select 'email' column only
* ```SELECT * FROM contacts WHERE name="DUNG";```: select a single entry
* ```SELECT DISTINCT col FROM table```: select distinct values
* ```SELECT COUNT(*) FROM table```: number of rows in table
* ```SELECT COUNT(birthday) FROM table```: count how many non-missing entries in ```birthday``` column
* ```SELECT COUNT (DISTINCT birthday) FROM table```: count how many non-missing distinct entries in ```birthday``` column
---
### Select with filters
* ```SELECT title FROM films WHERE title = 'Metropolis';```: select ```title``` column where ```title``` = smth
* ```= equal, <> not equal, < less than, > greater than, <= less than or equal to, >= greater than or equal to```
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
