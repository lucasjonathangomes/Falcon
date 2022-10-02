
from support import *
from Login import *

def Main():
    jan = Tk()
    jan.title('FALCON - Avaliação 360')
    jan.configure(background='white')
    jan.attributes('-alpha', 0.9)
    jan.geometry("%dx%d" % (jan.winfo_screenwidth(), jan.winfo_screenheight()))
    Login(jan)
    jan.mainloop()

if '__name__':
    Main()

