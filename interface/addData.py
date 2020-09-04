import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from backend.sqlpass import data as sql
import interface.userWin


class RootWin:

    def __init__(self, win, userid):
        self.userid = userid
        self.win = win
        self.win.title("Welcome to Keyper")
        self.win.geometry("500x600")
        # Screen Size
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        # Window Size and Position
        ww, wh = 500, 600
        wp, hp = (sw / 2) - (ww / 2), (sh / 2) - (wh / 2)
        self.win.geometry("{}x{}+{}+{}".format(round(ww), round(wh), round(wp), round(hp)))

        # Defining some variables
        self.data = sql()  # for sql functions from sqlpass.py

        """ Frames for Login and Signup """
        # Login Frame
        self.frameLogin = Frame(win)
        self.frameLogin.pack(fill=BOTH, padx=0, pady=0)  # initial frame is login
        # Signup Frame
        self.frameSignup = Frame(win)

        """ Login Elements """
        # Label Elements
        self.lbL = Label(self.frameLogin, text="Add new data here:")
        self.lbL.pack(pady=5)
        frmL1 = LabelFrame(self.frameLogin, text='New Data')
        frmL1.pack(fill=BOTH, padx=44, pady=20)
        frmL2 = LabelFrame(self.frameLogin)
        frmL2.pack(fill=BOTH, padx=44)
        # labels
        lbacc = Label(frmL1, text="Account")
        lbacc.grid(row=0, column=0, sticky=tk.W, pady=5)
        lbmail = Label(frmL1, text="Email")
        lbmail.grid(row=3, column=0, sticky=tk.W, pady=5)
        lbun = Label(frmL1, text="Username")
        lbun.grid(row=5, column=0, sticky=tk.W, pady=5)
        lbpw = Label(frmL1, text="Password")
        lbpw.grid(row=7, column=0, sticky=tk.W, pady=5)

        # Input Entry Elements
        self.entacc = Entry(frmL1, width=63)
        self.entacc.grid(row=2, column=0, columnspan=5, pady=5, padx=5)
        self.entacc.focus_set()
        self.entmail = Entry(frmL1, width=63)
        self.entmail.grid(row=4, column=0, columnspan=5, pady=5, padx=5)
        self.entun = Entry(frmL1, width=63)
        self.entun.grid(row=6, column=0, columnspan=5, pady=5, padx=5)
        self.entpw = Entry(frmL1, width=63)
        self.entpw.grid(row=8, column=0, columnspan=5, pady=5, padx=5)
        # Buttons
        self.loginL_btn = Button(frmL1, width=25, text='Add Data', command=self.add_data)
        self.loginL_btn.grid(row=9, column=4, sticky=tk.E, padx=5, pady=40)
        self.revealL_btn = Button(frmL1, width=25, text='Reset', command=self.reset)
        self.revealL_btn.grid(row=9, column=0, sticky=tk.E, padx=5, pady=40)
        self.signupL_btn = Button(frmL2, width=25, text='Cancel', command=self.goto_cancel)
        self.signupL_btn.pack(padx=5, pady=10)

    def add_data(self):
        """ proceed to login """
        acc = self.entacc.get()
        mail = self.entmail.get()
        username = self.entun.get()
        pasw = self.entpw.get()
        print("login button has been clicked")
        if self.check_entries:
            self.data.add_data(self.userid, acc, mail, username, pasw)
            tkinter.messagebox.showinfo("Success", "Data added")
            if tkinter.messagebox.OK:
                self.win.destroy()
                interface.userWin.main(self.userid)
        else:
            tkinter.messagebox.showinfo("Error", "Fill all info")

    def goto_cancel(self):
        """ to go back"""
        tkinter.messagebox.showinfo("Cancelled", "Data not added")
        if tkinter.messagebox.OK:
            self.win.destroy()
            interface.userWin.main(self.userid)

    def check_entries(self):
        """ to check if both password entries are same or not every key-press"""
        acc = self.entacc.get()
        mail = self.entmail.get()
        un = self.entun.get()
        pasw = self.entpw.get()
        if acc == "" or mail == "" or un == "" or pasw == "":
            if acc == " " or mail == " " or un == " " or pasw == " ":
                return True
        else:
            return False

    def reset(self):
        self.entacc.delete(0, END)
        self.entmail.delete(0, END)
        self.entun.delete(0, END)
        self.entpw.delete(0, END)


def main(userid="Apple"):
    """ Create the window"""
    win = Tk()
    RootWin(win, userid)
    win.mainloop()


if __name__ == '__main__':
    main()
