'''
Download chrome webdriver to same location as .py file - https://chromedriver.storage.googleapis.com/index.html?path=2.37/
'''
'''
TODO
-Check time ability to sync with website
-error handling/testing with prior checkin
'''

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import datetime, time, selenium


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

while True:
    print(datetime.datetime.now().strftime("%H:%M:%S.%f"))
    driver.get("https://www.southwest.com/air/check-in/index.html")
    #Get Form Fields
    try:
        confNumber = driver.find_element_by_id("confirmationNumber")
        firstName = driver.find_element_by_id("passengerFirstName")
        lastName = driver.find_element_by_id("passengerLastName")
    except Exception as e:
        print('[-] Cannot find checkin form. Reason:{}'.format(e))
        continue

    #Fill out form fields
    confNumber.send_keys("UDEE7J")
    firstName.send_keys("Ryan")
    lastName.send_keys("Haley")

    #Submit form fields
    try:
        button = driver.find_element_by_css_selector('#form-mixin--submit-button')
        button.click()
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="swa-content"]/div/div[2]/div/section/div/div/div[3]/button').click()
            print('[+] Successfully checked in!')
            print(driver.find_element_by_xpath('//*[@id="swa-content"]/div/div[2]/div/section/div/div/div/table/tbody/tr/td[1]/div/ul/li/div/div[2]/div/span[2]').text)
        except Exception as e:
            try:
                print(driver.find_element_by_xpath('//*[@id="swa-content"]/div/div[2]/div/section/div/div/div/table/tbody/tr/td[1]/div/ul/li/div/div[2]/div/span[2]').text)
                print('[-] Already checked in!')
            except:
                try:
                    print(driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/h2').text)
                    print('[-] Bad reservation information. Please check name and reservation number entered.')
                except:
                    print('[-] Error Checking in. Reason:{}'.format(e))
    except Exception as e:
        print('[-] Error submitting checkin information. Reason:{}'.format(e))

    print('Done')
    print(datetime.datetime.now().strftime("%H:%M:%S.%f"))
    driver.delete_all_cookies()
    driver.refresh()
    time.sleep(5)

