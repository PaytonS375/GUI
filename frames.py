# This program creates labels in two different frames

import tkinter
import tkinter.messagebox

class myGUI:
    def __init__(self):
        # Create the main window widet
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        # Create two frames, one for the top of the
        # window, and one for the bottom
        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        # Create three Label widgets for the
        # top frame
        # These widgets are added to the self.top_frame widget
        # and not to the self.main_window widget
        self.label1 = tkinter.Label(self.topframe, text='John')
        self.label2 = tkinter.Label(self.topframe, text='Jim')
        self.label3 = tkinter.Label(self.topframe, text='Jerry')

        # Pack the labels that are in the top frame
        # Use the side='top' argument to stack them
        # one on top of the other
        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='left')

        # Create three Label widgets for the
        # bottom frame
        self.label4 = tkinter.Label(self.bottomframe, text='Jill')
        self.label5 = tkinter.Label(self.bottomframe, text='Jen')
        self.label6 = tkinter.Label(self.bottomframe, text='Jessica')

        # Pack the labels that in the bottom frame
        # Use the side='left' argument to arrange them
        # horizontally from the left of the frame
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        # Yes, we have to pack the frames too!
        self.topframe.pack()
        self.bottomframe.pack()

        # Create a Button widget, the text 'Click Me!'
        # should appear on the face of the Button
        # The do_something method should be executed when
        # the user clicks the Button
        self.mybutton = tkinter.Button(self.main_window, text='Click Me!', command=self.do_something)
        self.quitbutton = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)

        # Pack the 'click me' button
        self.mybutton.pack(side='left')
        # Pack the 'quit' button
        self.quitbutton.pack(side='right')

        # Enter the tkinter main loop
        tkinter.mainloop()


    def do_something(self):
        # Display an info dialog box

        tkinter.messagebox.showinfo('Response', 'Thanks for clicking me!')

# Create an instance of the MyGUI class
my_gui = myGUI()

print('I am done!')