import sqlite3

indexDict = {'title' 		: 1,
			 'description' 	: 2,
			 'submitter' 	: 3,
			 'assignee' 	: 4,
			 'priority' 	: 5,
			 'status' 		: 6}


def connect_to_db(database=None):
	if database is None:
		mydb = ':memory:'
	else:
		mydb = '{}.db'.format(database)
	conn = sqlite3.connect(mydb)
	return conn


def disconnect_from_db(conn=None):
	if conn is not None:
		conn.close()


def create_table(conn):
	try:
		conn.execute('''CREATE TABLE tickets (
        								title text,
        								description text,
        								submitter text,
        								assignee text,
        								priority text,
        								created text,
        								status text
        								)
        							''')
	except OperationalError as e:
		print(e)


def create_ticket(conn,ticket):
	with conn: # No need for conn.commit()
		conn.execute("INSERT INTO tickets VALUES (?,?,?,?,?,?,?)", 
												(ticket.title,
												ticket.description,
												ticket.submitter,
												ticket.assignee,
												ticket.priority,
												ticket.created,
												ticket.status))

def read_ticket(conn,title):
	c = conn.execute("SELECT * FROM tickets WHERE title=?",(title,))
	return c.fetchone()

def read_tickets(conn):
	c = conn.execute("SELECT * FROM tickets")
	return c.fetchall()

def update_ticket(conn,title,updateIndex,updateData):
	with conn:
		if updateIndex==indexDict['title']:
			conn.execute("UPDATE tickets SET title=? WHERE title=?",(updateData,title))
		elif updateIndex==indexDict['description']:
			conn.execute("UPDATE tickets SET description=? WHERE title=?",(updateData,title))
		elif updateIndex==indexDict['submitter']:
			conn.execute("UPDATE tickets SET submitter=? WHERE title=?",(updateData,title))
		elif updateIndex==indexDict['assignee']:
			conn.execute("UPDATE tickets SET assignee=? WHERE title=?",(updateData,title))
		elif updateIndex==indexDict['priority']:
			conn.execute("UPDATE tickets SET priority=? WHERE title=?",(updateData,title))
		elif updateIndex==indexDict['status']:
			conn.execute("UPDATE tickets SET status=? WHERE title=?",(updateData,title))


def delete_ticket(conn,title):
	with conn:
		conn.execute("DELETE from tickets WHERE title=?",(title,))

