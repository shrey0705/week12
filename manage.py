from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap

import mysql.connector as sql

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_employee():
   return render_template('employee.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         EmpId = request.form['EmpID']
         EmpName = request.form['EmpName']
         EmpGender = request.form['EmpGender']
         EmpPhone = request.form['EmpPhone']
         EmpBdate = request.form['EmpBdate']
         
         with sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO employee (EmpID,EmpName,EmpGender,EmpPhone, EmpBdate) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(EmpId,EmpName,EmpGender,EmpPhone,Emp)
            cur.execute(cmd)
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
         
      finally:
         return render_template("output.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   with sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db") as conn:  
      cur = conn.cursor()
      cur.execute("select * from employee")
      rows = cur.fetchall()

   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
