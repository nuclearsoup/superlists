from selenium import webdriver

#Kevin has a need of a web based todo system
browser = webdriver.Firefox()
#He has found one here
browser.get('http://localhost:8000')
#As has the word to-do in the title
assert 'to-do' in browser.title
#He is invited to enter a todo item, straight away

#When he has entered the item the list is updated

#And there is a text box for another item.

#He goes away

#Worries that the item is gone, comes back

#Satisfied that it is there he goes back away

browser.quit()
