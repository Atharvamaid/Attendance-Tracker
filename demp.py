from flask import Flask,request,render_template,redirect
from selenium import webdriver

app = Flask('app')

@app.route('/')
@app.route('/home')
def home():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    user1 = request.form["username"]
    pas1 = request.form["pass"]
    op = webdriver.FirefoxOptions()
    op.add_argument('--headless')
    dr = webdriver.Firefox(executable_path='C:/geckodriver.exe', options=op)
    g = dr.get('http://www.pccoerp.com/pccoe/')
    user = dr.find_element_by_name('userid')
    pas = dr.find_element_by_name('pass_word')
    user.send_keys(user1)
    pas.send_keys(pas1)
    log = dr.find_element_by_id('loginbutton').click()
    dr.switch_to.frame("main")
    dr.find_element_by_link_text("Attendance").click()
    dr.find_element_by_link_text("Course Wise Attendance").click()
    data = dr.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/table[4]")
    return render_template('login.html',user1=user1, pas1=pas1,data=data)