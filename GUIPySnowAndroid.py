import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
import subprocess
import pyUnicodeSteganography as usteg

def snow_gui():
	finestra = tk.Tk()
	finestra.title("PySnow")
	finestra.configure(bg="black")
	#finestra.iconbitmap("icouriel.ico")
	frame1 = tk.Frame(finestra, bg="black")
	frame1.pack()
	
	def hide():
		finestra.destroy()
		def start_gui():
			global window
			#Window and frames
			window = tk.Tk()
			window.title("PySnow")
			window.configure(bg="black")
			#window.iconbitmap("icouriel.ico")
			frame1 = tk.Frame(window)
			frame1.pack()
			frame2 = tk.Frame(window, bg="black")
			frame2.pack()
			
			#Functions
			secret_message = ""
			container = "" #path
			
			def done():
				global newfile
				showinfo(
		        title='Done!',
		        message="Message hidden."
		    	)
				refresh()
			
			def stegsnow():
				global secret_message
				global container
				with open(container, "r", encoding='utf-8') as tohide:
					cont = tohide.read()
				encoded = usteg.encode(cont, secret_message)
				filetypes = (
						('testo', '*.txt'),
						('all', '.*')
						)
				final_path = fd.asksaveasfilename(initialdir="/storage/emulated/0", title="Save", filetypes=filetypes, defaultextension=".txt")
				with open(final_path, "w", encoding='utf-8') as finalpath:
					finalpath.write(encoded)
				done()
				
			def select_container():
				global container
				filetypes = (
				        ('testo', '*.txt'),
				        ('all', '.*')
				        )
				container = fd.askopenfilename(
				title='Container Text:  ',
				initialdir='/storage/emulated/0',
				filetypes=filetypes)
				path["state"] = "normal"
				path.insert(tk.END, container)
				path["state"] = "disabled"
						
			def hide():
				global secret_message
				global container
				secret_message = message.get("1.0", tk.END)
				message.delete("1.0", tk.END)
				stegsnow()
			
			def exithide():
				window.destroy()
				snow_gui()
				
			#Widgets
			buttons_style = ttk.Style()
			buttons_style.configure('my.TButton', font=('Times', 8))
			buttons_style.configure('big.TButton', font=('Times', 9, 'bold'))
			
			title = tk.Label(frame1, text="SNOW",
				fg= "white",
				bg= "black",
				font=("Times", 14, "bold"))
			title.pack(fill=tk.X)
			
			message_label = tk.Label(frame1, text="\n\nWrite here the secret message: ", bg="black", fg="white", font=("Times", 7))
			message_label.pack(fill=tk.X)
			
			message = tk.Text(frame1, padx=15, pady=15, height=8, font=("Times", 7), wrap="word")
			message.pack()
			
			select_label = tk.Label(frame1, text="\nChoose the text file \nin which you want to hide your message: ", bg="black", fg="white", font=("Times", 7))
			select_label.pack(fill=tk.X)
			
			path = tk.Entry(frame1, state="disabled")
			path.pack(side=tk.LEFT)
			
			filebutt = ttk.Button(frame1, text="Choose File", style="my.TButton", command=select_container)
			filebutt.pack(side=tk.RIGHT)
			
			empty = tk.Label(frame2, bg="black").pack(fill=tk.X)
			
			'''final_label = tk.Label(frame2, text="\nNome del file finale: ", bg="black", fg="white", font=("Times", 7))
			final_label.pack(fill=tk.X)
			
			newfileentry = tk.Entry(frame2)
			newfileentry.pack()'''
			
			empty = tk.Label(frame2, bg="black").pack(fill=tk.X)
			
			hidebutton = ttk.Button(frame2, text="Hide", style="big.TButton", command=hide)
			hidebutton.pack()
			
			empty = tk.Label(frame2, text="\n\n", bg="black").pack(fill=tk.X)
			
			refreshbutton = ttk.Button(frame2, text="Clean", style="my.TButton", command=refresh)
			refreshbutton.pack(side=tk.LEFT)
			
			empty = tk.Label(frame2, bg="black").pack(side=tk.LEFT)
			
			exitbutton = ttk.Button(frame2, text="Exit", style="my.TButton", command=exithide)
			exitbutton.pack(side=tk.LEFT)
			
			window.mainloop()
	
		def refresh():
			window.destroy()
			start_gui()
			
		start_gui()
	
	def extract():
		finestra.destroy()
		def startgui():
			global window
			file_path = None
			
			def extract2():
				global file_path
				with open(file_path, "r") as todecode:
					todecode = open(file_path, "r")
				mess = todecode.read()
				decoded = usteg.decode(mess)
				showtext["state"] = "normal"
				showtext.insert(tk.END, decoded)
				showtext["state"] = "disabled"
				todecode.close()
			
			def toopen():
				global file_path
				file_path = fd.askopenfilename(
					title='Container Text:  ',
					initialdir='/storage/emulated/0', 
					filetypes=(('text', '*.txt'), ('all', '.*'))
					)
				opened["text"] = file_path
			
			def principal():
				window.destroy()
				snow_gui()
			
			#Window
			window = tk.Tk()
			window.title("PySnow")
			window.configure(bg="black")
			#window.iconbitmap("icouriel.ico")
			#Widgets
			title = tk.Label(text="PySnow",
				fg= "white",
				bg= "black",
				font=("Times", 20,  "bold"))
			title.pack(fill=tk.X)
			
			empty = tk.Label(bg="black")
			empty.pack(fill=tk.X)
			
			openfile = ttk.Button(text="Open file", command=toopen)
			openfile.pack()
			
			opened = tk.Label(bg="black", fg="white", font=("Times", 7))
			opened.pack()
			
			empty = tk.Label(bg="black")
			empty.pack(fill=tk.X)
			empty = tk.Label(bg="black")
			empty.pack(fill=tk.X)
			
			showtext = tk.Text(padx=15, pady=15, height=7, wrap="word", state="disabled", font=("Times", 7))
			showtext.pack()
			
			extractbutt = ttk.Button(text="Retrieve", command=extract2)
			extractbutt.pack()
			
			cleanbutt = ttk.Button(text="Clean", command=refresh)
			cleanbutt.pack(side=tk.LEFT)
			
			exitbutt = ttk.Button(text="Exit", command=principal)
			exitbutt.pack(side=tk.RIGHT)
			
			window.mainloop()
			
		def refresh():
			window.destroy()
			startgui()
		startgui()
	
	#Widgets
	buttons_style = ttk.Style()
	buttons_style.configure('my.TButton', font=('Times', 8))
	
	'''empty = tk.Label(text="° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °")
	empty.pack(fill=tk.X)	
		
	title = tk.Label(text="-   PySnow   -",
		fg= "white",
		bg= "black",
		font=("Times", 18,  "bold"),
		height=2)
	title.pack(fill=tk.X)'''
	
	pslogo = tk.PhotoImage(file="pysnowlogo2.png")
	pssmallerlogo = pslogo.subsample(2, 2)
	ps = tk.Label(image=pssmallerlogo, bg='white')
	ps.pack(fill=tk.X)
	
	empty = tk.Label(text="° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °")
	empty.pack(fill=tk.X)
	
	empty = tk.Label(bg="black")
	empty.pack(fill=tk.X)
	
	nascondibutt = ttk.Button(text="Hide",style="my.TButton", command=hide)
	nascondibutt.pack()
	
	empty = tk.Label(bg="black")
	empty.pack(fill=tk.X)
	
	estraibutt = ttk.Button(text="Retrieve", style="my.TButton", command=extract)
	estraibutt.pack()
	
	empty = tk.Label(bg="black")
	empty.pack(fill=tk.X)
	
	empty = tk.Label(text="° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °")
	empty.pack(fill=tk.X)
	
	empty = tk.Label(bg="black", text="\n")
	empty.pack(fill=tk.X)
	
	#Image
	logo = tk.PhotoImage(file="uriel-white.png")
	smallerlogo = logo.subsample(2, 2)
	uriel = tk.Label(image=smallerlogo, bg='black')
	uriel.pack(fill=tk.X)
	
	powered = tk.Label(text="* * * * * * * * * * * * * * * *  powered by Uriel-SG  * * * * * * * * * * * * * * * *", font=("Calibri", 5))
	powered.pack(fill=tk.X, side=tk.BOTTOM)
	
	empty = tk.Label(bg="black")
	empty.pack(fill=tk.X, side=tk.BOTTOM)
	
	esci = ttk.Button(text="Exit", style="my.TButton", command=exit)
	esci.pack(side=tk.BOTTOM)
	
	finestra.mainloop()
	
snow_gui()
