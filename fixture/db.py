import mysql.connector
import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True #сбрасываем кэш бд после выполнения запроса(чтобы работали тесты сравнения после изменений объектов бд)

    def get_group_list(self):   #загружаем список групп из базы данных
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list") #выполнение запроса в базу
            for row in cursor:
                (id, name, header, footer) = row    #разбиваем полученный кортеж на переменные
                list.append(Group(id=str(id), name=name, header=header, footer=footer)) #передаем параметры объекту
        finally:
            cursor.close()
        return list

    def get_contact_list(self):   #загружаем список групп из базы данных
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'") #выполнение запроса в базу с фильтром на актуальные данные
            for row in cursor:
                (id, firstname, lastname) = row    #разбиваем полученный кортеж на переменные
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname)) #передаем параметры объекту
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()



