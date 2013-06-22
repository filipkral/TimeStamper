"""This utility gives you quick access to time stamps.
You canconfigure what formats of time stamps you want and what prefix to use.
The time stamps can be used for example in file names for version control."""
# Time Stamper by Filip Kral ( http://filipkral.com ) is licensed under a Creative Commons Attribution 3.0 Unported License
# based on http://stackoverflow.com/questions/2400262/code-a-timer-in-a-python-gui-in-tkinter
# based on http://stackoverflow.com/questions/4308152/python-copy-text-to-clipboard-platform-independent
# based on http://stackoverflow.com/questions/12862445/tkinter-get-button-name

import time
import sys

if sys.version_info[0] < 3: import Tkinter as tk
else: import tkinter as tk

class App():
    def __init__(self):
        """Create the main window with a text box for prefix and as many buttons as specified in the self.formats list"""
        self.currentTime = time.localtime()
        self.root = tk.Tk()
        self.root.wm_title("Time Stamper")
        
        # prefix text box and default value
        self.prefix = tk.Entry(self.root, bd = 3)
        self.prefix.pack()
        self.prefix.insert(0, "_expired")
        self.separator = tk.Frame(height = 4, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)
        
        # CONFIGURE WHAT FORMATS SHOULD BE DISPLAYED
        # must be vaid formats for time.strftime function
        self.formats = ["%Y%m%d%H%M%S", "%Y%m%d%H%M", "%Y%m%d", "%Y-%m-%d %H:%M:%S"]
        # create button for each format
        self.buttons = []
        for i in range(len(self.formats)):
            b = tk.Button(self.root, bd = 5, height = 3)
            b.config(text=time.strftime(self.formats[i], self.currentTime), width = 20)
            self.buttons.append(b)
            self.buttons[i].config(command = lambda inx=i:self.copyToClipboard(self.buttons[inx]['text']))
            self.buttons[i].pack()
        self.updateMe()
        self.root.mainloop()
    
    def updateMe(self):
        """Update button texts with current time. To be executed every second."""
        self.currentTime = time.localtime()
        for i in range(len(self.formats)):
            self.buttons[i].config(text=time.strftime(self.formats[i], self.currentTime))
        self.root.after(1000, self.updateMe)
    
    def copyToClipboard(self, tocopy):
        """Take the prefix, join it with the text of the button that was clicked and copy it to clip board."""
        aprefix = ""
        try: aprefix =  self.prefix.get()
        except: pass
        self.root.clipboard_clear()
        self.root.clipboard_append(aprefix + tocopy)

app=App()
#app.mainloop()
