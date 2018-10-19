* ```.quit```: quit sql
* ```sqlite3 test.db```: Create new data base:
* ```.headers on/off```: show headers
* ```create table contacts(name text, phone integer, email text);```: create a table name contact with <data_name, data_type>
* ```insert into contacts (name, phone, email) values('Tim', 8787878, 'tim@email.com');```: insert instance
* ```insert into contacts values('Tim', 8787878, "@email);```: quick add 
* ```insert into contacts (name, phone) values('Tim', 8787878);```: insert without email
* ```SELECT * FROM contacts;```: select all from contacts
* ```SELECT email FROM contacts;```: select 'email' column only
