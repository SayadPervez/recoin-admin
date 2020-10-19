import mysql.connector
import aux_func as f
import datetime as dt
import sys

def RUN(args):
	try:
		_id_,_type_=args.split(',')
		__db__='testdb1'
		pwd="pwd"
		db = mysql.connector.connect(
		  host="localhost",
		  password=f.decode(f.env('DB-PWD')),
		  user="root",
		  database=__db__,
		)
		c  = db.cursor()    
		c.execute(f'INSERT INTO creds (emailid,pwd) values("{_id_}","{pwd}");')
		db.commit()
		__db__='testdb2'
		pwd="pwd"
		db = mysql.connector.connect(
		  host="localhost",
		  password=f.decode(f.env('DB-PWD')),
		  user="root",
		  database=__db__,
		)
		c  = db.cursor()    
		c.execute(f'INSERT INTO creds (emailid,pwd) values("{_id_}","{pwd}");')
		db.commit()
		__db__='testdb3'
		pwd="pwd"
		db = mysql.connector.connect(
		  host="localhost",
		  password=f.decode(f.env('DB-PWD')),
		  user="root",
		  database=__db__,
		)
		c  = db.cursor()    
		c.execute(f'INSERT INTO creds (emailid,pwd) values("{_id_}","{pwd}");')
		db.commit()
		print("success")
	except Exception as e:
		print("failure")
	
if len(sys.argv)>1:
    RUN(sys.argv[1])
