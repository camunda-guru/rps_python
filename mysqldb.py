import pymysql

db= pymysql.connect(host="localhost", user="root", 
                    passwd="vignesh",
db="nessu")

cursor = db.cursor()
stmt = "SELECT * from employee"
cursor.execute(stmt)
rows = cursor.fetchall ()

for row in rows:
    print ("Row: ")
    for col in row :
        print ("Column: %s" % (col))
    #print ("End of Row")
#print ("Number of rows returned: %d" % cursor.rowcount)

cursor.close()

db.close()

