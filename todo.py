from tkinter import *
from tkinter import ttk 

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do',
              font='ariel, 25 bold', width=10,bd=5, bg='green', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Görev Ekle',
              font='ariel, 18 bold', width=10,bd=5, bg='green', fg='black')
        self.label2.place(x=1, y=70) 

        self.label3 = Label(self.root, text='Görev',
              font='ariel, 18 bold', width=10,bd=5, bg='green', fg='black')
        self.label3.place(x=256, y=70)
        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="ariel, 20 italic bold")
        self.main_text.place(x=150, y=120,)

        self.text = Text(self.root, bd=5, height=2, width=15, font='ariel, 10 bold')
        self.text.place(x=15, y=120)

        #görev ekle karşimm

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f: 
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()        
            self.main_text.delete(delete_)
            
        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close 
        
        self.button = Button(self.root, text='Ekle', font='sarif, 20 bold italic',
                  width=5, bd=5, bg='green', fg='black', command=add)
        self.button.place(x=25, y=200)

        self.button2 = Button(self.root, text='Sil', font='sarif, 20 bold italic',
                  width=5, bd=5, bg='green', fg='black', command=delete)
        self.button2.place(x=528, y=200)



def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()

