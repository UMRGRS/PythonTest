#Mediante este código puedo obtener la información sobre mis asistencias en la plataforma de mi universidad
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://proyecta.utch.edu.mx/")
assert "Proyecta UTCH" in driver.title
login_button = driver.find_element(By.LINK_TEXT, "Iniciar Sesión")
login_button.click()

driver.implicitly_wait(5)

username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')
send_creds = driver.find_element(By.ID, 'login')

username.send_keys('1121150034')
password.send_keys('qxrvynilp')
driver.implicitly_wait(5)

send_creds.click()
driver.implicitly_wait(5)

driver.get('https://proyecta.utch.edu.mx/salumno/informacion')

attendance_button = driver.find_element(By.LINK_TEXT, "Asistencias")

attendance_button.click()

driver.implicitly_wait(5)

table = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/table[2]')

head = table.find_element(By.TAG_NAME, 'thead')

for row in head.find_elements(By.TAG_NAME, 'tr'):
    for tr in row.find_elements(By.TAG_NAME, 'th'):
        print('|{}|'.format(tr.text), end='')
    print('')

body = table.find_element(By.TAG_NAME, 'tbody')

for row in body.find_elements(By.TAG_NAME, 'tr'):
    for td in row.find_elements(By.TAG_NAME, 'td'):
        print('|{}|'.format(td.text), end='')
    print('')

driver.close()