# This program converts distances in kilometers
# to miles, the result is displayed in an info
# dialog box

import tkinter
import tkinter.messagebox

class myGUI:
    def __init__(self):

        # Create the main window
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        # Create two frames to group widgets
        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        # Create the widgets for the top frame
        self.promptlabel = tkinter.Label(self.topframe, text='Enter a distance in Kilometers')
        self.entry = tkinter.Entry(self.topframe, width=10)

        # Pack the top frame's widgets
        self.promptlabel.pack(side='left')
        self.entry.pack(side='left')

        # Pack the frames
        self.topframe.pack()
        self.bottomframe.pack()

        # Create the button widets for the main window
        self.mybutton = tkinter.Button(self.main_window, text='Convert', command=self.convert)
        self.quitbutton = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)

        # Pack the buttons
        self.mybutton.pack(side='left')
        self.quitbutton.pack(side='right')

        # Enter the tkinter main loop
        tkinter.mainloop()


    def convert(self):
        # Get the value entered by the user into the
        # kilo_entry widget
        kilo = float(self.entry.get())

        # Conver kilometers to miles
        miles = round(kilo*0.6214,2)

        # Display the results in an info dialog box
        tkinter.messagebox.showinfo('Result',str(kilo) + 'kilometers is equal to' + str(miles) + 'miles')


my_gui = myGUI()

print('I am done!')