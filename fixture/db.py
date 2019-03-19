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
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, company, address, home, mobile, work, fax, email, email2, email3, bday, bmonth, byear, aday, amonth, ayear, address2, phone2, notes  from addressbook where deprecated='0000-00-00 00:00:00'") #выполнение запроса в базу с фильтром на актуальные данные
            for row in cursor:
                (id,  firstname, middlename, lastname, nickname, company, title, company, address, home, mobile, work, fax, email, email2, email3, bday, bmonth, byear, aday, amonth, ayear, address2, phone2, notes) = row    #разбиваем полученный кортеж на переменные
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title, company=company, address=address, homephone=home, workphone=work, fax=fax, email=email, email2=email2, email3=email3, bday=bday, bmonth=bmonth, byear=byear, aday=aday, amonth=amonth,ayear=ayear,address2=address2, secondaryphone=phone2, notes=notes )) #передаем параметры объекту
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()



