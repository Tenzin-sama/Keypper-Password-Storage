import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from backend.sqlpass import data as sql
import interface.addData
import interface.delete_win


class UserWin:
    def __init__(self, win, userid):
        self.userid = userid
        self.win = win
        self.win.title("Keypper Dashboard")
        self.win.geometry("500x550")
        self.db = sql()
        # Screen Size
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        # Window Size and Position
        ww, wh = 500, 450
        wp, hp = (sw / 2) - (ww / 2), (sh / 2) - (wh / 2)
        self.win.geometry("{}x{}+{}+{}".format(round(ww), round(wh), round(wp), round(hp)))
        # label
        self.lbL = Label(self.win, text="Welcome to Keyper! Your saved data is below")
        self.lbL.place(x=20, y=0)

        self.lbsearch = Label(self.win, text="Search for accounts: ")
        self.lbsearch.place(x=5, y=30)

        self.ensearch = Entry(self.win, width = 30)
        self.ensearch.place(x=150, y=30)

        self.searchbtn = Button(self.win, width=8, text='Search', command=self.search_acc)
        self.searchbtn.place(x=340, y=30)
        self.resetbtn = Button(self.win, width=8, text='Reset', command=self.reset_acc)
        self.resetbtn.place(x=420, y=30)

        self.lbsort = Label(self.win, text="Sort by accounts: ")
        self.lbsort.place(x=5, y=70)
        self.ascbtn = Button(self.win, width=8, text='Ascending', command=self.sort_asc)
        self.ascbtn.place(x=150, y=70)
        self.dscbtn = Button(self.win, width=8, text='Descending', command=self.sort_dsc)
        self.dscbtn.place(x=250, y=70)
        self.defbtn = Button(self.win, width=8, text='Default', command=self.reset_acc)
        self.defbtn.place(x=350, y=70)

        # creating a frame
        self.dashboard = LabelFrame(win)
        self.dashboard.place(x=1, y=330)

        # creating treeview
        self.create_tree()
        # buttons
        self.exit_btn = Button(self.dashboard, width=10, text='Exit', command=self.goto_exit)
        self.exit_btn.grid(row=8, column=2, sticky=tk.E, padx=5, pady=20)
        self.add_btn = Button(self.dashboard, width=25, text='Add New', command=self.add_newdata)
        self.add_btn.grid(row=8, column=1, sticky=tk.E, padx=5, pady=20)
        self.del_btn = Button(self.dashboard, width=25, text='Delete', command=self.delete_data)
        self.del_btn.grid(row=8, column=0, sticky=tk.E, padx=5, pady=20)

    def create_tree(self):
        self.data_tree = ttk.Treeview(self.win, selectmode="browse", columns=('account', 'email', 'username', 'password'), show='headings')
        self.data_tree.place(x=5, y=120, height=200, width=488)

        self.vscrollbar = ttk.Scrollbar(self.data_tree, orient="vertical", command=self.data_tree.yview)
        self.vscrollbar.pack(side='right', fill='x')

        self.data_tree.configure(yscrollcommand=self.vscrollbar.set)
        self.data_tree.heading('account', text='account')
        self.data_tree.column('account', minwidth=0, width=100)
        self.data_tree.heading('email', text='email')
        self.data_tree.column('email', minwidth=0, width=100)
        self.data_tree.heading('username', text='username')
        self.data_tree.column('username', minwidth=0, width=100)
        self.data_tree.heading('password', text='password')
        self.data_tree.column('password', minwidth=0, width=100)
        self.show_data()

    def show_data(self):
        for i in self.data_tree.get_children():
            self.data_tree.delete(i)
        data = self.db.show_data(self.userid)
        for i in data:
            self.data_tree.insert('', END, values=(i[0], i[1], i[2], i[3]))

    def add_newdata(self):
         self.win.destroy()
         interface.addData.main(self.userid)

    def delete_data(self):
        interface.delete_win.main(self.userid)
        self.show_data()

    def search_acc(self):
        searchvar = self.ensearch.get()
        for i in self.data_tree.get_children():
            self.data_tree.delete(i)
        data = self.db.search_acc(self.userid, searchvar)
        for i in data:
            self.data_tree.insert('', END, values=(i[0], i[1], i[2], i[3]))

    def reset_acc(self):
        self.show_data()

    def sort_dsc(self):
        for i in self.data_tree.get_children():
            self.data_tree.delete(i)
        data = self.db.sort_dataDesc(self.userid)
        for i in data:
            self.data_tree.insert('', END, values=(i[0], i[1], i[2], i[3]))

    def sort_asc(self):
        for i in self.data_tree.get_children():
            self.data_tree.delete(i)
        data = self.db.sort_dataAsc(self.userid)
        for i in data:
            self.data_tree.insert('', END, values=(i[0], i[1], i[2], i[3]))

    def goto_exit(self):
        tkinter.messagebox.showinfo("Confirm", "Do you want to exit?")
        if tkinter.messagebox.OK:
            self.win.destroy()



def main(userid = 'Apple'):
    """ Create the window"""
    win = Tk()
    UserWin(win, userid)
    win.mainloop()


if __name__ == '__main__':
    main()
