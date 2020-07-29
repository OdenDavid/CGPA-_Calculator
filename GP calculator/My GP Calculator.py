# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3

import math

from scrolled_frame import *

#====================================Main Application Class====================================
class Gp_calculator:
    def __init__(self, master): 
        #========================Sqlite3 Database Connection=========================
        try: 
            conn = sqlite3.connect(r"data.db")
            cursor = conn.cursor()
        except FileNotFoundError:
            tkinter.messagebox.showerror("Database Error","Cannnot Open This Application\nTry Again !")    
            
        background = '#ffffff' 
        background2 = 'gray98'
        foreground = '#050716'
        master.iconbitmap("GPA.ico") #window icon
        self.master = master #root window
        self.master.title("") #window title
        self.master.configure(background=background) #window background color
        self.master.geometry('800x600') #window geometry(size)
        self.master.resizable(False,False) # resize window -> false
        
        self.welcome = Label(self.master, text = 'Welcome to\nMy GPA Calculator !',font=('arial',40,'bold'),fg=foreground,bg=background)
        self.welcome.place(x=150,y=60)
        
        def CGPA():
            for widget in self.master.winfo_children():
                if str(widget)[2] == 'b' or str(widget)[2] == 'l': # If the widget is a button or a label delete it
                    widget.place_forget()
            self.settings.configure(state=DISABLED) # Disable the settings button once you enter this function
            #=======================================================================================================================================================
            def back():
                for w in self.master.winfo_children():
                    w.destroy()
                Gp_calculator(master)
                
            self.image_left = PhotoImage(file='left.png')
            self.back = Button(self.master,image=self.image_left,bg=background,activebackground=background,bd=0,command=back)
            self.back.place(x=5,y=0)               
            
            self.main_frame = scrollingFrame(self.master,background=background,width=777,height=470,relief='sunken',bd=3)
            self.main_frame.grid(row=0, column=0, pady=25,padx=0)
                       
            #=====================================Information==============================================
            self.info_frame = Frame(self.main_frame,width=350,height=300,bg='#f1e2d3',relief='groove',bd=2)
            self.info_frame.place(x=240,y=0)            
            
            self.image0 = PhotoImage(file='caution.png')
            self.image_lbl = Label(self.info_frame,image=self.image0,bg='#f1e2d3')
            self.image_lbl.place(x=145,y=3)
            
            self.info = """
    Before you continue you need to know
    that this section helps you calculate your
   cumulative GPA(CGPA), You have to fill the 
   current CGPA space provided for it to work.
   During the process of adding semesters if 
   you add more than you want to, you can 
   delete the semester. However once you click
   the add course button you won't be able to 
   delete thesemester, So if for any reason you
   make such mistakes or you are shown an error 
    message kindly go back to the main menu to try again.
    Go to steps to find out how to best use this section"""
            
            self.info_lbl = Label(self.info_frame,text=self.info,font=('normal',10,'italic'),fg=foreground,bg='#f1e2d3')
            self.info_lbl.place(x=0,y=53)
            
            entry_list = []
            def _continue():
                self.info_frame.place_forget()
                self.add_semester.configure(state=NORMAL)
                self.master.title("Calculate your Cumulative GPA") # Configure window title
                
                self.current_frame = Frame(self.main_frame.frame,width=250,height=140,bg=background,relief='groove',bd=2)
                self.current_frame.grid(row=0,column=0,padx=290,pady=0)                
                
                #=============================================================================
                gpa_lbl = Label(self.current_frame,text='Current CGPA',font=('arial',10,'bold'),fg=foreground,bg=background)
                gpa_lbl.place(x=75,y=5)    
                
                gpa_ent = Entry(self.current_frame,font=('normal',11),width=7,bd=2,justify='right')
                gpa_ent.place(x=90,y=30) 
                entry_list.append(gpa_ent)
                
                cu_lbl = Label(self.current_frame,text='Total Credits',font=('arial',10,'bold'),fg=foreground,bg=background)
                cu_lbl.place(x=77,y=75)    
                
                cu_ent = Entry(self.current_frame,font=('normal',11),width=7,bd=2,justify='right')
                cu_ent.place(x=90,y=100) 
                entry_list.append(cu_ent)
                
                self.cgpa_btn = Button(self.master,text='Calculate CGPA',font=('normal',11,'bold'),fg=background,bg=foreground,activebackground=background,bd=2,relief='ridge',state=DISABLED)
                self.cgpa_btn.place(x=360,y=518)        
                                
            self.continue_btn = Button(self.info_frame,text='Continue',font=('normal',10,'bold'),fg='#6673f5',bg='#f1e2d3',activebackground='#f1e2d3',bd=0,command=_continue)
            self.continue_btn.place(x=145,y=267)                       
        
                
            #============================================Properties of the frame==========================================================
            add_w = add_widget2(self.master, self.main_frame, self.main_frame.frame)            
                 
            def add_semester():
                add_w.add_frame(background,background2,foreground,550,260,'raised',2,self.cgpa_btn,entry_list)
                
            self.add_semester = Button(self.master,text='+ Add Semester',font=('normal',10,'bold'),fg=background,bg=foreground,activebackground=background,bd=2,relief='ridge',state=DISABLED,command=add_semester)
            self.add_semester.place(x=365,y=0)            
                
           
        def GPA():
            for widget in self.master.winfo_children():
                if str(widget)[2] == 'b' or str(widget)[2] == 'l': # If the widget is a button or a label delete it
                    widget.place_forget()
                    
            self.settings.configure(state=DISABLED) # Disable the settings button once you enter this function
            
            self.main_frame = scrollingFrame(self.master,background=background,width=777,height=515,relief='sunken',bd=3)
            self.main_frame.grid(row=0, column=0, pady=25,padx=0)
            
            #=====================================Information==============================================
            self.info_frame = Frame(self.main_frame,width=350,height=300,bg='#f1e2d3',relief='groove',bd=2)
            self.info_frame.place(x=240,y=0)            
            
            self.image0 = PhotoImage(file='caution.png')
            self.image_lbl = Label(self.info_frame,image=self.image0,bg='#f1e2d3')
            self.image_lbl.place(x=145,y=3)
            
            self.info = """
    Before you continue you need to know
    that this section helps you calculate your
   GPA for not more than 16 semesters at
  the sametime. During the process of 
    adding semesters if you add more than
    you want to, you can delete the semester.
    However once you click the add course 
    button you won't be able to delete the 
    semester, So if for any reason you make
    such mistakes or you are shown an error 
    message kindly go back to the main menu to try again.
    Go to steps to find out how to best use this section"""
            
            self.info_lbl = Label(self.info_frame,text=self.info,font=('normal',10,'italic'),fg=foreground,bg='#f1e2d3')
            self.info_lbl.place(x=0,y=53)
            
            def _continue():
                self.info_frame.destroy()
                self.add_semester.configure(state=NORMAL)
                self.master.title("Calculate your GPA") # Configure window title
            self.continue_btn = Button(self.info_frame,text='Continue',font=('normal',10,'bold'),fg='#6673f5',bg='#f1e2d3',bd=0,command=_continue)
            self.continue_btn.place(x=145,y=267)
            
            add_w = add_widget1(self.master, background, self.main_frame, self.main_frame.frame)            
            
            def add_semester():
                add_w.add_frame(background,background2,foreground,550,260,'raised',2)
                
            self.add_semester = Button(self.master,text='+ Add Semester',font=('normal',10,'bold'),fg=background,bg=foreground,activebackground=background,bd=2,relief='ridge',state=DISABLED,command=add_semester)
            self.add_semester.place(x=365,y=0)
        
        self.back_image = PhotoImage(file='background.png')
        self.background_lbl = Label(self.master,image=self.back_image,font=('arial',40,'bold'),fg=foreground,bg=background)
        self.background_lbl.place(x=0,y=280)        
            
        self.image1 = PhotoImage(file='girl.png')
        self.CGPA = Button(self.master, image=self.image1,bg=foreground,activebackground=foreground,relief='ridge',bd=1,command=CGPA)
        self.CGPA.place(x=80,y=280)                  
        
        self.image2 = PhotoImage(file='guy.png')
        self.GPA = Button(self.master, image=self.image2,bg=foreground,activebackground=foreground,relief='ridge',bd=1,command=GPA)
        self.GPA.place(x=323,y=205)        
        
        self.image3 = PhotoImage(file='guy2.png')
        self.P_CGPA = Button(self.master, image=self.image3,bg=foreground,activebackground=foreground,relief='ridge',bd=1)
        self.P_CGPA.place(x=565,y=280)         
        
        #===================================Bottom Frame======================================
        self.control_frame = Frame(self.master,width=800,height=50,background=background2,relief='ridge',bd=2)
        self.control_frame.place(x=0,y=562)
        #Go to root folder and fetch this images
        self.photo1 = PhotoImage(file='Settings.png')
        self.photo2 = PhotoImage(file='question2.png')
        self.photo3 = PhotoImage(file='left.png')
        
        #======================Settings Function=========================
        def settings():
            for widget in self.master.winfo_children():
                if str(widget)[2] == 'b' or str(widget)[2] == 'l' or str(widget)[2] == 's': # If the widget is a button a label or a spinbox disable it
                    widget.configure(state=DISABLED)
            
            settings_frame = Frame(self.master,width=400,height=440,relief='raised',bd=3,bg=background)
            settings_frame.place(x=210,y=65)
            
            settings_lbl = Label(settings_frame,text='Settings',font=('arial',14,'bold'),fg=foreground,bg=background)
            settings_lbl.place(x=150,y=0)
            def close():
                settings_frame.place_forget()
                for widget in self.master.winfo_children():
                    if str(widget)[2] == 'b' or str(widget)[2] == 'l' or str(widget)[2] == 's': # If the widget is a button or a label disable it
                        widget.configure(state=NORMAL)    
                        
            remove_settings = Button(settings_frame, text='X',font=('arial',13,'bold'), foreground='gray60', bg=background, bd=0, activebackground=background, activeforeground=background,command=close)
            remove_settings.place(x=365,y=0)      
            
            settings_frame2 = scrollingFrame(settings_frame,background=background2,width=385,height=430,relief='flat',bd=1)
            settings_frame2.grid(row=0, column=0,pady=30,padx=0)
            
        self.settings = Button(self.control_frame, image=self.photo1, bg=background2, bd=0, activebackground=foreground,command=settings)
        self.settings.place(x=760,y=0)
       
