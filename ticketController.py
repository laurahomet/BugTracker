#------------------------------------------------------
# Author: Laura Homet Garcia
# Date: 10/16/2020
# Description: Ticket View for BugTracker V1.0
# Additional Comments: None
#------------------------------------------------------

class TicketController(object):
	
	def __init__(self, model, view):
		self.model = model
		self.view = view

	def show_ticket_list(self):
		tickets = self.model.read_tickets()
		self.view.show_ticket_list(tickets)

	def show_ticket(self,title):
		try:
			ticket = self.model.read_ticket(title)
			self.view.show_ticket(ticket)
		except:
			self.view.display_missing_ticket(title)

	def insert_ticket(self,ticket):
		try:
			self.model.create_ticket(ticket)
			self.view.display_ticket_stored(ticket.title)
		except:
			self.view.display_ticket_already_stored(ticket.title)

	def update_ticket(self,title,index,newVal):
		self.model.update_ticket(title,index,newVal)
		self.view.display_ticket_updated(title,newVal)

	def delete_ticket(self,title):
		self.model.delete_ticket(title)
		self.view.display_ticket_deleted(title)


