import tkinter
import tkinter.messagebox

class myGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Frame Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)


        self.label1 = tkinter.Label(self.topframe, text='Enter the score for test 1:')
        self.score1_entry = tkinter.Entry(self.topframe, width=10)

        self.label2 = tkinter.Label(self.topframe, text='Enter the score for test 2:')
        self.score2_entry = tkinter.Entry(self.topframe, width=10)

        self.label3 = tkinter.Label(self.topframe, text='Enter the score for test 3:')
        self.score3_entry = tkinter.Entry(self.topframe, width=10)

        self.label4 = tkinter.Label(self.topframe, text='Average')

        self.label5 = tkinter.Label(self.topframe)

        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')
        self.label4.pack(side='top')
        self.label5.pack(side='top')


        self.radio_var = tkinter.IntVar()

        self.rb1 = tkinter.Radiobutton(self.topframe,text='Average', variable=self.radio_var, value=10)
        self.rb2 = tkinter.Radiobutton(self.topframe,text='Quit', variable=self.radio_var, value=20)

        self.rb1.pack(side='left')
        self.rb2.pack(side='right')


        self.topframe.pack(side='top')
        self.bottomframe.pack(side='top')


        self.mybutton = tkinter.Button(self.main_window, text='Click Me!', command=self.do_something)
        self.quitbutton = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)

        self.mybutton.pack(side='left')
        self.quitbutton.pack(side='right')


        tkinter.mainloop()


    def do_something(self):
        message = 'Your average test score is:\n'

        tkinter.messagebox.showinfo('Avg Test Score',message)


myGUI = myGUI()

print('I am done!')