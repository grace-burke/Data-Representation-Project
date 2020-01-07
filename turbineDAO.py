import mysql.connector

class TurbineDAO:
    db=""

    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        port="3308",
        user="root",
        password="",
        database="DataRep"
        )
    
            
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into windturbine (Model,Manufacturer,Rating) values (%s,%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid


    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from windturbine"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        return returnArray


    def findByID(self, ID):
        cursor = self.db.cursor()
        sql="select * from windturbine where ID = %s"
        values = (ID,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)


    def update(self, values):
        cursor = self.db.cursor()
        sql="update windturbine set Model=%s, Manufacturer=%s, Rating=%s  where ID = %s"
        cursor.execute(sql, values)
        self.db.commit()


    def delete(self, ID):
        cursor = self.db.cursor()
        sql="delete from windturbine where ID = %s"
        values = (ID,)
        cursor.execute(sql, values)
        self.db.commit()
        print("Delete Done")


    def convertToDictionary(self, result):
        colnames=['ID','Model','Manufacturer', "Rating"]
        item = {}    
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value        
        return item


turbineDAO = TurbineDAO()