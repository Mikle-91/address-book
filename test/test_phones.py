import re
from model.contact import Contact

def test_phones_on_home_page(app):
    app.contact.modify_first_contact(Contact(firstname="Axel")) #рабочий тест из другого файла

    contact_from_home_page = app.contact.get_contact_list()[0]  # новая проверка учитывающая незапаолненные номера
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "",s)  # (что заменяем, на что, где) удаляем лишние символы из номеров телефонов
def merge_phones_like_on_home_page(contact): # склеили список телефонов  (обратная проверка)
    return "\n".join(filter(lambda x: x != "",  #если остались пустые строки, то их тоже убираем
                             (map(lambda x: clear(x),   #убираем лишние символы
                                  filter(lambda x: x is not None,   #  убираем из него с значением None
                                         [contact.homephone, contact.workphone, contact.mobilephone, contact.secondaryphone]))))) #исходный список










#
# def test_phones_on_contact_view_page(app):    # старая проверка телефонов если все заполнены
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone #на странице view лишние символы не отчищаются в отличае от home, claer убираем
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone