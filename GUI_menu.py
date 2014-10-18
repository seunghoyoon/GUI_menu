from Tkinter import *
#=====================================================================
class APP:
    def __init__(self,root):
               
        MENU_PAN = Menu(root)
        root.config(menu=MENU_PAN)
                  
        menu01 = Menu(MENU_PAN)
        menu02 = Menu(MENU_PAN)
        
        MENU_PAN.add_cascade(label='01',menu=menu01)
        menu01.add_command(label='0101',command=self.go_0101)
        menu01.add_cascade(label='0102',command=self.go_0102)

        MENU_PAN.add_cascade(label='02',menu=menu02)
        menu02.add_cascade(label='0201',command=self.go_0201)
        menu02.add_cascade(label='0202',command=self.go_0202)

    def go_0101(self):
        print "1_1"

    def go_0102(self):
        print "1_2"
        
    def go_0201(self):
        print "2_1"

    def go_0202(self):
        print "2_2"
        
        
        
#=====================================================================
if __name__=='__main__':
   root = Tk()
   root.title('navigation')
   root.geometry('500x200')
   APP(root) 
   root.mainloop()