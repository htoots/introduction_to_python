from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog
import os


#	Main window root
root = Tk(className = " Untitled - Text Editor")

#	Width and height dont matter, theyre dynamically changed
textArea = scrolledtext.ScrolledText(root, width = 100, height = 100)

#	Functions

#	Function for erasing everything(new unsaved file)
def newFile(event = None):

	#	If current text area has something written in it
	if len(textArea.get('1.0', END+'-1c')) > 0:
		if messagebox.askyesno("Save?", "Do you wish to save?"):
			saveFile()
			#textArea.delete('1.0', END)
		else:
			textArea.delete('1.0', END)

	root.title("Untitled - Text Editor")

#	Function for opening a file in our editor
def openFile(event = None):
	file = filedialog.askopenfile(parent = root, title = 'Select a text file', filetypes = (("Text file","*.txt"), ("All files", "*.*")))
	
	root.title(os.path.basename(file.name) + " - Text Editor")

	#	Check if opened file is not None
	if file != None:
		contents = file.read()
		textArea.insert('1.0', contents)
		file.close()

	#	Bug code, probably cant be accessed
	else:
		root.title("Untitled - Text Editor")

#	Function to save the file curerntly open
def saveFile(event = None):
	file = filedialog.asksaveasfile(mode = 'w', defaultextension = ".txt", filetypes = (("Text file","*.txt"), ("All files", "*.*")))

	if file != None:
		# .get adds a character that we will remove
		data = textArea.get('1.0', END+'-1c')
		file.write(data)
		file.close()

def about():
	label = messagebox.showinfo("About", "A python text editor made by Hannes Toots")

def exit():
	if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
		root.destroy()

#	Binded commands to keyboard
root.bind('<Control-s>', saveFile)
root.bind('<Control-S>', saveFile)
root.bind('<Control-n>', newFile)
root.bind('<Control-N>', newFile)
root.bind('<Control-o>', openFile)
root.bind('<Control-O>', openFile)



#	Menu and its cascades/commands
menu = Menu(root)
root.config(menu = menu)
fileMenu = Menu(menu)
menu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command( label = "New", command = newFile,  accelerator ="Ctrl+N")
fileMenu.add_command( label = "Open", command = openFile,  accelerator ="Ctrl+O")
fileMenu.add_command( label = "Save", command = saveFile, accelerator ="Ctrl+S")
fileMenu.add_command( label = "Print")
fileMenu.add_separator()
fileMenu.add_command( label = "Exit", command = exit)

helpMenu = Menu(menu)
menu.add_cascade(label = "Help", menu = helpMenu)
helpMenu.add_command(label = "About", command = about)

#	Pack in order to dynamically increase the textarea size
textArea.pack(fill="both", expand = True)


#	Keep window open
root.mainloop()