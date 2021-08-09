#------------------------------------------------------
# Author: Laura Homet Garcia
# Date: 11/21/2020
# Description: Constants for BugTracker V2.0
# Additional Comments: None
#------------------------------------------------------

### Constants
win_width = 1000
win_height = 700

ID_width = 30
title_width = 300
assignee_width = 100
priority_width = 80
status_width = 50

plus_size = 5

titleBG = "#dab420"
ticketBG = "#fff6df"

ticket_indexes = {	
	'ID': 0,
	'title':1,
	'description':2,
	'submitter':3,
	'assignee':4,
	'priority':5,
	'created':6,
	'status':7
}

### Properties
ticket_properties = [
	"Title",
	"Description",
	"Submitter",
	"Assignee",
	"Priority"
]

ticket_all_properties = [
	"ID",
	"Title",
	"Description",
	"Submitter",
	"Assignee",
	"Priority",
	"Created At",
	"Status"
]

### Initial ticket values
ticket_defaults = [
	"",
	"Insert a title",
	"Insert a description",
	"Insert your name",
	"Insert assignee's name",
	"Insert a priority level",
	"",
	""
]

### Progress columns
progress_headings = [
	'Pending',
	'In Progress',
	'Testing',
	'Done'
]

progress_index = {	
	'Pending':0,
	'In Progress':1,
	'Testing':2,
	'Done':3
}


