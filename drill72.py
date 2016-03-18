#drill 72 creating a GUI to update website content

from tkinter import *
from tkinter import ttk
import webbrowser

class retailSite:

    def __init__(self, master):

        master.title('Retail Website Content Manager')
        master.resizable(False, False)
        master.configure(background = '#F6CED8')
        
        #styling the widgets
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#F6CED8')
        self.style.configure('TButton', background = '#F6CED8')
        self.style.configure('TLabel', background = '#F6CED8', font = ('Arial', 11, 'bold'))
        self.style.configure('Header.TLabel', background = '#F6CED8', font = ('Arial', 18, 'bold'))
        
        #frame constructor method
        self.frame_header = ttk.Frame(master)
        #pack method geometry manager
        self.frame_header.pack()

        self.logo = PhotoImage(file = 'shoe.png')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2, padx = 40)
        ttk.Label(self.frame_header, text = "Retail Website Manager", style = 'Header.TLabel').grid(row = 0, column = 1, padx= 10)
        ttk.Label(self.frame_header, text = "Update your website's content").grid(row = 1, column = 1, sticky = 'n')
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Header:').grid(row = 0, column = 0, padx = 10, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Body:').grid(row = 2, column = 0, padx = 10, sticky = 'sw')
        
        self.entry_htmlH1 = ttk.Entry(self.frame_content, width = 75, font = ('Arial', 10))
        self.text_htmlP = Text(self.frame_content, width = 75, height = 10, font = ('Ariel', 10))

        self.entry_htmlH1.grid(row= 1, column = 0, columnspan= 2, padx = 10)
        self.text_htmlP.grid(row = 3, column = 0, columnspan= 2, padx = 10)

        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 4, column = 0, padx = 10, pady = 10, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 4, column = 1, padx = 10, pady = 10, sticky = 'w')
        
    def submit(self):
        self.h1Text = self.entry_htmlH1.get()
        print (self.h1Text)
        self.pText = self.text_htmlP.get(1.0, 'end')
        print (self.pText)
        self.createHtml()
        self.clear()
        messagebox.showinfo(title = "Success!", message = "Site Content Updated!")

    def clear(self):
        self.entry_htmlH1.delete(0, 'end')
        self.text_htmlP.delete(1.0, 'end')

    def createHtml(self):
        self.html = open('index.html', 'w')
        self.content = "<html> \n<body> \n <h1> \n" + self.h1Text + "\n </h1> \n <p> \n" \
                       + self.pText + "\n </p> \n</body> \n</html>"
        self.html.write(self.content)
        self.html.close()

   
        
            
def main():
    root = Tk()
    feedback = retailSite(root)
    root.mainloop()

if __name__ == "__main__": main()
