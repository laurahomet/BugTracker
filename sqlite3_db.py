import sqlite3
import constants as C

# indexDict = {'title' 		: 1,
# 			 'description' 	: 2,
# 			 'submitter' 	: 3,
# 			 'assignee' 	: 4,
# 			 'priority' 	: 5,
# 			 'status' 		: 6}

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
        								id integer,
        								title text,
        								description text,
        								submitter text,
        								assignee text,
        								priority text,
        								created text,
        								status text
        								)
        							''')
	except:
		pass
	#except OperationalError as e:
	#	print(e)


def create_ticket(conn,ticket):
	with conn: # No need for conn.commit()
		conn.execute("INSERT INTO tickets VALUES (?,?,?,?,?,?,?,?)", 
												(ticket.id,
												ticket.title,
												ticket.description,
												ticket.submitter,
												ticket.assignee,
												ticket.priority,
												ticket.created,
												ticket.status))

def read_ticket(conn,ID):
	c = conn.execute("SELECT * FROM tickets WHERE id=?",(ID,))
	return c.fetchone()

def read_tickets(conn):
	c = conn.execute("SELECT * FROM tickets")
	return c.fetchall()

def update_ticket(conn,ID,updateIndex,updateData):
	with conn:
		if updateIndex==C.ticket_indexes['title']:
			conn.execute("UPDATE tickets SET title=? WHERE id=?",(updateData,ID))
		elif updateIndex==C.ticket_indexes['description']:
			conn.execute("UPDATE tickets SET description=? WHERE id=?",(updateData,ID))
		# elif updateIndex==C.ticket_indexes['submitter']:
		# 	conn.execute("UPDATE tickets SET submitter=? WHERE id=?",(updateData,ID))
		elif updateIndex==C.ticket_indexes['assignee']:
			conn.execute("UPDATE tickets SET assignee=? WHERE id=?",(updateData,ID))
		elif updateIndex==C.ticket_indexes['priority']:
			conn.execute("UPDATE tickets SET priority=? WHERE id=?",(updateData,ID))
		elif updateIndex==C.ticket_indexes['status']:
			conn.execute("UPDATE tickets SET status=? WHERE id=?",(updateData,ID))


def delete_ticket(conn,ID):
	print(f'deleting {ID}')
	with conn:
		conn.execute("DELETE from tickets WHERE id=?",(ID,))

