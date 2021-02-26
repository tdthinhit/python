from tkinter import *
import tkinter.ttk as exTk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def openchr():
    user= cmb1.get()
    driver=webdriver.Chrome()
    driver.get('https://www.youtube.com/')
    el=driver.find_element_by_xpath('//*[@id="search"]')
    el.send_keys(user)    
    

win =Tk()
cmb1 = exTk.Combobox(win, width=30, font ='Times 30')
cmb1['values'] = ('1', '2', '3')
btstart = Button(win, text='start', font='Time 30',command=openchr)
cmb1.grid(row = 0, column = 0)
btstart.grid(row=0, column=1, padx=20)
win.mainloop ()