
from support import * 

class Main:
    def __init__(self, window) -> None:
        self.window = window
        self.window.title('Creation Tables in MDS')
        self.window.geometry('700x350')
        self.window.resizable(width=False, height=False)
        self.window.attributes('-alpha', 0.9)

        self.list_tables_name = [] 

        self.Create_itens()   





if '__name__':
    window = Tk()
    Main(window)
    window.mainloop()

