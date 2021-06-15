from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

who = input("kime yazmak istiyorsun [rehberinde kayıtlı ismi]: ")
message = input("MESAJINIZ.: ")
kac_message = int(input("KAÇ ADET MESAJ YAZMAK İSTİYORSUNUZ: "))

print("LÜTFEN WHATSAPP QR KOD OKUYUCUYU HAZIRLAYINIZ...")

time.sleep(6)

driver = webdriver.Chrome()
wp = "https://web.whatsapp.com/"

driver.get(wp)
time.sleep(8)

search_bar = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]").send_keys(who)
time.sleep(3)
xox = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]").send_keys(Keys.ENTER)
for i in range(kac_message):
	text_bar = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(message)
	text_baro =driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(Keys.ENTER)
