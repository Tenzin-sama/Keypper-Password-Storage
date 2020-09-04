import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from backend.sqlpass import data as sql
import interface.userWin


class RootWin:

    def __init__(self, win):
        self.win = win
        self.win.title("Welcome to Keyper")
        self.win.geometry("500x550")
        # Screen Size
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        # Window Size and Position
        ww, wh = 500, 500
        wp, hp = (sw / 2) - (ww / 2), (sh / 2) - (wh / 2)
        self.win.geometry("{}x{}+{}+{}".format(round(ww), round(wh), round(wp), round(hp)))

        # Defining some variables
        self.page = "login"
        self.showLpass = False
        self.varL_ui = StringVar()
        self.varL_pw = StringVar()
        self.showSpass = False
        self.samepass = BooleanVar()
        self.varS_ui = StringVar()
        self.varS_pw = StringVar()
        self.pw_status = StringVar()
        self.user = sql()  # for sql functions from sqlpass.py

        """ Frames for Login and Signup """
        # Login Frame
        self.frameLogin = Frame(win)
        self.frameLogin.pack(fill=BOTH, padx=0, pady=0)  # initial frame is login
        # Signup Frame
        self.frameSignup = Frame(win)

        """ Login Elements """
        # Label Elements
        self.lbL = Label(self.frameLogin, text="Welcome to Keyper! Enter the details to continue")
        self.lbL.pack(pady=20)
        frmL1 = LabelFrame(self.frameLogin, text='Login Form')
        frmL1.pack(fill=BOTH, padx=44, pady=20)
        frmL2 = LabelFrame(self.frameLogin)
        frmL2.pack(fill=BOTH, padx=44)
        lbL2 = Label(frmL1, text="Username")
        lbL2.grid(row=0, column=0, sticky=tk.W, pady=5)
        lbL3 = Label(frmL1, text="Password")
        lbL3.grid(row=3, column=0, sticky=tk.W, pady=5)
        lbL4 = Label(frmL2, text="Create new account:")
        lbL4.pack(pady=10)
        # Input Entry Elements
        self.entL_ui = Entry(frmL1, width=63)
        self.entL_ui.grid(row=2, column=0, columnspan=5, pady=5, padx=5)
        self.entL_ui.focus_set()
        self.entL_pw = Entry(frmL1, width=63, show="*")
        self.entL_pw.grid(row=4, column=0, columnspan=5, pady=5, padx=5)
        # Buttons
        self.loginL_btn = Button(frmL1, width=25, text='Login', command=self.login_func)
        self.loginL_btn.grid(row=5, column=4, sticky=tk.E, padx=5, pady=40)
        self.revealL_btn = Button(frmL1, width=25, text='Reveal Password', command=self.revealLpass)
        self.revealL_btn.grid(row=5, column=0, sticky=tk.E, padx=5, pady=40)
        self.signupL_btn = Button(frmL2, width=25, text='Signup', command=self.goto_signup)
        self.signupL_btn.pack(padx=5, pady=10)

        """ Signup Elements """
        # Label Elements
        self.lb = Label(self.frameSignup, text="Enter new username and password to register a new account")
        self.lb.pack(pady=20)
        self.frm1 = LabelFrame(self.frameSignup, text='Signup Form')
        self.frm1.pack(fill=BOTH, padx=44, pady=10)
        self.frm2 = LabelFrame(self.frameSignup)
        self.frm2.pack(fill=BOTH, padx=44)
        self.lb2 = Label(self.frm1, text="Username")
        self.lb2.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.lb3 = Label(self.frm1, text="Password")
        self.lb3.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.lb3 = Label(self.frm1, text="Retype Password")
        self.lb3.grid(row=5, column=0, sticky=tk.W, pady=5)
        self.lb5 = Label(self.frm1, text="")
        self.lb5.grid(row=7, column=0, sticky=tk.W, pady=1)
        self.lb4 = Label(self.frm2, text="Already have an account?")
        self.lb4.pack(pady=5)
        # Input Entry Elements
        self.ent_ui = Entry(self.frm1, width=63)
        self.ent_ui.grid(row=2, column=0, columnspan=5, pady=5, padx=5)
        self.ent_ui.focus_set()
        self.ent_pw = Entry(self.frm1, width=63, show="*")
        self.ent_pw.grid(row=4, column=0, columnspan=5, pady=5, padx=5)
        self.ent_pw2 = Entry(self.frm1, width=63, show="*")
        self.ent_pw2.grid(row=6, column=0, columnspan=5, pady=5, padx=5)
        # Buttons
        self.login_btn = Button(self.frm1, width=25, text='Signup', command=self.signup_func)
        self.login_btn.grid(row=8, column=4, sticky=tk.E, padx=5, pady=20)
        self.reveal_btn = Button(self.frm1, width=25, text='Reveal Password', command=self.revealpass)
        self.reveal_btn.grid(row=8, column=0, sticky=tk.E, padx=5, pady=20)
        self.signup_btn = Button(self.frm2, width=25, text='Login', command=self.goto_login)
        self.signup_btn.pack(padx=5, pady=10)

        # listening to key-press for checking two password entries in signup
        self.ent_pw.bind("<KeyRelease>", self.checkbothpass)
        self.ent_pw2.bind("<KeyRelease>", self.checkbothpass)

    def login_func(self):
        """ proceed to login """
        self.varL_ui = self.entL_ui.get()
        self.varL_pw = self.entL_pw.get()
        print("login button has been clicked")
        if self.user.check_user(self.varL_ui):
            if self.user.check_pass(self.varL_ui, self.varL_pw):
                tkinter.messagebox.showinfo("Success", "Login success")
                if tkinter.messagebox.OK:
                    self.win.destroy()
                    interface.userWin.main(self.varL_ui)
            else:
                tkinter.messagebox.showinfo("Error", "Incorrect password")
        else:
            tkinter.messagebox.showinfo("Error", "Userid is incorrect")

    def signup_func(self):
        """ add new user to database"""
        ui = self.ent_ui.get()
        pw = self.ent_pw.get()
        pr = self.ent_pw2.get()
        if ui == "" or pw == "" or pr == "":
            tkinter.messagebox.showinfo("Error", "Some entries are empty. Please fill them first")
        else:
            if self.samepass:
                if not self.user.check_user(ui):
                    tkinter.messagebox.showinfo("Success", "New user added.")
                    self.user.add_user(ui, pw)
                    self.goto_login()
                else:
                    tkinter.messagebox.showinfo("Error", "User already exists")
            else:
                tkinter.messagebox.showinfo("Error", "Passwords do not match.")


    def goto_signup(self):
        """ to go to signup page"""
        self.varL_ui = self.entL_ui.get()
        self.varL_pw = self.entL_pw.get()
        self.frameLogin.pack_forget()
        self.frameSignup.pack(fill=BOTH, padx=0, pady=0)

    def goto_login(self):
        """ to go to login window after the login button is clicked"""
        self.varS_ui = self.ent_ui.get()
        self.varS_pw = self.ent_pw.get()
        print(self.varS_ui)
        print(self.varS_pw)
        self.frameSignup.pack_forget()
        self.frameLogin.pack(fill=BOTH, padx=0, pady=0)

    def revealLpass(self):
        """ to show/reveal password in Entry Box for login"""
        if not self.showLpass:
            self.entL_pw.configure(show="")
            self.revealL_btn.configure(text="Hide Password")
            self.showLpass = True
        else:
            self.entL_pw.configure(show="*")
            self.revealL_btn.configure(text="Reveal Password")
            self.showLpass = False

    def revealpass(self):
        """ to show/reveal password in Entry Box for signup"""
        if not self.showSpass:
            self.ent_pw.configure(show="")
            self.ent_pw2.configure(show="")
            self.reveal_btn.configure(text="Hide Password")
            self.showSpass = True
        else:
            self.ent_pw.configure(show="*")
            self.ent_pw2.configure(show="*")
            self.reveal_btn.configure(text="Reveal Password")
            self.showSpass = False

    def checkbothpass(self, event):
        """ to check if both password entries are same or not every key-press"""
        print(event.char)
        password = self.ent_pw.get()
        passwordr = self.ent_pw2.get()
        if password != passwordr:
            self.pw_status = "Passwords do not match"
            self.samepass = False
            self.lb5.configure(text=self.pw_status, fg="red")
        else:
            self.pw_status = "Passwords Match"
            self.lb5.configure(text=self.pw_status, fg="green")
            self.samepass = True


def main():
    """ Create the window"""
    win = Tk()
    RootWin(win)
    win.mainloop()


if __name__ == '__main__':
    main()
