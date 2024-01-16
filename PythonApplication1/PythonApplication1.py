import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_953=tk.Button(root)
        GButton_953["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_953["font"] = ft
        GButton_953["fg"] = "#000000"
        GButton_953["justify"] = "center"
        GButton_953["text"] = "START"
        GButton_953.place(x=260,y=300,width=70,height=25)
        GButton_953["command"] = self.GButton_953_command

        GLabel_186=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_186["font"] = ft
        GLabel_186["fg"] = "#333333"
        GLabel_186["justify"] = "center"
        GLabel_186["text"] = "Wellcome To Computer"
        GLabel_186.place(x=180,y=60,width=246,height=50)

        GLabel_329=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_329["font"] = ft
        GLabel_329["fg"] = "#333333"
        GLabel_329["justify"] = "center"
        GLabel_329["text"] = "Please insert Username Password"
        GLabel_329.place(x=190,y=90,width=234,height=50)

        GLineEdit_481=tk.Entry(root)
        GLineEdit_481["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_481["font"] = ft
        GLineEdit_481["fg"] = "#333333"
        GLineEdit_481["justify"] = "center"
        GLineEdit_481["text"] = "Username"
        GLineEdit_481.place(x=200,y=140,width=211,height=30)

        GLineEdit_520=tk.Entry(root)
        GLineEdit_520["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_520["font"] = ft
        GLineEdit_520["fg"] = "#333333"
        GLineEdit_520["justify"] = "center"
        GLineEdit_520["text"] = "Password"
        GLineEdit_520.place(x=200,y=190,width=211,height=30)

    def GButton_953_command(self):
        print("command")
    def on_entry_click(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry.insert(0, "")
            entry.config(fg='black')

    def on_entry_leave(self, event, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg='grey')

    def GButton_953_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
