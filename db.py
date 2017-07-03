import sqlite3
import uuid
import time
import sys,os

class dbsqlite(object):
    def __init__(self):
        self.cx = sqlite3.connect( sys.path[0] +"/test.db")
        self.cu = self.cx.cursor()
        self.create()

    def create(self):
        self.cu.execute(
            "create table   if not exists show (id integer primary key,  city varchar(100), venue varchar(100), time integer,state integer,title varchar(100) )")

    def no_select_action(self, actionStr):
        try:
            self.cu.execute(actionStr)
            self.cx.commit()
        except:
            return

    def _select(self, selectStr):
        self.cu.execute(selectStr)
        return self.cu.fetchall()

    def update(self,str ):
        self.cu.execute(str)
        self.cx.commit()

class db(dbsqlite):
    def __init__(self):
        dbsqlite.__init__(self)

    def insert(self, data):
        insert_str = 'insert into show values(' + str(int(time.time())) \
                     + ',' + '"' + data['city'] + '"' \
                     + ',' + '"' + data['venue'] + '"' \
                     + ',' + '"' + str(data['time']) + '"' \
                     + ',' + '"' + str(data['state']) + '"' \
                     + ',' + '"' + data['title'] + '"' \
                     + ')'
        self.no_select_action(insert_str)

    def select_by_title(self,title):
        str = 'SELECT * FROM show where  title=' +  '"''"'+    title +  '"'
        return  self._select(str)

    def selectAll(self):
        str = 'SELECT * FROM show ;'
        return self._select(str)

    def select_by_state(self, state):
        str = 'SELECT * FROM show where  state=' +  '"''"'+    str(state) +  '"'
        return  self._select(str)
    def update_itemstate_by_id(self, id , state):
        strxx = 'update show set state=' + '"''"'+ str(state)  + '"'  +  ' where id = ' + str(id)
        self.update(strxx)

if __name__ == "__main__":
    path = sys.path[0]

    xx = db()
    xx.insert({'city': '南京', 'venue': 'venue', 'time': 2233, 'state': 1,
               'title': 'xx' + str(int(time.time()))})

    # item = xx.select_by_title('xx1498529836')
    # if len(item):
    #     print ("select succ")
    # else :
    #     print ('select fail ')

    # xx.update_itemstate_by_id(1498529836, 6)