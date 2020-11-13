#------------------------------------------------------
# Author: Laura Homet Garcia
# Date: 10/16/2020
# Description: Ticket View for BugTracker V1.0
# Additional Comments: None
#------------------------------------------------------
class TicketView(object):

	@staticmethod # Means we don't need to create a class to call this method
	def show_ticket_list(tickets):
		print("TICKET LIST:")
		for i, ticket in enumerate(tickets):
			print("{}. {}".format(i+1,ticket.title))
		print("\n")

	@staticmethod
	def show_ticket(ticket):
		print(ticket)
		print("\n")

	@staticmethod
	def display_missing_ticket(title):
		print("TICKET NOT FOUND. Sorry, we could not find the ticket: {}\n".format(title))

	@staticmethod
	def display_ticket_already_stored(title):
		print("TICKET ALREADY STORED. Sorry, this ticket was already created: {}\n".format(title))

	@staticmethod
	def display_ticket_stored(title):
		print("TICKET STORED SUCCESSFULLY. You added this ticket to the list: {}\n".format(title))

	@staticmethod
	def display_ticket_updated(title, newVal):
		print("TICKET INFORMATION WAS UPDATED. You updated the ticket with the following information: {}\n".format(newVal))

	@staticmethod
	def display_ticket_deleted(title):	
		print("TICKET REMOVED. You just removed this ticket: {}\n".format(title))


