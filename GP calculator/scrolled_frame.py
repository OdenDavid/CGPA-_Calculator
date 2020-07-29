from tkinter import *

class scrollingFrame(Frame):
    def __init__(self, parentObject, background,width,height,relief,bd):
        Frame.__init__(self, parentObject, background = background, width=width,height=height,relief=relief,bd=bd)
        self.canvas = Canvas(self, borderwidth=0, background = background, width=width, height=height, highlightthickness=0)
        self.frame = Frame(self.canvas, background = background, width=width, height=height,relief=relief,bd=bd)

        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview, background=background)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=0, column=1, sticky=N+S)

        self.hsb = Scrollbar(self, orient="horizontal", command=self.canvas.xview, background=background)
        self.canvas.configure(xscrollcommand=self.hsb.set)
        self.hsb.grid(row=1, column=0, sticky=E+W)

        self.canvas.grid(row=0, column=0, sticky=N+S+E+W)
        self.window = self.canvas.create_window(0,0, window=self.frame, anchor="nw", tags="self.frame")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)         
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind("<Configure>", self.onCanvasConfigure)

    def on_mousewheel(self, event):
        shift = (event.state & 0x1) != 0
        scroll = -1 if event.delta > 0 else 1
        if shift:
            self.canvas.xview_scroll(scroll, "units")
        else:
            self.canvas.yview_scroll(scroll, "units")  
       
    def onFrameConfigure(self, event):
        #Reset the scroll region to encompass the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def onCanvasConfigure(self, event):
        #Resize the inner frame to match the canvas
        minWidth = self.frame.winfo_reqwidth()
        minHeight = self.frame.winfo_reqheight()

        if self.winfo_width() >= minWidth:
            newWidth = self.winfo_width()
            #Hide the scrollbar when not needed
            self.hsb.grid_remove()
        else:
            newWidth = minWidth
            #Show the scrollbar when needed
            self.hsb.grid()

        if self.winfo_height() >= minHeight:
            newHeight = self.winfo_height()
            #Hide the scrollbar when not needed
            self.vsb.grid_remove()
        else:
            newHeight = minHeight
            #Show the scrollbar when needed
            self.vsb.grid()

        self.canvas.itemconfig(self.window, width=newWidth, height=newHeight)
