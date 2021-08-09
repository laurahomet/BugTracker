#------------------------------------------------------
# Author: Laura Homet Garcia
# Date: 10/16/2020
# Description: Ticket View for BugTracker V2.0
# Additional Comments: None
#------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as scr
import ticketModel as tm
import constants as C

class TicketView(tk.Tk):

	def __init__(self, controller):

		self.controller = controller

		super().__init__() # Initialize the tk.Tk object

		self.view_frame_hidden = True

		self._init_window()
		self._init_vars()
		self._make_title_frame()
		self._make_side_bar()
		self._make_ticket_tab()
		self._customize_ticket_list()
		self.update_ticket_list()
		self._make_progress_tab()
		self._update_progress_tab()


	def main(self):
		self.mainloop()

	def _init_window(self):
		self.title("Bug Tracker 2.0") # Title method inherited from tk
		self.geometry(f'{C.win_width}x{C.win_height}')
		self.resizable(False,False)
		self.configure(bg=C.titleBG)


	def _init_vars(self):
		self.vars = list()
		self.entries = list()
		self.iid_count = int()
		self.edit_flag = False
		for item in C.ticket_all_properties:
			self.vars.append('')
			self.entries.append('')

	def _make_title_frame(self):
		frame = ttk.Frame(self)
		frame.pack(fill='x')
		label = tk.Label(frame, text="Welcome to Bug Tracker!", bg=C.titleBG, font="Calibri 20")
		label.pack(fill='x')

	def _make_side_bar(self):
		style = ttk.Style(self)
		style.theme_use('classic')
		style.configure('TNotebook', background=C.ticketBG, borderwidth=0)

		notebook = ttk.Notebook(self, style='TNotebook')
		self.ticket_list_tab = tk.Frame(notebook, bg=C.ticketBG, width=C.win_width, height=C.win_height)
		self.progress_tab = tk.Frame(notebook, bg=C.ticketBG, width=C.win_width, height=C.win_height)
		notebook.add(self.ticket_list_tab, text='Ticket List')
		notebook.add(self.progress_tab, text='Progress')
		notebook.pack(padx=10, pady=10, expand=True, fill='both')
		notebook.bind("<<NotebookTabChanged>>",self._progress_tab_click)

	def _make_ticket_tab(self):
		ticket_list_frame = tk.Frame(self.ticket_list_tab,bg=C.ticketBG)
		ticket_list_frame.pack(padx=30, pady=30, expand=True,fill='both')

		plus_button = tk.Button(ticket_list_frame, text='+', width=C.plus_size, height=C.plus_size-2, bg=C.ticketBG, command=self._new_ticket)
		plus_button.pack(side='right',anchor='ne')

		self.ticket_list = ttk.Treeview(ticket_list_frame, columns=(1,2,3,4,5), show="tree")
		self.ticket_list.pack(side='left',expand=True, fill='both')

	def _customize_ticket_list(self):
		style = ttk.Style()
		style.configure('Treeview',background=C.ticketBG,rowheight=25,fieldbackground=C.ticketBG,borderwidth=0)
		style.map('Treeview', background=[('selected',C.titleBG)])

		self.ticket_list.heading(1, text="ID")
		self.ticket_list.heading(2, text="Title")
		self.ticket_list.heading(3, text="Assignee")
		self.ticket_list.heading(4, text="Priority")
		self.ticket_list.heading(5, text="Status")

		self.ticket_list.column('#0', width=0, stretch=tk.NO)
		self.ticket_list.column(1, width=C.ID_width)
		self.ticket_list.column(2, width=C.title_width)
		self.ticket_list.column(3, width=C.assignee_width)
		self.ticket_list.column(4, width=C.priority_width)
		self.ticket_list.column(5, width=C.status_width)

		self.ticket_list.bind('<Double-1>', self._edit_ticket)

	def _make_edit_window(self):
		self.top = tk.Toplevel(self,bg=C.ticketBG)
		self.top.geometry(f'{int(C.win_width/2)}x{int(C.win_height/2)}')
		self.top.title("Edit Ticket")
		self.top.resizable(False,False)
		self.top.configure(bg=C.titleBG)

		frame = tk.Frame(self.top,bg=C.ticketBG)
		frame.pack(padx=10,pady=10,expand=True,fill='both')

		in_frame = tk.Frame(frame,bg=C.ticketBG)
		in_frame.pack(expand=True, fill='x',padx=30, pady=30)

		for i,item in enumerate(C.ticket_all_properties):

			row_frame = tk.Frame(in_frame,bg=C.ticketBG)
			row_frame.pack(expand=True, fill='x')

			self.vars[i] = tk.StringVar()

			if i == C.ticket_indexes['ID'] and not self.edit_flag:
				pass
			elif i == C.ticket_indexes['description']:
				label = tk.Label(row_frame,text=item+':',font="Calibri 13",bg=C.ticketBG,width=10,justify='left')
				label.pack(side='left',anchor='nw')
				self.entries[i] = scr.ScrolledText(row_frame,wrap=tk.WORD,font="Calibri 13",height=1,fg='gray',highlightcolor='white')
				self.entries[i].pack(side='right',anchor='nw',fill='x')
			elif i == C.ticket_indexes['created'] and not self.edit_flag:
				pass
			elif i == C.ticket_indexes['status'] and not self.edit_flag:
				pass
			else:
				label = tk.Label(row_frame,text=item+':',font="Calibri 13",bg=C.ticketBG,width=10,justify='left')
				label.pack(side='left')
				self.entries[i] = tk.Entry(row_frame, textvariable=self.vars[i], font="Calibri 13",bg='white',fg='gray',highlightcolor='white',bd=0)
				self.entries[i].pack(side='right',fill='x',expand=True)

		buttons_frame = tk.Frame(in_frame,bg=C.ticketBG)
		buttons_frame.pack(expand=True, fill='x')

		if self.edit_flag:
			delete_button = tk.Button(buttons_frame, text='Delete', bg='red', command=self._delete_click)
			delete_button.pack(side='left',padx=75)

		discard_button = tk.Button(buttons_frame, text='Discard', bg='red', command=self._discard_click)
		submit_button = tk.Button(buttons_frame, text='Submit', bg='red', command=self._submit_click)
		discard_button.pack(side='right')
		submit_button.pack(side='right')

	def _new_ticket(self):
		self.edit_flag = False
		self._make_edit_window()

	def _edit_ticket(self,a):
		self.edit_flag = True
		self._make_edit_window()
		iid = self.ticket_list.focus()
		ticket = self.controller.show_ticket(iid)
		self.vars[C.ticket_indexes['ID']].set(ticket.id)
		self.vars[C.ticket_indexes['title']].set(ticket.title)
		self.entries[C.ticket_indexes['description']].insert(tk.INSERT,ticket.description)
		self.vars[C.ticket_indexes['submitter']].set(ticket.submitter)
		self.vars[C.ticket_indexes['assignee']].set(ticket.assignee)
		self.vars[C.ticket_indexes['priority']].set(ticket.priority)
		self.vars[C.ticket_indexes['created']].set(ticket.created)
		self.vars[C.ticket_indexes['status']].set(ticket.status)

	def _delete_click(self):
		self.top.destroy()
		self._reset_vars()
		iid = self.ticket_list.focus()
		self.controller.delete_ticket(iid)
		#self.ticket_list.delete(iid)

	def _discard_click(self):
		self.top.destroy()
		self._reset_vars()

	def _submit_click(self):

		if self.edit_flag:

			iid = self.ticket_list.focus()

			for i,item in enumerate(C.ticket_all_properties):
				if i == C.ticket_indexes['ID']: pass          # Not editable
				elif i == C.ticket_indexes['description']:
					self.controller.update_ticket(iid, i, self.entries[i].get('1.0',tk.END))
				elif i == C.ticket_indexes['submitter']: pass # Not editable
				elif i == C.ticket_indexes['created']: pass   # Not editable
				else:
					self.controller.update_ticket(iid, i, self.entries[i].get())

		else:
			for i,item in enumerate(C.ticket_all_properties):
				if i == C.ticket_indexes['ID']: pass          # No shown
				elif i == C.ticket_indexes['description']:
					self.vars[i].set(self.entries[i].get('1.0',tk.END))
				elif i == C.ticket_indexes['created']: pass   # Not shown
				elif i == C.ticket_indexes['status']: pass   # Not shown
				else:
					self.vars[i].set(self.entries[i].get())

			ticket = tm.Ticket(self.iid_count,
							self.vars[C.ticket_indexes['title']].get(),
							self.vars[C.ticket_indexes['description']].get(),
							self.vars[C.ticket_indexes['submitter']].get(),
							self.vars[C.ticket_indexes['assignee']].get(),
							self.vars[C.ticket_indexes['priority']].get())

			self.controller.insert_ticket(ticket)

		self.top.destroy()
		self._reset_vars()

	def _reset_vars(self):
		for i,item in enumerate(C.ticket_all_properties):
			self.vars[i] = ''
			self.entries[i] = ''

	def _show_ticket(self,a):
		iid = self.ticket_list.focus()
		print(f'Selected ticket {iid}')

		#Retrieve data from this ticket
		ticket = self.controller.show_ticket(iid)

		#Show the ticket view
		if self.view_frame_hidden:
			self.view_frame_hidden = False
		else:
			self.view_frame.destroy()
		self._make_ticket_view(ticket)


	def _edit_click(self):
		iid = self.ticket_list.focus()
		print(f'Edit ticket {iid}')



	def update_ticket_list(self):

		#Remove all items in ticket list
		for item in self.ticket_list.get_children():
			self.ticket_list.delete(item)

		#Retrieve values from database
		tickets = self.controller.show_ticket_list()

		#Create ticket list
		for ticket in tickets:
			self.ticket_list.insert('','end',iid=ticket.id,values=(ticket.id,ticket.title,ticket.assignee,ticket.priority,ticket.status))
			self.iid_count = ticket.id+1 #Assuming tickets are retrieved in order


	def _make_progress_tab(self):
		progress_frame = tk.Frame(self.progress_tab,bg=C.ticketBG)
		progress_frame.pack(padx=30, pady=30, expand=True,fill='both')

		self.progress_frames = ['']*len(C.progress_index)
		for i in range(len(C.progress_index)):
			self.progress_frames[i] = tk.Frame(progress_frame,bg=C.ticketBG)
			self.progress_frames[i].pack(padx=5, pady=5, side='left', expand=True,fill='both')
			self.progress_frames[i].pack_propagate(0)

	def _update_progress_tab(self):

		#Remove current contents
		for i in range(len(C.progress_index)):
			#self.progress_frames[i].pack_forget()
			for widget in self.progress_frames[i].winfo_children():
				widget.destroy()

		#Headings
		for i in range(len(C.progress_headings)):
			label = tk.Label(self.progress_frames[i], text=C.progress_headings[i], bg=C.ticketBG, font="Calibri 15 bold", anchor='w')
			label.pack(fill='x')

		#Retrieve values from database
		tickets = self.controller.show_ticket_list()

		#Create ticket list
		for ticket in tickets:
			label = tk.Label(self.progress_frames[C.progress_index[ticket.status]], text=ticket.title, bg=C.ticketBG, font="Calibri 15", anchor='nw')
			label.pack(fill='x')


	def _progress_tab_click(self,event):
		self._update_progress_tab()




