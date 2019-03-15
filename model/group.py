from sys import maxsize

class Group:
    def __init__(self, name=None, header=None, footer=None, id = None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other): # переопределяем сравнение, для сравнения групп
        # 2 группы равны, когда у них совпадают имена и совпадают идентификаторы даже если идентификатор не определен(None)
        return (self.id is None or other.id is None or self.id == other.id)and self.name == other.name



    def id_or_max(self): #вспомогательная функция для сортировки элементов в списке
        if self.id:
            return int(self.id)
        else:
            return  maxsize