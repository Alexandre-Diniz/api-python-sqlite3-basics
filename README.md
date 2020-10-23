# api-python-sqlite3-basics

## Routes

<h3>'/'</h3>
default route

<h3>'/api/v1/' method=['POST']</h3>
It inserts in database values (id, name, begin_date, end_date). It returns 'Done in insert one' if everything is fine, else it returns an empty array. If some error occours it also returns an empty array

<h3>'/api/v1/?id=any' method=['GET']</h3>
It searchs in database by id that is passed through query params. It returns all matches.

<h3>'/api/v1/all' method=['GET']</h3>
It returns all items from database
