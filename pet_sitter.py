# Selenium Project
# automating pet_planet website - tells you the closest pet_sitter according to the
# user's location, options, dates. 


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys # keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

user_address = input("주소를 입력하세요: ")
user_startdate = input("체크인 날짜를 입력하세요 (year/month/day): ")
user_enddate = input("체크아웃 날짜를 입력하세요: (year/month/day): ")
user_options = input('''선택하실 옵션의 번호를 입력하세요: (2개 이상 선택 가능. 선택하실 옵션이 없는 경우 '없음' 이라고 입력해주세요): 

1) 반려동물 없음 
2) 픽업 가능 
3) 대형견 가능 
4) 마당 있음 
5) 노견 케어 
''')
user_options.split(' ')


# Launch Browser 
driver_path = "/Applications/chromedriver"
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://petplanet.co/")
driver.implicitly_wait(10)
driver.maximize_window()

# Click Start button 
start_button = driver.find_element(By.LINK_TEXT, "내 주변 펫시터 찾기")
start_button.click()

# Enter the input address

# Enter the date 
driver.implicitly_wait(10)
startDate = driver.find_element(By.CSS_SELECTOR, '#service-container > div.desktop.hidden-s > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div > div > div > button')
startDate.click()
driver.find_element(By.ID, "startDate").send_keys(user_startdate)
driver.implicitly_wait(10)
driver.find_element(By.ID, 'endDate').send_keys(user_enddate)

# Give some delay 
time.sleep(1)
driver.implicitly_wait(10)

# Enter the address
search_address = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "addressInput"))
    )
search_address.send_keys(user_address)
address_choice = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#service-container > div.desktop.hidden-s > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(2) > div > p'))
    )
address_choice.click()

# Give some delay 
time.sleep(1)

# Select options
for option in user_options:
    if option == '1':
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]/p').click()
        time.sleep(1)
    elif option == '2':
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/p').click()
        time.sleep(1)
    elif option == '3':
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[3]/p').click()
        time.sleep(1)
    elif option == '4':
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[4]/p').click()
        time.sleep(1)
    elif option == '5':
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[5]/p').click()
        time.sleep(1)
    else:
        break 

# Select the closest pet sitting house
time.sleep(2)
house = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div[2]/div/a/img')
house.click()

time.sleep(1)

# Switch tab
#get current window handle
current_window = driver.current_window_handle

#get first child window
child_window = driver.window_handles

for w in child_window:
#switch focus to child window
    if(w != current_window):
        driver.switch_to.window(w)

time.sleep(1)

# Print out necessary info
description = driver.find_element(By.XPATH, '//*[@id="detail-page-container"]/div[1]/div[1]/div/div/div[4]/div[1]/div[1]/div[2]/p')
location = driver.find_element(By.TAG_NAME, 'h1')
reviews = driver.find_elements(By.TAG_NAME, 'h2')
print('\n')
print(description.text)
print("주소: ", location.text)
print(reviews[3].text)


# Close the browser
time.sleep(5)
driver.quit()



