# SQL, Models and Migrations
SQL: Database language
Models: PYthon interact with database through "data type" called  models
Migrations: Update the database responding to changes made.

## Data
### Data management systems
- MySQL
- PostgreSQL
- SQLite: Small implementation of SQL
- ..
One might have different use cases.

### Types of data
Each DMS has different types of data
SQLite:
- TEXT
- NUMERIC
- INTEGER
- REAL
- BLOB: Binary large object
MySQL:
- CHAR(size): If you happen to know the `size` then you can save storage.
- VARCHAR(size): variable-sized, up to `size`
- SMALLINT
- INT
- BIGINT
- FLOAT
- And much more.

### Operations
Create table:
```sql
 CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL, 
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL,
```
`NOT NULL` is a constraint for a field. Data must be valid before adding to the database.

Insert
```sql 
INSERT INTO flights
    (origin, destination, duration)
    VALUES ("New York", "London", "90")
```

Select
```sql
SELECT * FROM flights
```
```sql
SELECT origin, destination FROM flights
```
```sql
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE destination LIKE "%N%";
SELECT * FROM flights WHERE destination="SGN";
SELECT * FROM flights where duration > 80;
```
Update
```sql
UPDATE flights
    SET duration = 220
    WHERE destination LIKE "%N%";
```
Delete
```sql
DELETE FROM flights
    WHERE origin="New York"
```
Other Clauses:
- LIMIT
- ORDER BY
- GROUP BY
- HAVING
- ...
-> Django will handle these kind of operations.

### Working with SQLite prompt
```
.mode columns
.headers yes
```
