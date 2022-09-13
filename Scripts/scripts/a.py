import tkinter as tk

class App():
    def __init__(self, parent):
        self.parent = parent
        self.options = ['one', 'two', 'three']

        self.om_variable = tk.StringVar(self.parent)
        self.om_variable.set(self.options[0])

        self.om = tk.OptionMenu(self.parent, self.om_variable, *self.options)
        self.om.grid(column=0, row=0)

        self.label = tk.Label(self.parent, text='Enter new option')

        self.label.grid(column=1, row=0)


    def update_option_menu(self):
        menu = self.om["menu"]
        menu.delete(0, "end")
        for string in self.options:
            menu.add_command(label=string, command=lambda value=string: self.om_variable.set(value))
        




root = tk.Tk()
App(root)
root.mainloop()
