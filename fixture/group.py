from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app


    def create(self, Group):    #создание группы
        driver = self.app.driver
        self.open_groups_page()
        # init groupe creation
        driver.find_element_by_name("new").click()
        #fill form
        self.fill_group_form(Group)
        # submit group
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None # объявляем кэш невалидным

    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)



    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def open_groups_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/group.php") and len(driver.find_elements_by_name("new")) >0):
            driver.find_element_by_link_text("groups").click()


    def select_group_by_index(self, index): #выделение группы из списка кликом по чекбоксу
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        driver = self.app.driver
        driver.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        driver.find_element_by_name("delete").click()     #delete group
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_id(id)
        driver.find_element_by_name("delete").click()     #delete group
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self): #выделение первой группы из списка
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def modify_first_group(self): # редактирование первой в списке группы
        self.modify_group_by_index(0)


    def modify_group_by_index(self, index, group):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        #open modification form
        driver.find_element_by_name("edit").click()
        #fill group form
        self.fill_group_form(group)
        # submit modification
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def count(self): # счетчик количества групп(чекбоксов) на странице
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self): #получение списка групп на странице
        if self.group_cache is None:
            driver = self.app.driver
            self.open_groups_page()
            self.group_cache =[]
            for element in driver.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id ))
        return list(self.group_cache)   #возвращяем копию кэша