class add_widget1(object):
    def __init__(self, master, background, scrollFrame, innerFrame):
        self.master = master
        self.innerFrame = innerFrame
        self.scrollFrame = scrollFrame
        self.background = background
            
        #=======================================================================================================================================================
        def back():
            for w in self.master.winfo_children():
                w.destroy()
            Gp_calculator(master)
            
        self.image1 = PhotoImage(file='left.png')
        self.back = Button(self.master,image=self.image1,bg=self.background,activebackground=background,bd=0,command=back)
        self.back.place(x=5,y=0)   
        
        #=======================================================================================================================================================
        #============object names============
        self.container_list = []         # A list to track the number of semesters placed on the main frame
        self.semester_names = []         # A list used to hold semester names gotten from labels
        self.id_semester = []            # A list to hold the label values of the semester 
        self.gpa_button = []             # A list to hold button values
        #========widget names============
        self.containers = {}
        self.semester_frames = {}
        self.id_frames = {}
        self.result_frames = {}
        self.id_semesters = {}
        self.add_course_buttons = {}
        self.course_counts = {}
        self.result = {}
        self.remove_frame_buttons = {} 
        self.gpa_buttons = {}
        #========Dictionaries containing lists===========
        self.courses = {}                # A dictionary to hold lists of courses(course_frame) used in each semester
        self.course_codes = {}           # A dictionary to hold lists of course codes used in each semester
        self.credit_units = {}           # A dictionary to hold lists of credit units used in each semester
        self.grades = {}                 # A dictionary to hold lists of grades used in each semester
    def add_frame(self, background, background2, foreground, width, height, relief, bd):
        """
        1. create a variable 'i' to hold the value of the number of scrolling frames on the inner frame(main scrolling frame) i.e number of semesters
        Because they are going to be multiple semesters and courses unknown to us;
        2. create a dictionary 'scrolling_frame' to hold all the object names 'semesters' to be added to the inner frame(main scrolling frame) each time this function is called
        3. create a dictionary 'id_frames' to hold all the normal frame 'id_frame' to help identify each scrolling frame
        4. create a label 'id_semester' to tell the id of a particular frame
        5. create a dictionary 'add_course_buttons' to hold all the all the button objects 'add_course' on each semester frame
        6. create a dictionary 'remove_frame_buttons' to hold all the button objects 'remove_frame' on each semester frame to remove the scrolling frame entirely 
        7. append the name of the semester frame to the 'self.semester_list' so when next the function is pressed the 'i' variable would know how many semester frames are in
           the list so to know what position to place the next semester frame   
        """           
        
        #========================Sqlite3 Database Connection=========================
        try: 
            conn = sqlite3.connect(r"data.db")
            cursor = conn.cursor()
        except FileNotFoundError:
            tkinter.messagebox.showerror("Database Error","Try Again !")            
        #=============================Semester=================================
        i = len(self.container_list)
        #========widget names============
        course_frames = {}
        course_codes = {}
        credits = {}  
        scores = {}
        grades = {}  
        remove_course_buttons = {}
                
        self.courses["course_list"+str(i)] = []             #A list that is going to be saved in the courses dictionary
        self.course_codes["course_code_list"+str(i)] = []   #A list to append each course_code widget created 
        self.credit_units["credit_unit_list"+str(i)] = []   #A list to append each credit widget created 
        self.grades["grade_list"+str(i)] = []               #A list to append each grade widget created 
        #=========================================================================================================================================================================
        self.count_label = Label(self.master,text="Semester count: "+str(len(self.semester_names)+1),font=('normal',10,'bold'),fg=foreground,background=background)
        self.count_label.place(x=670,y=0)
        #=========================================================================================================================================================================
        self.containers["container"+str(i)] = Frame(self.innerFrame,background=background,width=575,height=350,relief='flat',bd=0)
        self.containers["container"+str(i)].grid(row=0+i, column=0, padx=120, pady=30)
        
        self.id_frames["id_frame"+str(i)] = Frame(self.containers["container"+str(i)],background=background,width=555,height=30,relief=relief,bd=3)
        self.id_frames["id_frame"+str(i)].place(x=0,y=0)
        
        self.semester_frames["semester"+str(i)] = scrollingFrame(self.containers["container"+str(i)],background=background2,width=width,height=height,relief=relief,bd=bd)
        self.semester_frames["semester"+str(i)].place(x=0,y=30)
        
        self.result_frames["result_frame"+str(i)] = Frame(self.containers["container"+str(i)],background=background,width=555,height=50,relief='flat',bd=0)
        self.result_frames["result_frame"+str(i)].place(x=0,y=295)
        
        #==================ID FRAME======================
        if len(self.semester_names) == 0: #if there is 0 semester on the frame
            semester = 'Semester 1'
        if len(self.semester_names) == 1: #if there is 1 semester on the frame
            semester = 'Semester 2'
        if len(self.semester_names) == 2: #if there is 2 semester on the frame
            semester = 'Semester 3'
        if len(self.semester_names) == 3: #if there is 3 semester on the frame
            semester = 'Semester 4'
        if len(self.semester_names) == 4: #if there is 4 semester on the frame
            semester = 'Semester 5'
        if len(self.semester_names) == 5: #if there is 5 semester on the frame
            semester = 'Semester 6'
        if len(self.semester_names) == 6: #if there is 6 semester on the frame
            semester = 'Semester 7'
        if len(self.semester_names) == 7: #if there is 7 semester on the frame
            semester = 'Semester 8'
        if len(self.semester_names) == 8: #if there is 8 semester on the frame
            semester = 'Semester 9'
        if len(self.semester_names) == 9: #if there is 9 semester on the frame
            semester = 'Semester 10'
        if len(self.semester_names) == 10: #if there is 10 semester on the frame
            semester = 'Semester 11'
        if len(self.semester_names) == 11: #if there is 11 semester on the frame
            semester = 'Semester 12'
        if len(self.semester_names) == 12: #if there is 12 semester on the frame
            semester = 'Semester 13'
        if len(self.semester_names) == 13: #if there is 13 semester on the frame
            semester = 'Semester 14'
        if len(self.semester_names) == 14: #if there is 14 semester on the frame
            semester = 'Semester 15'
        if len(self.semester_names) == 15: #if there is 15 semester on the frame  #"Semester "+str(i+1)
            semester = 'Semester 16'                                                                   
        
        
        self.id_semesters["id_semester"+str(i)] = Label(self.id_frames["id_frame"+str(i)],text=semester,font=('normal',11,'bold'),fg=foreground,background=background)
        self.id_semesters["id_semester"+str(i)].place(x=5,y=0)
        
        def add_course():
            """
            1. create Labels to help identify entries to be filled inside each semester frame
            2. create a variable 'n' to hold  the number of courses being added to each semester frame each time this function is being called
            3. create a dictionary 'course_frames' to hold all label_frame objects
            4. create a dictionary 'course_codes' to hold all course_code entry objects which are placed in the label_frame
            5. create a dictionary 'credits' to hold all credit spinbox objects which are placed in the label_frame
            6. create a dictionary 'scores' to hold all scores entry objects which are placed in the label_frame
            7. create a dictionary 'grades' to hold all grades combobox objects which are placed in the label_frame"""
            course_code_lbl = Label(self.semester_frames["semester"+str(i)].frame,text='Course code',font=('normal',10),fg=foreground,bg=background2).place(x=60,y=0)
            course_code_opt_lbl = Label(self.semester_frames["semester"+str(i)].frame,text='(optional)',font=('normal',8,'italic'),fg=foreground,bg=background2).place(x=135,y=1) 
            credit_unit_lbl = Label(self.semester_frames["semester"+str(i)].frame,text='Credit unit',font=('normal',10),fg=foreground,bg=background2).place(x=230,y=0)
            credit_unit_imp_lbl = Label(self.semester_frames["semester"+str(i)].frame,text='*',font=('normal',10,'bold'),fg='red',bg=background2).place(x=293,y=2)
            score_grade_lbl = Label(self.semester_frames["semester"+str(i)].frame,text='Score/100   or   Grade',font=('normal',10),fg=foreground,bg=background2).place(x=355,y=0)
            score_grade_imp_lbl = Label(self.semester_frames["semester"+str(i)].frame,text='*',font=('normal',10,'bold'),fg='red',bg=background2).place(x=488,y=2)
            #============================Courses=============================           
            n = len(self.courses["course_list"+str(i)])
            
            if n == 0: # meaning the first course is being placed
                y_index = 18
            else: 
                y_index = 0
            
            course_frames["course_frame"+str(n)] = Frame(self.semester_frames["semester"+str(i)].frame,width=530,height=45,bg=background2,relief='sunken',bd=1)
            course_frames["course_frame"+str(n)].grid(row=0+n, column=0, padx=10, pady=y_index)
            
            course_codes["course_code"+str(n)] = Entry(course_frames["course_frame"+str(n)],font=('normal',10),width=15,relief='groove',bd=2)
            course_codes["course_code"+str(n)].place(x=60,y=10)
            
            credits["credit"+str(n)] = Spinbox(course_frames["course_frame"+str(n)],font=('normal',9),width=6,from_= 0, to= 15,bd=1,justify='right')
            credits["credit"+str(n)].place(x=225,y=10)
            
            #============================Database============================
            cursor.execute("SELECT * FROM grades")
            all_grades = cursor.fetchall()
            for grade in all_grades:
                A = grade[0]
                B = grade[1]
                C = grade[2]
                D = grade[3]
                E = grade[4]
                F = grade[5]
           
            def change(*args,**kwargs):
                _score = score.get()
                if _score == "":
                    grades["grade"+str(n)].delete(0,END)
                
                elif int(_score) >= int(A):
                    grades["grade"+str(n)].insert(0,"A")
                    
                elif int(_score) >=int(B) and int(_score)<=int(A)-1:
                    grades["grade"+str(n)].insert(0,"B")
                    
                elif int(_score) >=int(C) and int(_score)<=int(B)-1:
                    grades["grade"+str(n)].insert(0,"C") 
                    
                elif int(_score) >=int(D) and int(_score)<=int(C)-1:
                    grades["grade"+str(n)].insert(0,"D")   
                    
                elif int(_score) >=int(E) and int(_score)<=int(D)-1:
                    grades["grade"+str(n)].insert(0,"E")
                    
                elif int(_score) >= 10 and int(_score)<=int(E)-1:
                    grades["grade"+str(n)].insert(0,"F")                   
                    
            
            score = StringVar()
            score.trace("w", lambda l, idx, mode: change())   
            
            scores["score"+str(n)] = Entry(course_frames["course_frame"+str(n)],textvariable=score,font=('normal',9),width=7,relief='groove',bd=2,justify='right')
            scores["score"+str(n)].place(x=350,y=10)    

            grades["grade"+str(n)] = ttk.Combobox(course_frames["course_frame"+str(n)],font=('normal',9),width=4,justify='right')
            grades["grade"+str(n)]['values'] = ['A','B','C','D','E','F']
            grades["grade"+str(n)].place(x=435,y=10)
            
            def remove_course():
                """ Remove the last course_frame and it's children irrespective of the remove button pressed
                   1. Create a variable 'temp_frame' to store the last course_frame in the self.courses list
                   2. Remove that frame from the semester frame by 'grid_forget()'
                   3. Remove the frame from the list too
                   4. Configure the course count to be equated to the current length of courses list
                   5. Configure the semester frame to adjust after the course frame has been removed"""
                temp_frame = self.courses["course_list"+str(i)][-1] 
                temp_frame.grid_forget()
                
                self.courses["course_list"+str(i)].remove(self.courses["course_list"+str(i)][-1])                        # Remove the last item from this list
                self.course_codes["course_code_list"+str(i)].remove(self.course_codes["course_code_list"+str(i)][-1])    # Remove the last item from this list
                self.credit_units["credit_unit_list"+str(i)].remove(self.credit_units["credit_unit_list"+str(i)][-1])    # Remove the last item from this list
                self.grades["grade_list"+str(i)].remove(self.grades["grade_list"+str(i)][-1])                            # Remove the last item from this list
                
                course_codes.popitem()
                credits.popitem()
                scores.popitem()
                grades.popitem()
                
                self.course_counts["course_count"+str(i)].configure(text = str(len(self.courses["course_list"+str(i)])))
                
                self.semester_frames["semester"+str(i)].frame.update_idletasks()    
                self.semester_frames["semester"+str(i)].onCanvasConfigure(None)         
                
            if n != 0:
                remove_course_buttons["remove_course"+str(n)] = Button(course_frames["course_frame"+str(n)],text='X',font=('arial',9,'bold'),fg='gray60',background=background2,activebackground=background2,bd=0,command=remove_course)
                remove_course_buttons["remove_course"+str(n)].place(x=510,y=10)            
            else:
                pass
               
            self.courses["course_list"+str(i)].append(course_frames["course_frame"+str(n)])              # Append the course_frame widget created when this function is called to the course_list
            self.course_codes["course_code_list"+str(i)].append(course_codes["course_code"+str(n)])      # Append the course_code widget created when this function is called to the course_codes_list
            self.credit_units["credit_unit_list"+str(i)].append(credits["credit"+str(n)])                # Append the credit widget created when this function is called to the credits_list
            self.grades["grade_list"+str(i)].append(grades["grade"+str(n)])                              # Append the grade widget created when this function is called to the grades_list
            
            self.semester_frames["semester"+str(i)].frame.update_idletasks()
            self.semester_frames["semester"+str(i)].onCanvasConfigure(None)  

            #=================Disable Remove frame button once this function is called=================
            def do_nothing(event):
                pass
            self.remove_frame_buttons["remove_frame"+str(i)].place_forget()
            self.remove_frame_buttons["remove_frame"+str(i)].bind('<Button-1>',do_nothing)
                        
            #=====================Course Count=======================
            self.course_counts["course_count"+str(i)] = Label(self.id_frames["id_frame"+str(i)],text=str(len(self.courses["course_list"+str(i)])),font=('normal',10,'bold'),fg=foreground,bg=background)
            self.course_counts["course_count"+str(i)].place(x=530,y=0)
            
            #===================Calculate GPA========================"Semester"+str(i+1)
            def gpa(event):            
                
                course_list = [] # A list to hold actual course code values entered by the user; will range in one
                credit_list = [] # A list to hold actual credit unit values entered by the user; will range in two 
                grade_list = [] # A list to hold actual grade values entered by the user; will range in three                
                
                #--------------------------------Handle Course Code---------------------------------------
                course_entries = list(course_codes.values()) # Create a list to append entry variales of course codes for a particular semester
                for one in range(0,len(course_entries)):
                    course_list.append(course_entries[one].get())
                
                #--------------------------------Handle Credit Unit---------------------------------------
                credit_entries = list(credits.values()) # Create a list to append entry variales of credit units for a particular semester
                for two in range(0,len(credit_entries)):
                    credit_list.append(credit_entries[two].get())
                
                try: #convert all items in this list to integer
                    credit_list = [int(a) for a in credit_list]
                except ValueError: 
                    tkinter.messagebox.showerror("Entry error","Please confirm your credit units are numbers")                
                
                #------------------------------------Handle Grades-----------------------------------------
                grade_entries = list(grades.values()) # Create a list to append entry variales of grades for a particular semester
                for three in range(0,len(grade_entries)):
                    grade_list.append(grade_entries[three].get())                  
                
                grade_list2 = [] # A list to hold integer representations of grades
                for b in range(0,len(grade_list)):
                    if grade_list[b] == "A":
                        grade_list2.append(5)
                    elif grade_list[b] == "B":
                        grade_list2.append(4)
                    elif grade_list[b] == "C":
                        grade_list2.append(3)
                    elif grade_list[b] == "D":
                        grade_list2.append(2) 
                    elif grade_list[b] == "E":
                        grade_list2.append(1)
                    elif grade_list[b] == "F":
                        grade_list2.append(0)                                      
                    else:
                        tkinter.messagebox.showerror("Entry error","Missing your grades\nPlease confirm")
                #--------------------------------------5.0 GPA calculation----------------------------------
                quality_point = [] 
                if len(grade_list2) == len(credit_list):
                    for c in range(0,len(grade_list2)):
                        quality_point.append(grade_list2[c] * credit_list[c])
                else:
                    tkinter.messagebox.showerror("Entry error","Confirm credit unit and\ngrade entries are entered correctly")
                
                sum1 = sum(credit_list)
                sum2 = sum(quality_point)
                
                my_gpa = sum2/sum1
                
                if float(my_gpa) > 2.50:
                    color = 'green' 
                elif float(my_gpa) < 2.50:
                    color = 'red'
                self.result["gpa"+str(i)] = Label(self.result_frames["result_frame"+str(i)],text=str(round(my_gpa,2)),font=('normal',13,'bold'),justify='left',fg=color,bg=background,relief='groove',bd=2)
                self.result["gpa"+str(i)].place(x=515,y=0)                
            
            self.gpa_buttons["gpa"+str(i)] = Button(self.result_frames["result_frame"+str(i)],text=semester+" GPA",font=('arial',10,'bold'),fg=background,bg=foreground,activebackground=foreground,activeforeground=background,relief='ridge',bd=2)
            self.gpa_buttons["gpa"+str(i)].bind('<Button-1>', gpa)
            self.gpa_buttons["gpa"+str(i)].place(x=245,y=0)  
            
        self.add_course_buttons["add_course"+str(i)] = Button(self.id_frames["id_frame"+str(i)],text='+ Add Course',font=('normal',9,'bold'),fg=background,bg=foreground,activebackground=background,bd=2,relief='ridge',command=add_course)
        self.add_course_buttons["add_course"+str(i)].place(x=250,y=0)
        
        def remove_semester(event):
            """1. Pass event as an argument into this function inorder to track what button calls this function
               2. Each time this function is called delete the frame that contains the semester selected from the 'self.containers' dictionary
               3. Remove the last item of the list 'self.semester_names' each time this function is called
               4. Create a for loop to iterate through the 'self.id_semester' list getting each label value
               4.1. Insisde this for loop use the 'event.widget' statement to get the the button value that is pressed, then slice it to get the index  
               4.2. Also slice each value of the 'self.id_semester' list and check if any matches the index result matches 4.1. if it does remove that value from the list
               5. Each time you call this function i.e each time a semester frame is deleted re-adjust the frames below it to fit to size
               6. Each time you call this function re-adjust the scrollable frame
               7. After the semester frame has been deleted, create a for loop to range through the length of semester frames left 
               7.1. Inside this for loop change the text of the labels on all semester frames
               8. Put all the above code in a try block, except there is an IndexError continue""" 
           
            try:
                self.containers["container"+str(i)].grid_forget()
    
                self.semester_names.remove(self.semester_names[-1]) 
                for id_value in self.id_semester:
                    if str(event.widget)[-17] == str(id_value)[-15]:
                        self.id_semester.remove(id_value)
                
                self.innerFrame.update_idletasks()
                self.scrollFrame.onCanvasConfigure(None)      
                
                for c in range(0, len(self.id_semester)):
                    self.id_semester[c]['text'] = self.semester_names[c]
                
                self.count_label.configure(text="Semester count: "+str(len(self.semester_names)))
            except IndexError:
                tkinter.messagebox.showerror("Index Error","Oops, something went wrong!!!\nGo back to home page and try again")
                #------------Go back-------------
                for w in self.master.winfo_children():
                    w.destroy()
                Gp_calculator(self.master)                
                                                                                                                                                                               
        
        self.remove_frame_buttons["remove_frame"+str(i)] = Button(self.id_frames["id_frame"+str(i)],text='X',font=('arial',10,'bold'),fg='gray60',bg=background,activebackground=background,bd=0)
        self.remove_frame_buttons["remove_frame"+str(i)].bind('<Button-1>',remove_semester)
        self.remove_frame_buttons["remove_frame"+str(i)].place(x=530,y=0) 

        
        self.container_list = list(self.containers.keys())
        
        self.semester_names.append(self.id_semesters["id_semester"+str(i)]['text'])
        self.id_semester = list(self.id_semesters.values())
        self.gpa_button = list(self.gpa_buttons.values())
        
        self.innerFrame.update_idletasks()
        self.scrollFrame.onCanvasConfigure(None)    


