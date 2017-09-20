import time
from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
pref = {"download.default_directory": "C:\\Users\\Surya\\Desktop\\Scilab"}
chromeOptions.add_experimental_option("prefs", pref)
browser = webdriver.Chrome(executable_path="C:\\Python34\\chromedriver.exe",
                           chrome_options=chromeOptions)
browser.get("http://ulc.srmuniv.ac.in/elabvdp/")
print("Complete Login")
browser.find_element_by_id("username").send_keys("RA1711003040014")
browser.find_element_by_id("password").send_keys("skiran1998")
browser.find_element_by_id("button").click()
time.sleep(1)
browser.find_element_by_css_selector("div.card-content.white-text").click()
time.sleep(1)

f = open("questions.txt", "r")
a = []
b = []
d = []
for line in f:
    a.append(line)

for i in range(len(a)):
    b.append(a[i].strip())

d = []
browser.get("http://ulc.srmuniv.ac.in/elabvdp/login/student/code/mathslab/mathslab.code.php?id=1&value=0")
c = browser.find_elements_by_class_name("collection-item")[1].text.lstrip()[11:]

if c in b:
    print("Question Found")
    index1 = b.index(c)

    answers = open("answers.txt", "r")
    for line1 in answers:
        d.append(line1)
    time.sleep(2)

time.sleep(2)

x = "Hello"
#browser.execute_script("var editor = CodeMirror(document.getElementById(' CodeMirror-line '));editor.setValue('" + x + "');")
browser.execute_script("var g = document.getElementsByClassName('cm-variable');g.setValue('" + x + "')");
#editor = browser.find_element_by_class_name('cm-variable')
#editor.send_keys(x)
browser.find_element_by_id("evaluateButton").click()
