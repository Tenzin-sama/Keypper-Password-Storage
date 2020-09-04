import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from backend.sqlpass import data as sql


class RootWin:

    def __init__(self, win, userid):
        self.userid = userid
        self.win = win
        self.win.title("Delete data")
        # Screen Size
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        # Window Size and Position
        ww, wh = 400, 250
        wp, hp = (sw / 2) - (ww / 2), (sh / 2) - (wh / 2)
        self.win.geometry("{}x{}+{}+{}".format(round(ww), round(wh), round(wp), round(hp)))

        # Defining some variables
        self.data = sql()  # for sql functions from sqlpass.py

        """ Login Elements """
        # Label Elements
        self.lbL = Label(self.win, text="Enter Account and username to be deleted:")
        self.lbL.pack(pady=5)
        frmL1 = LabelFrame(self.win, text='Deletion details')
        frmL1.pack()
        # labels
        lbacc = Label(frmL1, text="Account")
        lbacc.grid(row=1, column=0, sticky=tk.W, pady=5)
        lbun = Label(frmL1, text="Username")
        lbun.grid(row=3, column=0, sticky=tk.W, pady=5)

        # Input Entry Elements
        self.entacc = Entry(frmL1, width=63)
        self.entacc.grid(row=2, column=0, columnspan=5, pady=5, padx=5)
        self.entacc.focus_set()
        self.entun = Entry(frmL1, width=63)
        self.entun.grid(row=4, column=0, columnspan=5, pady=5, padx=5)
        # Buttons
        self.loginL_btn = Button(frmL1, width=25, text='Delete', command=self.delete_data)
        self.loginL_btn.grid(row=9, column=4, sticky=tk.E, padx=5, pady=10)
        self.revealL_btn = Button(frmL1, width=25, text='Reset', command=self.reset)
        self.revealL_btn.grid(row=9, column=0, sticky=tk.E, padx=5, pady=10)

    def reset(self):
        self.entacc.delete(0, END)
        self.entun.delete(0, END)

    def delete_data(self):
        tkinter.messagebox.showinfo("Confirm", "Do you want to delete the data?")
        if tkinter.messagebox.OK:
            acc = self.entacc.get()
            un = self.entun.get()
            self.data.delete_item(self.userid, acc, un)
            tkinter.messagebox.showinfo("Success", "Data has been deleted")
            self.win.destroy()


def main(userid="Apple"):
    """ Create the window"""
    win = Tk()
    RootWin(win, userid)
    win.mainloop()


if __name__ == '__main__':
    main()
