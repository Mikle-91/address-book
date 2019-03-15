from sys import maxsize

class Contact:
    #def __init__(self, firstname=None, lastname=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None):
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, nickname=None, photo=None, title=None,
                 company=None, address=None, homephone=None, mobilephone=None, workphone=None, fax=None, email=None,
                 email2=None,
                 email3=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, new_group=None,
                 address2=None, secondaryphone=None, notes=None, all_phones_from_home_page = None ):

        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.new_group = new_group
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return"%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):  # переопределяем сравнение, для сравнения групп
        return (self.id is None or other.id is None or self.id == other.id)\
                and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return  maxsize