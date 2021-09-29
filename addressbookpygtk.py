# import pygtk
# pygtk.require('2.0')
import gtk

import MySQLdb
#connect to mysql database
conn = MySQLdb.connect(host="localhost",user="master",passwd="master",db="address_book")
#create a cursor
cursor = conn.cursor()

class Addressbook:
	def __init__(self):
		#Initialising widgets and packing it into window
		self.mainWindow = gtk.Window()
		self.mainWindow.set_title("AddressBook - PyGTK, Python & MySQL")
		self.mainWindow.set_size_request(600,300)
		self.mainWindow.connect("destroy",gtk.main_quit)

		self.vbox = gtk.VBox()
		self.vbox.set_border_width(10)
		self.mainWindow.add(self.vbox)

		self.table = gtk.Table(7,2,True) #creates a table with 7 rows and 2 columns
		self.table.set_border_width(10)
		self.table.set_row_spacings(3)
		self.table.set_col_spacings(3)
		self.vbox.pack_start(self.table,False,True,0)

		label = gtk.Label("Enter the SSN Number :")   
		self.table.attach(label,0,1,0,1)
		self.entry1 = gtk.Entry(max = 30)
		self.table.attach(self.entry1,1,2,0,1)

		label = gtk.Label("Enter the Name :")
		self.table.attach(label,0,1,1,2)
		self.entry2 = gtk.Entry(max = 30)
		self.table.attach(self.entry2,1,2,1,2)

		label = gtk.Label("Enter the Address :")
		self.table.attach(label,0,1,2,3)
		self.entry3 = gtk.Entry(max = 30)
		self.table.attach(self.entry3,1,2,2,3)

		label = gtk.Label("Enter the City :")
		self.table.attach(label,0,1,3,4)
		self.entry4 = gtk.Entry(max = 30)
		self.table.attach(self.entry4,1,2,3,4)

		
		label = gtk.Label("Enter the State :")
		self.table.attach(label,0,1,4,5)
		self.entry5 = gtk.Entry(max = 30)
		self.table.attach(self.entry5,1,2,4,5)

		label = gtk.Label("Enter the Postcode :")
		self.table.attach(label,0,1,5,6)
		self.entry6 = gtk.Entry(max = 30)
		self.table.attach(self.entry6,1,2,5,6)

		label = gtk.Label("Enter the Country :")
		self.table.attach(label,0,1,6,7)
		self.entry7 = gtk.Entry(max = 30)
		self.table.attach(self.entry7,1,2,6,7)

		separator = gtk.HSeparator()
		self.vbox.pack_start(separator,False,True,5)

		self.hbox = gtk.HBox(False,0)
		self.vbox.pack_start(self.hbox,True,True,0)

		self.tooltips = gtk.Tooltips()
		
		#creating buttons and packing it into window
		button = gtk.Button("Add") 
		self.hbox.pack_start(button,True,True,2)
		button.connect("clicked",self.add_entry) #When this button is clicked, it invokes self.add_entry method
		self.tooltips.set_tip(button,"Add a Record")

		button  = gtk.Button("showUpdateWindow")
		self.hbox.pack_start(button,True,True,2)
		button.connect("clicked",self.create_UpdateWind)#When this button is clicked, it invokes self.create_UpdateWind method
		self.tooltips.set_tip(button,"Update a Record")
		

		button  = gtk.Button("Update")
		self.hbox.pack_start(button,True,True,2)
		button.connect("clicked",self.update_entry)#When this button is clicked, it invokes self.update_entry method
		self.tooltips.set_tip(button,"Update a Record")
		

		button  = gtk.Button("Delete")
		self.hbox.pack_start(button,True,True,2)
		button.connect("clicked",self.create_DeleteWind)#When this button is clicked, it invokes self.create_DeleteWind method
		self.tooltips.set_tip(button,"Delete a Record")

		button  = gtk.Button("Search")
		self.hbox.pack_start(button,True,True,2)
		button.connect("clicked",self.create_SearchWind)#When this button is clicked, it invokes self.create_SearchWind method
		self.tooltips.set_tip(button,"Search a Record")


		button  = gtk.Button("View")
		self.hbox.pack_start(button,True,True,2)
		button.connect("clicked",self.view_entry)#When this button is clicked, it invokes self.view_entry method
		self.tooltips.set_tip(button,"View Records")

		button = gtk.Button("Close")
		self.hbox.pack_start(button,True,True,2)
		button.connect("clicked",gtk.main_quit)#When this button is clicked, terminates the application
		self.tooltips.set_tip(button,"Terminate the Application")

		separator = gtk.HSeparator()
		self.vbox.pack_start(separator,False,True,5)
		
		self.mainWindow.show_all()
		

	def add_entry(self,widget):
		#Receiving data from text entries
		self.ssn = self.entry1.get_text()
		self.name = self.entry2.get_text()
		self.address = self.entry3.get_text()
		self.city = self.entry4.get_text()
		self.state = self.entry5.get_text()
		self.postcode = self.entry6.get_text()
		self.country = self.entry7.get_text()
		#inserting the data into the database
		cursor.execute("""
				insert into addresses (ssn,name,address,city,state,postcode,country)
				values (%s,%s,%s,%s,%s,%s,%s)""",(self.ssn,self.name,self.address,self.city,self.state,self.postcode,self.country))
		#after inserting clear all the text in the text entries
		self.entry1.set_text("")
		self.entry2.set_text("")
		self.entry3.set_text("")
		self.entry4.set_text("")
		self.entry5.set_text("")
		self.entry6.set_text("")
		self.entry7.set_text("")		
		
	def create_UpdateWind(self,widget):
		#creating update window
		self.updateWindow = gtk.Window()
		self.updateWindow.set_title("Update Window")
		self.updateWindow.set_size_request(500,100)

		self.vbox = gtk.VBox()
		self.updateWindow.add(self.vbox)
		
		self.table = gtk.Table(1,2,True)
		self.vbox.pack_start(self.table,True,True,0)

		label = gtk.Label("Enter the Old SSN Number to Update :")
		self.table.attach(label,0,1,0,1)
		self.entry8 = gtk.Entry(max = 30)
		self.table.attach(self.entry8,1,2,0,1)
		
		
		separator = gtk.HSeparator()
		self.vbox.pack_start(separator,False,True,5)

		self.hbox = gtk.HBox(False,0)
		self.vbox.pack_start(self.hbox,True,True,0)

		button = gtk.Button("OK")
		self.hbox.pack_start(button,True,True,2)
		button.connect("clicked",self.destroy_showUpdate)
			
		separator = gtk.HSeparator()
		self.vbox.pack_start(separator,False,True,5)				

		self.updateWindow.show_all()

	def destroy_showUpdate(self,widget):
		#Hides updateWindow
		self.updateWindow.hide()


	def update_entry(self,widget):
		#Receiving data from text entries
		self.oldssn = self.entry8.get_text()
		self.ssn = self.entry1.get_text()
		self.name = self.entry2.get_text()
		self.address = self.entry3.get_text()
		self.city = self.entry4.get_text()
		self.state = self.entry5.get_text()
		self.postcode = self.entry6.get_text()
		self.country = self.entry7.get_text()
		#update the database
		cursor.execute("""
			update addresses set ssn = %s,name = %s,address=%s,city=%s,state=%s,postcode=%s,country=%s
			where ssn = %s""",(self.ssn,self.name,self.address,self.city,self.state,self.postcode,self.country,self.oldssn))
		#after updating clear all the text in the text entries
		self.entry1.set_text("")	
		self.entry2.set_text("")
		self.entry3.set_text("")
		self.entry4.set_text("")
		self.entry5.set_text("")
		self.entry6.set_text("")
		self.entry7.set_text("")			
	
	def create_DeleteWind(self,widget):
		#creating delete window
		self.deleteWindow = gtk.Window()
		self.deleteWindow.set_title("Delete Window")
		self.deleteWindow.set_size_request(500,100)

		self.vbox = gtk.VBox()
		self.deleteWindow.add(self.vbox)
		
		self.table = gtk.Table(1,2,True)
		self.vbox.pack_start(self.table,True,True,0)

		label = gtk.Label("Enter the SSN Number to Delete :")
		self.table.attach(label,0,1,0,1)
		self.entry9 = gtk.Entry(max = 30)
		self.table.attach(self.entry9,1,2,0,1)

		separator = gtk.HSeparator()
		self.vbox.pack_start(separator,False,True,5)
		
		self.hbox = gtk.HBox(False,0)
		self.vbox.pack_start(self.hbox,True,True,0)		

		button = gtk.Button("Ok")
		self.hbox.pack_start(button,True,True,0)
		button.connect("clicked",self.destroy_deleteWind)

		button = gtk.Button("Delete")
		self.hbox.pack_start(button,True,True,0)
		button.connect("clicked",self.delete_entry)


		separator = gtk.HSeparator()
		self.vbox.pack_start(separator,False,True,5)	

		self.deleteWindow.show_all()

	def delete_entry(self,widget):
		#receive data from the text entry
		ssn = self.entry9.get_text()
		#delete appropriate record
		cursor.execute("""
			delete from addresses 
			where ssn=%s""",ssn)
		#set the text entry to null
		self.entry9.set_text("")

	def destroy_deleteWind(self,widget):
		#Hides deleteWindow
		self.deleteWindow.hide()
		

	def create_SearchWind(self,widget):
		#create search window
		self.searchWindow = gtk.Window()
		self.searchWindow.set_title("Search Window")
		self.searchWindow.set_size_request(500,100)

		self.vbox = gtk.VBox()
		self.searchWindow.add(self.vbox)
		
		self.table = gtk.Table(1,2,True)
		self.vbox.pack_start(self.table,True,True,0)

		label = gtk.Label("Enter Name to Search a Record:")
		self.table.attach(label,0,1,0,1)
		self.entry10 = gtk.Entry(max = 30)
		self.table.attach(self.entry10,1,2,0,1)

		separator = gtk.HSeparator()
		self.vbox.pack_start(separator,False,True,5)
		
		self.hbox = gtk.HBox(False,0)
		self.vbox.pack_start(self.hbox,True,True,0)		

		button = gtk.Button("OK")
		self.hbox.pack_start(button,True,True,0)
		button.connect("clicked",self.search_entry)		

		separator = gtk.HSeparator()
		self.vbox.pack_start(separator,False,True,5)	

		self.searchWindow.show_all()

	def search_entry(self,widget):
		#open a file in write mode
		try:
			f = open("dbdata.py","w")
		except IOError:
			pass
		#create Display Search Entry window
		self.searchDisplay = gtk.Window()
		self.searchDisplay.set_title("Display Search Entry")
		self.searchDisplay.set_size_request(600,200)	

		self.vbox = gtk.VBox()
		self.searchDisplay.add(self.vbox)

		self.scrolled_window = gtk.ScrolledWindow()
		self.scrolled_window.set_border_width(10)
		self.scrolled_window.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
	

		self.textview = gtk.TextView()
		self.textview.set_left_margin(20)
		self.textbuffer = self.textview.get_buffer()
		self.scrolled_window.add(self.textview)		
		self.vbox.pack_start(self.scrolled_window,True,True,0)

		#receive data from text entry
		search_item = self.entry10.get_text()
		
		#search the database
		cursor.execute( "select * from addresses where name = %s",search_item)
		#fetch all rows
		rows = cursor.fetchall()
		for record in rows:
			#a is a tuple
			a = str(record[0]),"-->",record[1],"-->",record[2],"-->",record[3],"-->",record[4],"-->",str(record[5]),"-->",record[6]	
			#write the tuple into a file
			f.write(" ".join(a))
			f.write("\n")
		
		#open the file in read mode	
		f = open("dbdata.py","r")
		if f:
			string = f.read() #read the file contents
			f.close()#close the file 
			self.textbuffer.set_text(string)#in the text buffer set the file contents

		separator = gtk.HSeparator()
		self.vbox.pack_start(separator,False,True,5)
		
		self.hbox = gtk.HBox(False,0)
		self.vbox.pack_start(self.hbox,True,True,0)		

		button = gtk.Button("Close")
		self.hbox.pack_start(button,True,True,0)
		button.connect("clicked",self.destroy_search)		

		separator = gtk.HSeparator()
		self.vbox.pack_start(separator,False,True,5)
		
		self.searchDisplay.show_all()	

	def destroy_search(self,widget):
		#hide search window
		self.searchWindow.hide()
		#hide search display window
		self.searchDisplay.hide()
			
		
	def view_entry(self,widget):
		try:
			f = open("dbdata.py","w")
		except IOError:
			pass
		self.viewWindow = gtk.Window()
		self.viewWindow.set_title("View Database")
		self.viewWindow.set_size_request(600,200)	
	
		self.vbox = gtk.VBox()
		self.viewWindow.add(self.vbox)

		self.scrolled_window = gtk.ScrolledWindow()
		self.scrolled_window.set_border_width(10)
		self.scrolled_window.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
	

		self.textview = gtk.TextView()
		self.textview.set_left_margin(20)
		self.textbuffer = self.textview.get_buffer()
		self.scrolled_window.add(self.textview)		
		self.vbox.pack_start(self.scrolled_window,True,True,0)

		#returns the whole table data
		cursor.execute("select * from addresses")
		rows = cursor.fetchall()
		for record in rows:
			a = str(record[0]),"-->",record[1],"-->",record[2],"-->",record[3],"-->",record[4],"-->",str(record[5]),"-->",record[6]	
			f.write(" ".join(a))
			f.write("\n")
		
		f = open("dbdata.py","r")
		if f:
			string = f.read()
			f.close()
			self.textbuffer.set_text(string)
		

		separator = gtk.HSeparator()
		self.vbox.pack_start(separator,False,True,5)
		
		self.hbox = gtk.HBox(False,0)
		self.vbox.pack_start(self.hbox,True,True,0)		

		button = gtk.Button("Close")
		self.hbox.pack_start(button,True,True,0)
		button.connect("clicked",self.destroy_view)		

		separator = gtk.HSeparator()
		self.vbox.pack_start(separator,False,True,5)
		
		self.viewWindow.show_all()

	def destroy_view(self,widget):
		#hide view Window
		self.viewWindow.hide()		
	
	def main(self):
		gtk.main()	

if __name__ == "__main__":
	a = Addressbook()
	a.main()
