#------------------------------------------------------
# Author: Laura Homet Garcia
# Date: 10/16/2020
# Description: Ticket View for BugTracker V2.0
# Additional Comments: None
#------------------------------------------------------
import ticketModel as tm
import ticketView as tv

class TicketController(object):
	
	def __init__(self):
		self.model = tm.TicketModel()
		self.view = tv.TicketView(self)

	def main(self):
		self.view.main()

	def show_ticket_list(self):
		return self.model.read_tickets()

	def show_ticket(self,ID):
		try:
			ticket = self.model.read_ticket(ID)
			return ticket
		except:
			print('No ticket with this ID')

	def insert_ticket(self,ticket):
		try:
			self.model.create_ticket(ticket)
		except:
			print('Ticket already stored')
		self.view.update_ticket_list()

	def update_ticket(self,title,index,newVal):
		self.model.update_ticket(title,index,newVal)
		self.view.update_ticket_list()

	def delete_ticket(self,ID):
		self.model.delete_ticket(ID)
		self.view.update_ticket_list()


if __name__== "__main__":
	tc = TicketController()
	tc.main()
