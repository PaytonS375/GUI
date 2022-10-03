# This program displays an empty window

import tkinter

class myGUI:
    def __init__(self):
        # Create the main window widget and assign it to the variable 'main window'

        self.main_window = tkinter.Tk()

        # configure the main window
        
        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        # Create the label widget containing the text 'Hello World!'
        # the 'label1' is part of the root widget 'main window'
        # this means we are creating the label in the main window
        
        self.label1 = tkinter.Label(self.main_window, text='Hello World!')
        
        # Create a second label containing the text ' This is my GUI program'
        # the 'label2' is part of the root widget 'main_window'
        
        self.label2 = tkinter.Label(self.main_window, text='This is my GUI program')

        # Call the pack method for each label
        # The pack method determines where a widget shoudl be positioned and makes
        # the widget visible when the main window is displayed

        # Call both Label widgets' pack method

        #self.label1.pack()
        #self.label2.pack()

        # Because the label1 widget was added to the main_window first, it will appear
        # at the leftmost edge. The label2 widget was added next, so it appears next to the label1 widget
        # As a result, the labels appear side by side. The valid side arguements that you can pass to the
        # pack method are side='top', side='bottom', side='left', and side='right'

        self.label1.pack(side='left')
        self.label2.pack(side='bottom')

        # Enter the tkinter main loop. This function runs like an infinite
        # loop until you close the main window

        tkinter.mainloop()

# Create an instance of the MyGUI class
my_gui = myGUI()

print('I am done!')