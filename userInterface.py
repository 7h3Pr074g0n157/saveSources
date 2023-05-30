import tkinter as tk
import sourceHandling as sh

class mkLabel():
    def __init__(self, window, text, x=10, y=10, font=('Arial', 16)):
        self.label = tk.Label(window, text=text, font=font)
        self.label.pack(padx=x, pady=y)

class mkText(tk.Text):
    def __init__(self, window, h=2, x=10, y=10, f=('Arial', 16)):
        super().__init__()
        self.text = tk.Text(window, height=h, font=f)
        self.text.pack(padx=x, pady=y)

class mkButton():
    def __init__(self, window, text='', x=10, y=10, font=('Arial', 16), align=None, fill=None, expand=None, handler=None, args=None):
        self.button = tk.Button(window, text=text, font=font)
        self.button.pack(padx=x, pady=y, anchor=align, fill=fill, expand=expand)
        self.button.bind(
            '<Button-1>',
            lambda event, arg=args: handler(self=self, event=event, textFields=arg))

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title('saveSources')
        self.heading = mkLabel(self.root, 'saveSources', font=('Arial', 28))

        self.strTitleLabel = mkLabel(self.root, 'Title')
        self.strTitleText = mkText(self.root)

        self.strURLLabel = mkLabel(self.root, 'Source')
        self.strURLText = mkText(self.root)
        
        self.addButton = mkButton(window=self.root, text='Add Source', align='n', fill='x', expand=True, handler=sh.handleAddSource, args=[
            self.strTitleText.get('1.o', tk.END), 
            self.strURLText.get('1.0', tk.END)])

        self.root.mainloop()
