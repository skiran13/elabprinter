import tkinter as tk
import time
import os
from img2pdf import convert
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

def entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
            entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry

def pdfconv():
    with open("Matlab Programs.pdf", "wb") as f:
        f.write(convert([i for i in os.listdir(os.path.join(os.environ['USERPROFILE'], "Desktop\\Matlab Printer")) if i.endswith(".png")]))
    for file in os.listdir(os.path.join(os.environ['USERPROFILE'], "Desktop\\Matlab Printer")):
        if file.endswith(".png"):
            os.remove(file)
    return

def store_login():
    u = user.get()
    p = password.get()
    progs = programs.get()
    progs = int(progs)
    root.destroy()
    chromeOptions = webdriver.ChromeOptions()
    pref = {"download.default_directory" : os.path.join(os.environ['USERPROFILE'], "Desktop\\Matlab Printer")}
    chromeOptions.add_experimental_option("prefs",pref)
    browser = webdriver.Chrome(executable_path=os.path.join(os.environ['USERPROFILE'], "Desktop\\Matlab Printer\\chromedriver.exe"), chrome_options=chromeOptions)
    browser.get("http://ulc.srmuniv.ac.in/elabvdp/")
    browser.find_element_by_id("username").send_keys(u)
    browser.find_element_by_id("password").send_keys(p)
    browser.find_element_by_id("button").click()
    time.sleep(1)
    browser.find_element_by_css_selector("div.card-content.white-text").click()
    delay = 1
    for o in range(progs):
        o = str(o)
        browser.get("http://ulc.srmuniv.ac.in/elabvdp/login/student/code/mathslab/mathslab.code.php?id=1&value="+o)
        try:
            WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'evaluateButton')))
            browser.get("http://ulc.srmuniv.ac.in/elabvdp/login/student/code/getReport.php")

        except TimeoutException:
            print("Loading took too much time!")
    print("All Reports Printed")
    time.sleep(2)
    return


root = tk.Tk()
root.geometry('300x270')
root.title('Matlab Printer')
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
user = entry(parent, "User Name : ", 16)
password = entry(parent, "Password :", 16, show="*")
programs = entry(parent, "No. of Programs : ", 3)
w = tk.Label(parent, text="\nMade by:\nS Surya Kiran\nRA1711003040014(CSE-B)\nskiran13@gmail.com")
w.pack(side=tk.BOTTOM)
b = tk.Button(parent, borderwidth=4, text="Login", width=10, pady=5, command=store_login)
b.pack(side=tk.BOTTOM)
parent.mainloop()
pdfconv()
