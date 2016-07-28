import sys,csv,sqlite3,os,scipy
scriptpath = os.path.dirname(sys.argv[0])
db =  scriptpath + '/Data/data'
conn =sqlite3.connect(db)
print(scriptpath)
