#------------------------------------------------------
# Author: Laura Homet Garcia
# Date: 10/15/2020
# Description: Ticket Model for BugTracker V1.0
# Additional Comments: None
#------------------------------------------------------
import database as db
import sqlite3_db as sdb
import datetime

class Ticket:

	def __init__(self,title,description,submitter,assignee,priority):
		self.title = title
		self.description = description
		self.submitter = submitter
		self.assignee = assignee
		self.priority = priority

		self.created = datetime.datetime.now()
		self.status = 'Pending'


	def __str__(self):
		return "PRINTING TICKET.\nTitle: {}\nDescription: {}\nCreated: {}\nSubmitter: {}\nAssignee: {}\nPriority: {}\nStatus: {}".format(
			self.title,self.description,self.created,self.submitter,self.assignee,self.priority,self.status)


class TicketModel(object):

	def __init__(self):
		self.conn = sdb.connect_to_db('tickets')
		sdb.create_table(self.conn)

	def tuple_to_ticket(self,tup):
		title,description,submitter,assignee,priority,created,status = tup
		temp_ticket = Ticket(title,description,submitter,assignee,priority)
		temp_ticket.created = created
		temp_ticket.status = status
		return temp_ticket

	def create_ticket(self,ticket):
		sdb.create_ticket(self.conn,ticket)

	def read_ticket(self,title):
		return self.tuple_to_ticket(sdb.read_ticket(self.conn,title))

	def read_tickets(self):
		return [self.tuple_to_ticket(ticket) for ticket in sdb.read_tickets(self.conn)]

	def update_ticket(self,title,index,newVal):
		sdb.update_ticket(self.conn,title,index,newVal)

	def delete_ticket(self,title):
		sdb.delete_ticket(self.conn,title)


