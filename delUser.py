import mysql.connector
import aux_func as f
import datetime as dt
import sys

def RUN(args):
	try:
		_id_=args
		__db__='testdb1'
		pwd="pwd"
		db = mysql.connector.connect(
		  host="localhost",
		  password=f.decode(f.env('DB-PWD')),
		  user="root",
		  database=__db__,
		)
		c  = db.cursor()    
		def vid(uname):
		
			c.execute(f'SELECT * FROM creds WHERE  emailid="{uname}";')
			x=c.fetchall()
			if(x==[]):
				return(0)
			else:
				return(1)

		def calCoins(uname):
			if(vid(uname)):
					
				c.execute(f"Select * FROM transactions WHERE from_email='{uname}' OR to_email='{uname}';")
				
				x=c.fetchall()
				
				myCoins=[]
				
				for _ in x:
					if(_[2]==uname and _[3]==uname):
						myCoins.append(0)
					elif(_[2]==uname):
						myCoins.append(-1*_[4])
					elif(_[3]==uname):
						myCoins.append(_[4])
				
				return(sum(myCoins))
			else:
				return(0)		
		
		fr=_id_
		to="recoin.man@gmail.com"
		amt=calCoins(fr)
		c.execute(f'INSERT INTO transactions (from_email,to_email,amt,time,status) values("{fr}","{to}",{amt},"{dt.datetime.now().strftime("%H:%M:%S of %d-%m-%Y")}","success")')
		c.execute(f'DELETE FROM creds WHERE emailid LIKE "{_id_}";')
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
		c.execute(f'INSERT INTO transactions (from_email,to_email,amt,time,status) values("{fr}","{to}",{amt},"{dt.datetime.now().strftime("%H:%M:%S of %d-%m-%Y")}","success")')
		c.execute(f'DELETE FROM creds WHERE emailid LIKE "{_id_}";')
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
		c.execute(f'INSERT INTO transactions (from_email,to_email,amt,time,status) values("{fr}","{to}",{amt},"{dt.datetime.now().strftime("%H:%M:%S of %d-%m-%Y")}","success")')   
		c.execute(f'DELETE FROM creds WHERE emailid LIKE "{_id_}";')
		db.commit()
		print("success")
	except Exception as e:
		print("failure")
	
if len(sys.argv)>1:
    RUN(sys.argv[1])
