from flask import Flask,render_template,request
import sqlite3 as sqlite

app= Flask(__name__)
 
@app.route('/')
def home():
    return render_template('home.html')
 
@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrecord',methods=['POST','GET'])
def addrecord():
    if request.method == "POST":
        
        try: 
            nm= request.form['nm']
            addr=request.form['add']
            city= request.form['city']
            pin=request.form['pin']
            
            with sqlite.connect('database1.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin))
                
                msg = "Record succesfully added"
        except:
            con.rollback()
            msg="error in insert operation"   
        
        finally:
            return render_template("result.html",msg=msg)     
            con.close()    
@app.route('/list')
def list():
    con =sqlite.connect("database1.db")
    con.row_factory= sqlite.Row
    
    cur=con.cursor()
    
    cur.execute("select * from students")
    rows=cur.fetchall()
    return render_template('list.html',rows=rows)
               
        
    

if __name__== "__main__":
    
      app.run(debug=True)