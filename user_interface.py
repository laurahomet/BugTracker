#------------------------------------------------------
# Author: Laura Homet Garcia
# Date: 10/16/2020
# Description: User Interface for BugTracker V1.0
# Additional Comments: None
#------------------------------------------------------
import ticketModel as tm
import ticketView as tv
import ticketController as tc

# Create an instance of the controller
c = tc.TicketController(tm.TicketModel(),tv.TicketView())

# Create some tickets to insert
t1 = tm.Ticket('Improve Database','Show an error when trying to re-insert existing ticket or read/update/delete an empty lcoation','Laura','Myself','High')
t2 = tm.Ticket('Handle timezone in \'Created\' item','Improve \'Created\' so that it makes sure the time zone is correct','Homet','Me','Medium')
t3 = tm.Ticket('Create a GUI','The Bug Tracker will need a GUI for the user to use it','Garcia','MeMyself&I','Low')
t4 = tm.Ticket('Fix error handling','Errors must be raised (not printed) in order to call the proper function and be displayed','Myself','Laura','Critical')

# Insert the created tickets
c.insert_ticket(t1)
c.insert_ticket(t2)
c.insert_ticket(t3)
c.insert_ticket(t4)

# Read the tickets as a list
c.show_ticket_list()

# Update ticket 1
c.update_ticket('Missing Database',2,'I need to use an atual database, ,like SQLite, to create this Bug Tracker')

# Read the updated ticket
c.show_ticket('Missing Database')

# Add a new ticket
t5 = tm.Ticket('Fix ticket update','Find some other way to specify which item to updated, not hardcoding an index','Laura','Me','Critical')
c.insert_ticket(t5)

# Delete one of the tickets
c.delete_ticket('Create a GUI')

# Read all the tickets
c.show_ticket_list()

##---------------------- Assume not possible ----------------------
##Try to re-insert, read, update, or delete a non-existing ticket
#c.insert_ticket(t5)
#c.show_ticket('Create a GUI')
#c.update_ticket('Create a GUI',2,'Bug Tracker needs a GUI')
#c.delete_ticket('Create a GUI')
##-----------------------------------------------------------------
