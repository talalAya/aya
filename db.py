import sqlite3


class Database:
  def __init__(self,db):

      self.con =sqlite3.connect(db)
      self.cur =self.con.cursor()

        
      sql ="""
      CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY autoincrement,
            name text NOT NULL,
            age INTEGER,
            job text,
            email text,
            gender text,
            mobile text,
            address text)"""
      self.cur.execute(sql)
      self.con.commit()
  
  def insert(self,name,age,job,email,gender,mobile,address):
      self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                        (name,age,job,email,gender,mobile,address))
      self.con.commit()               
  
  def fetch(self): 
      self.cur.execute("SELECT * FROM employees")
      rows = self.cur.fetchall()
      return rows
      
  def remove(self,id):

      self.cur.execute("delete from employees where id=?",(id,))  
      self.con.commit()   

  def update(self,id,name,age,job,email,gender,mobile,address):

      self.cur.execute("UPDATE employees SET name=?,age=?,job=?,email=?,gender=?,mobile=?,address=? where id=?",
                       (name,age,job,email,gender,mobile,address,id))
      self.con.commit()                
  
  
  
  
   
