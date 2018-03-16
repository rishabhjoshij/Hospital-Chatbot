import sqlite3

conn = sqlite3.connect('hospital.db')

conn.execute('''CREATE TABLE PATIENT
	(PID INTEGER PRIMARY KEY,
	PNAME TEXT NOT NULL,
	PAGE INTEGER NOT NULL,
	PSEX TEXT NOT NULL
	);''')

conn.execute('''CREATE TABLE APPOINTMENT
	(AID INTEGER PRIMARY KEY,
	PID INTEGER NOT NULL,
	DID INTEGER NOT NULL,
	HID INTEGER NOT NULL,
	PURPOSE TEXT NOT NULL,
	ADATETIME TEXT NOT NULL,
	AFEE REAL NOT NULL
	);''')

conn.execute('''CREATE TABLE DOCTOR
	(DID INTEGER PRIMARY KEY,
	HID INTEGER NOT NULL,
	DNAME TEXT NOT NULL,
	DSPECIAL TEXT NOT NULL,
	DFEE REAL NOT NULL
	);''')

conn.execute('''CREATE TABLE AVAILABLE
	(DID INTEGER NOT NULL,
	TIME TEXT NOT NULL,
	WEEKDAY TEXT NOT NULL
	);''')
	
conn.execute('''CREATE TABLE MEDICINE
	(MID INTEGER PRIMARY KEY,
	MNAME TEXT NOT NULL,
	MDOSAGE TEXT NOT NULL,
	MPRICE REAL NOT NULL
	);''')

conn.execute('''CREATE TABLE SYMPTOMS
	(SID INTEGER PRIMARY KEY,
	SNAME TEXT NOT NULL,
	SMED INTEGER NOT NULL
	);''')

conn.execute('''CREATE TABLE HOSPITAL
	(HID INTEGER PRIMARY KEY,
	HNAME TEXT NOT NULL,
	HLOCATION TEXT NOT NULL,
	HPHONE INTEGER NOT NULL
	);''')

# To check if all went well
cursor = conn.execute("select name from sqlite_master where type = 'table';")
print cursor.fetchall()

conn.close()