class add_widget2(object):
    def __init__(self, master, scrollFrame, innerFrame):
        self.master = master
        self.innerFrame = innerFrame
        self.scrollFrame = scrollFrame

        self.container = {}
        self.frame = {} 
        self.TCU = {} # Total credit units
        self.TQP = {} # Total quality points
        

        #=======================================================================================================================================================
        #============object names============
        self.container_list = []         # A list to track the number of semesters placed on the main frame
        self.semester_names = []         # A list used to hold semester names gotten from labels
        self.id_semester = []            # A list to hold the label values of the semester 
        self.gpa_button = []             # A list to hold button values
        #========widget names============
        self.containers = {}
        self.semester_frames = {}
        self.id_frames = {}
        self.result_frames = {}
        self.id_semesters = {}
        self.add_course_buttons = {}
        self.course_counts = {}
        self.result = {}
        self.remove_frame_buttons = {} 
        self.gpa_buttons = {}
        #========Dictionaries containing lists===========
        self.courses = {}                # A dictionary to hold lists of courses(course_frame) used in each semester
        self.course_codes = {}           # A dictionary to hold lists of course codes used in each semester
        self.credit_units = {}           # A dictionary to hold lists of credit units used in each semester
        self.grades = {}                 # A dictionary to hold lists of grades used in each semester        
        
    def add_frame(self, background, background2, foreground, width, height, relief, bd, cgpa_btn, entry_list):
         #========================Sqlite3 Database Connection=========================
        try: 
            conn = sqlite3.connect(r"data.db")
            cursor = conn.cursor()
        except FileNotFoundError:
            tkinter.messagebox.showerror("Database Error","Try Again !")            
          
        #=============================Semester=================================
        i = len(self.container_list)
        #========widget names============
        course_frames = {}
        course_codes = {}
        credits = {}  
        scores = {}
        grades = {}  
        remove_course_buttons = {}
                
        self.courses["course_list"+str(i)] = []             #A list that is going to be saved in the courses dictionary
        self.course_codes["course_code_list"+str(i)] = []   #A list to append each course_code widget created 
        self.credit_units["credit_unit_list"+str(i)] = []   #A list to append each credit widget created 
        self.grades["grade_list"+str(i)] = []               #A list to append each grade widget created 
        #=========================================================================================================================================================================
        self.count_label = Label(self.master,text="Semester count: "+str(len(self.semester_names)+1),font=('normal',10,'bold'),fg=foreground,background=background)
        self.count_label.place(x=670,y=0)
        #=========================================================================================================================================================================
        self.containers["container"+str(i)] = Frame(self.innerFrame,background=background,width=575,height=350,relief='flat',bd=0)
        self.containers["container"+str(i)].grid(row=1+i, column=0, padx=120, pady=17)
        
        self.id_frames["id_frame"+str(i)] = Frame(self.containers["container"+str(i)],background=background,width=555,height=30,relief=relief,bd=3)
        self.id_frames["id_frame"+str(i)].place(x=0,y=0)
        
        self.semester_frames["semester"+str(i)] = scrollingFrame(self.containers["container"+str(i)],background=background2,width=width,height=height,relief=relief,bd=bd)
        self.semester_frames["semester"+str(i)].place(x=0,y=30)
        
        self.result_frames["result_frame"+str(i)] = Frame(self.containers["container"+str(i)],background=background,width=555,height=50,relief='flat',bd=0)
        self.result_frames["result_frame"+str(i)].place(x=0,y=295)
        
        #==================ID FRAME======================
        if len(self.semester_names) == 0: #if there is 0 semester on the frame
            semester = 'Semester 1'
        if len(self.semester_names) == 1: #if there is 1 semester on the frame
            semester = 'Semester 2'
        if len(self.semester_names) == 2: #if there is 2 semester on the frame
            semester = 'Semester 3'
        if len(self.semester_names) == 3: #if there is 3 semester on the frame
            semester = 'Semester 4'
        if len(self.semester_names) == 4: #if there is 4 semester on the frame
            semester = 'Semester 5'
        if len(self.semester_names) == 5: #if there is 5 semester on the frame
            semester = 'Semester 6'
        if len(self.semester_names) == 6: #if there is 6 semester on the frame
            semester = 'Semester 7'
        if len(self.semester_names) == 7: #if there is 7 semester on the frame
            semester = 'Semester 8'
        if len(self.semester_names) == 8: #if there is 8 semester on the frame
            semester = 'Semester 9'
        if len(self.semester_names) == 9: #if there is 9 semester on the frame
            semester = 'Semester 10'
        if len(self.semester_names) == 10: #if there is 10 semester on the frame
            semester = 'Semester 11'
        if len(self.semester_names) == 11: #if there is 11 semester on the frame
            semester = 'Semester 12'
        if len(self.semester_names) == 12: #if there is 12 semester on the frame
            semester = 'Semester 13'
        if len(self.semester_names) == 13: #if there is 13 semester on the frame
            semester = 'Semester 14'
        if len(self.semester_names) == 14: #if there is 14 semester on the frame
            semester = 'Semester 15'
        if len(self.semester_names) == 15: #if there is 15 semester on the frame  #"Semester "+str(i+1)
            semester = 'Semester 16'                                                                   
        
        
        self.id_semesters["id_semester"+str(i)] = Label(self.id_frames["id_frame"+str(i)],text=semester,font=('normal',11,'bold'),fg=foreground,background=background)
        self.id_semesters["id_semester"+str(i)].place(x=5,y=0)
        
        def add_course():
            """
            1. create Labels to help identify entries to be filled inside each semester frame
            2. create a variable 'n' to hold  the number of courses being added to each semester frame each time this function is being called
            3. create a dictionary 'course_frames' to hold all label_frame objects
            4. create a dictionary 'course_codes' to hold all course_code entry objects which are placed in the label_frame
            5. create a dictionary 'credits' to hold all credit spinbox objects which are placed in the label_frame
            6. create a dictionary 'scores' to hold all scores entry objects which are placed in the label_frame
            7. create a dictionary 'grades' to hold all grades combobox objects which are placed in the label_frame"""
            course_code_lbl = Label(self.semester_frames["semester"+str(i)].frame,text='Course code',font=('normal',10),fg=foreground,bg=background2).place(x=60,y=0)
            course_code_opt_lbl = Label(self.semester_frames["semester"+str(i)].frame,text='(optional)',font=('normal',8,'italic'),fg=foreground,bg=background2).place(x=135,y=1) 
            credit_unit_lbl = Label(self.semester_frames["semester"+str(i)].frame,text='Credit unit',font=('normal',10),fg=foreground,bg=background2).place(x=230,y=0)
            credit_unit_imp_lbl = Label(self.semester_frames["semester"+str(i)].frame,text='*',font=('normal',10,'bold'),fg='red',bg=background2).place(x=293,y=2)
            score_grade_lbl = Label(self.semester_frames["semester"+str(i)].frame,text='Score/100   or   Grade',font=('normal',10),fg=foreground,bg=background2).place(x=355,y=0)
            score_grade_imp_lbl = Label(self.semester_frames["semester"+str(i)].frame,text='*',font=('normal',10,'bold'),fg='red',bg=background2).place(x=488,y=2)
            #============================Courses=============================           
            n = len(self.courses["course_list"+str(i)])
            
            if n == 0: # meaning the first course is being placed
                y_index = 18
            else: 
                y_index = 0
            
            course_frames["course_frame"+str(n)] = Frame(self.semester_frames["semester"+str(i)].frame,width=530,height=45,bg=background2,relief='sunken',bd=1)
            course_frames["course_frame"+str(n)].grid(row=0+n, column=0, padx=10, pady=y_index)
            
            course_codes["course_code"+str(n)] = Entry(course_frames["course_frame"+str(n)],font=('normal',10),width=15,relief='groove',bd=2)
            course_codes["course_code"+str(n)].place(x=60,y=10)
            
            credits["credit"+str(n)] = Spinbox(course_frames["course_frame"+str(n)],font=('normal',9),width=6,from_= 0, to= 15,bd=1,justify='right')
            credits["credit"+str(n)].place(x=225,y=10)
            
            #============================Database============================
            cursor.execute("SELECT * FROM grades")
            all_grades = cursor.fetchall()
            for grade in all_grades:
                A = grade[0]
                B = grade[1]
                C = grade[2]
                D = grade[3]
                E = grade[4]
                F = grade[5]
           
            def change(*args,**kwargs):
                _score = score.get()
                if _score == "":
                    grades["grade"+str(n)].delete(0,END)
                
                elif int(_score) >= int(A):
                    grades["grade"+str(n)].insert(0,"A")
                    
                elif int(_score) >=int(B) and int(_score)<=int(A)-1:
                    grades["grade"+str(n)].insert(0,"B")
                    
                elif int(_score) >=int(C) and int(_score)<=int(B)-1:
                    grades["grade"+str(n)].insert(0,"C") 
                    
                elif int(_score) >=int(D) and int(_score)<=int(C)-1:
                    grades["grade"+str(n)].insert(0,"D")   
                    
                elif int(_score) >=int(E) and int(_score)<=int(D)-1:
                    grades["grade"+str(n)].insert(0,"E")
                    
                elif int(_score) >= 10 and int(_score)<=int(E)-1:
                    grades["grade"+str(n)].insert(0,"F")                   
                    
            
            score = StringVar()
            score.trace("w", lambda l, idx, mode: change())   
            
            scores["score"+str(n)] = Entry(course_frames["course_frame"+str(n)],textvariable=score,font=('normal',9),width=7,relief='groove',bd=2,justify='right')
            scores["score"+str(n)].place(x=350,y=10)    

            grades["grade"+str(n)] = ttk.Combobox(course_frames["course_frame"+str(n)],font=('normal',9),width=4,justify='right')
            grades["grade"+str(n)]['values'] = ['A','B','C','D','E','F']
            grades["grade"+str(n)].place(x=435,y=10)
            
            def remove_course():
                """ Remove the last course_frame and it's children irrespective of the remove button pressed
                   1. Create a variable 'temp_frame' to store the last course_frame in the self.courses list
                   2. Remove that frame from the semester frame by 'grid_forget()'
                   3. Remove the frame from the list too
                   4. Configure the course count to be equated to the current length of courses list
                   5. Configure the semester frame to adjust after the course frame has been removed"""
                temp_frame = self.courses["course_list"+str(i)][-1] 
                temp_frame.grid_forget()
                
                self.courses["course_list"+str(i)].remove(self.courses["course_list"+str(i)][-1])                        # Remove the last item from this list
                self.course_codes["course_code_list"+str(i)].remove(self.course_codes["course_code_list"+str(i)][-1])    # Remove the last item from this list
                self.credit_units["credit_unit_list"+str(i)].remove(self.credit_units["credit_unit_list"+str(i)][-1])    # Remove the last item from this list
                self.grades["grade_list"+str(i)].remove(self.grades["grade_list"+str(i)][-1])                            # Remove the last item from this list
                
                course_codes.popitem()
                credits.popitem()
                scores.popitem()
                grades.popitem()
                
                self.course_counts["course_count"+str(i)].configure(text = str(len(self.courses["course_list"+str(i)])))
                
                self.semester_frames["semester"+str(i)].frame.update_idletasks()    
                self.semester_frames["semester"+str(i)].onCanvasConfigure(None)         
                
            if n != 0:
                remove_course_buttons["remove_course"+str(n)] = Button(course_frames["course_frame"+str(n)],text='X',font=('arial',9,'bold'),fg='gray60',background=background2,activebackground=background2,bd=0,command=remove_course)
                remove_course_buttons["remove_course"+str(n)].place(x=510,y=10)            
            else:
                pass
               
            self.courses["course_list"+str(i)].append(course_frames["course_frame"+str(n)])              # Append the course_frame widget created when this function is called to the course_list
            self.course_codes["course_code_list"+str(i)].append(course_codes["course_code"+str(n)])      # Append the course_code widget created when this function is called to the course_codes_list
            self.credit_units["credit_unit_list"+str(i)].append(credits["credit"+str(n)])                # Append the credit widget created when this function is called to the credits_list
            self.grades["grade_list"+str(i)].append(grades["grade"+str(n)])                              # Append the grade widget created when this function is called to the grades_list
            
            self.semester_frames["semester"+str(i)].frame.update_idletasks()
            self.semester_frames["semester"+str(i)].onCanvasConfigure(None)  

            #=================Disable Remove frame button once this function is called=================
            def do_nothing(event):
                pass
            self.remove_frame_buttons["remove_frame"+str(i)].place_forget()
            self.remove_frame_buttons["remove_frame"+str(i)].bind('<Button-1>',do_nothing)
                        
            #=====================Course Count=======================
            self.course_counts["course_count"+str(i)] = Label(self.id_frames["id_frame"+str(i)],text=str(len(self.courses["course_list"+str(i)])),font=('normal',10,'bold'),fg=foreground,bg=background)
            self.course_counts["course_count"+str(i)].place(x=530,y=0)
            
           
        self.add_course_buttons["add_course"+str(i)] = Button(self.id_frames["id_frame"+str(i)],text='+ Add Course',font=('normal',9,'bold'),fg=background,bg=foreground,activebackground=background,bd=2,relief='ridge',command=add_course)
        self.add_course_buttons["add_course"+str(i)].place(x=250,y=0)
        
        def remove_semester(event):
            """1. Pass event as an argument into this function inorder to track what button calls this function
               2. Each time this function is called delete the frame that contains the semester selected from the 'self.containers' dictionary
               3. Remove the last item of the list 'self.semester_names' each time this function is called
               4. Create a for loop to iterate through the 'self.id_semester' list getting each label value
               4.1. Insisde this for loop use the 'event.widget' statement to get the the button value that is pressed, then slice it to get the index  
               4.2. Also slice each value of the 'self.id_semester' list and check if any matches the index result matches 4.1. if it does remove that value from the list
               5. Each time you call this function i.e each time a semester frame is deleted re-adjust the frames below it to fit to size
               6. Each time you call this function re-adjust the scrollable frame
               7. After the semester frame has been deleted, create a for loop to range through the length of semester frames left 
               7.1. Inside this for loop change the text of the labels on all semester frames
               8. Put all the above code in a try block, except there is an IndexError continue""" 
           
            try:
                self.containers["container"+str(i)].grid_forget()
                self.container_list.remove(self.container_list[-1])
                
                self.semester_names.remove(self.semester_names[-1]) 
                for id_value in self.id_semester:
                    if str(event.widget)[-17] == str(id_value)[-15]:
                        self.id_semester.remove(id_value)
                
                self.innerFrame.update_idletasks()
                self.scrollFrame.onCanvasConfigure(None)      
                
                for c in range(0, len(self.id_semester)):
                    self.id_semester[c]['text'] = self.semester_names[c]
                
                self.count_label.configure(text="Semester count: "+str(len(self.semester_names)))
            except IndexError:
                tkinter.messagebox.showerror("Index Error","Oops, something went wrong!!!\nGo back to home page and try again")
                #------------Go back-------------
                for w in self.master.winfo_children():
                    w.destroy()
                Gp_calculator(self.master)                
                                                                                                                                                                               
        
        self.remove_frame_buttons["remove_frame"+str(i)] = Button(self.id_frames["id_frame"+str(i)],text='X',font=('arial',10,'bold'),fg='gray60',bg=background,activebackground=background,bd=0)
        self.remove_frame_buttons["remove_frame"+str(i)].bind('<Button-1>',remove_semester)
        self.remove_frame_buttons["remove_frame"+str(i)].place(x=530,y=0) 

        
        self.container_list = list(self.containers.keys())
        
        self.semester_names.append(self.id_semesters["id_semester"+str(i)]['text'])
        self.id_semester = list(self.id_semesters.values())
        self.gpa_button = list(self.gpa_buttons.values())
        
        self.innerFrame.update_idletasks()
        self.scrollFrame.onCanvasConfigure(None)          
        
        def cgpa():
            all_credits = []
            all_quality_points = []
            
            for a in range(0, len(self.container_list)):
                #===================Calculate GPA========================
               
                course_list = [] # A list to hold actual course code values entered by the user; will range in one
                credit_list = [] # A list to hold actual credit unit values entered by the user; will range in two 
                grade_list = [] # A list to hold actual grade values entered by the user; will range in three                
                
                #--------------------------------Handle Course Code---------------------------------------
                course_entries = list(list(self.course_codes.values())[a]) # Create a list to append entry variales of course codes for a particular semester
 
                for one in range(0,len(course_entries)):
                    course_list.append(course_entries[one].get())

                #--------------------------------Handle Credit Unit---------------------------------------
                credit_entries = list(list(self.credit_units.values())[a]) # Create a list to append entry variales of credit units for a particular semester
                for two in range(0,len(credit_entries)):
                    credit_list.append(credit_entries[two].get())
                
                try: #convert all items in this list to integer
                    credit_list = [int(a) for a in credit_list]
                except ValueError: 
                    tkinter.messagebox.showerror("Entry error","Please confirm your credit units are numbers")                
                
                #------------------------------------Handle Grades-----------------------------------------
                grade_entries =  list(list(self.grades.values())[a]) # Create a list to append entry variales of grades for a particular semester
                for three in range(0,len(grade_entries)):
                    grade_list.append(grade_entries[three].get())                  
                
                grade_list2 = [] # A list to hold integer representations of grades
                for b in range(0,len(grade_list)):
                    if grade_list[b] == "A":
                        grade_list2.append(5)
                    elif grade_list[b] == "B":
                        grade_list2.append(4)
                    elif grade_list[b] == "C":
                        grade_list2.append(3)
                    elif grade_list[b] == "D":
                        grade_list2.append(2) 
                    elif grade_list[b] == "E":
                        grade_list2.append(1)
                    elif grade_list[b] == "F":
                        grade_list2.append(0)                                      
                    else:
                        tkinter.messagebox.showerror("Entry error","Missing your grades\nPlease confirm")
                #--------------------------------------5.0 GPA calculation----------------------------------
                quality_point = [] 
                if len(grade_list2) == len(credit_list):
                    for c in range(0,len(grade_list2)):
                        quality_point.append(grade_list2[c] * credit_list[c])
                else:
                    tkinter.messagebox.showerror("Entry error","Confirm credit unit and\ngrade entries are entered correctly")
                
                sum1 = sum(credit_list)
                sum2 = sum(quality_point)
                
                all_credits.append(sum1) # to be used to calculate cgpa
                all_quality_points.append(sum2) # to be used to calculate cgpa
                
                my_gpa = sum2/sum1
                
                if float(my_gpa) > 2.50:
                    color = 'green' 
                elif float(my_gpa) < 2.50:
                    color = 'red'
                
                self.result["gpa"+str(a)] = Label(self.result_frames["result_frame"+str(a)],text=str(round(my_gpa,2)),font=('arial',17,'bold'),justify='left',fg=color,bg=background,relief='groove',bd=2)
                self.result["gpa"+str(a)].place(x=280,y=0)                
            
           
            #=================================
            current_cgpa = entry_list[0].get()
            current_credit = entry_list[1].get()
            
            try:
                current_qp = float(current_credit) * float(current_cgpa) # Multiply the current credit units by the current cgpa
            except (ValueError, TypeError):
                tkinter.messagebox.showerror("Entry error","Please check current CGPA entries")
            
            all_credits.append(float(current_credit))
            all_quality_points.append(current_qp)
            #=================================
 
            c_sum = sum(all_credits) # Sum up all the credit units 
            qp_sum = sum(all_quality_points) # Sum up all the quality points            
            
            my_cgpa = qp_sum/c_sum
            if float(my_cgpa) > 2.50:
                color2 = 'green' 
            elif float(my_cgpa) < 2.50:
                color2 = 'red'            
            
            self.cgpa_lbl.configure(text=str(round(my_cgpa,2)),fg=color2,bd=2)
            cgpa_btn.place_configure(x=135,y=518)
        
        self.cgpa_lbl = Label(self.master,text="",font=('arial',18,'bold'),justify='left',fg='#ffffff',bg=background,relief='groove',bd=0)
        self.cgpa_lbl.place(x=630,y=518) 
            
        cgpa_btn.configure(state=NORMAL,command=cgpa)        
        
       
        """try:
            value = int(entry)
            if value > 12:
                tkinter.messagebox.showerror("Count error","Value should be less than 12\nTry again")
                function()
        except ValueError:
            tkinter.messagebox.showerror("Entry error","You entered a wrong value")
            function()
            
        for c in range(0,value):
            self.container["container"+str(c)] = Frame(self.innerFrame,width=400,height=150,bg=background,relief='flat',bd=0)
            self.container["container"+str(c)].grid(row=0+c, column=0, padx=200, pady=10) 
            
            semester_name = Label(self.container["container"+str(c)],text='Semester '+str(c+1),font=('arial',10,'bold'),fg=foreground,bg=background,relief='raised',bd=2)
            semester_name.place(x=7,y=0)            
            
            self.frame["frame"+str(c)] = Frame(self.container["container"+str(c)],width=380,height=95,bg=background2,relief='raised',bd=2)
            self.frame["frame"+str(c)].place(x=7,y=22)
            
            TCU_lbl = Label(self.frame["frame"+str(c)],text='Total credit units for this semsester ',font=('arial',10),fg=foreground,bg=background2)
            TCU_lbl.place(x=5,y=0)  
            if c == 0:
                TCU_lbl_info = Label(self.frame["frame"+str(c)],text='what is this',font=('normal',8,'underline'),fg='#6673f5',bg=background2)
                TCU_lbl_info.place(x=311,y=2)  
                TQP_lbl_info = Label(self.frame["frame"+str(c)],text='what is this',font=('normal',8,'underline'),fg='#6673f5',bg=background2)
                TQP_lbl_info.place(x=311,y=43)    
            else:
                pass
            
            self.TCU["TCU_ent"+str(c)] = Entry(self.frame["frame"+str(c)],font=('normal',11),width=7,bd=2,justify='right')
            self.TCU["TCU_ent"+str(c)].place(x=240,y=5)
            
            TQP_lbl = Label(self.frame["frame"+str(c)],text='Total quality points for this semsester ',font=('arial',10),fg=foreground,bg=background2)
            TQP_lbl.place(x=5,y=40)                   
            
            self.TQP["TQP_ent"+str(c)] = Entry(self.frame["frame"+str(c)],font=('normal',11),width=7,bd=2,justify='right')
            self.TQP["TQP_ent"+str(c)].place(x=240,y=45)     
            
            def cgpa():
                TCU = list(self.TCU.values())
                TQP = list(self.TQP.values())
                list1 = []
                list2 = []
                if len(TCU) == len(TQP):
                    for i in range(0, len(TQP)):
                        list1.append(int(TCU[i].get()))
                        list2.append(int(TQP[i].get()))
                        
                    var1 = sum(list1)
                    var2 = sum(list2)
                    result = var2/var1
                    print(result)
                    if c == value-1:
                        result_lbl = Label(self.container["container"+str(c)],text=str(round(result,2)),font=('arial',12,'bold'),fg='green',bg=background2)
                        result_lbl.place(x=450,y=116)                    
                    
                else:
                    tkinter.messagebox.showerror("Entry error","Please to make sure all entries are filled correctly")
                    
            if c == value-1:
                self.cgpa_btn = Button(self.container["container"+str(c)],text='Calculate CGPA',font=('arial',10,'bold'),fg=background,bg=foreground,activebackground=foreground,activeforeground=background,relief='ridge',bd=2,command=cgpa)
                self.cgpa_btn.place(x=150,y=116)
            else:
            pass"""
        
if __name__=='__main__':
    root = Tk()
    main_app = Gp_calculator(root)
    root.mainloop()