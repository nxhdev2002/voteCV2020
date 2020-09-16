import requests, time
from selenium import webdriver

while True:
    hide = input("Ẩn Chrome? (1==ẩn or 0==không)")
    if (hide == '1' or hide == '0'):
        break
hide = int(hide)
proxy = input("My proxy? (ĐỂ trống nếu k có)")
solanvote = input("Số lần vote ? (Mặc định 10)")
if (len(str(solanvote)) == 0):
    solanvote = 10
else:
    solanvote = int(solanvote)
print(solanvote)
while True:
    if (solanvote == 0):
        break
    try:
        print("LEFT: " +str(solanvote))
        opts=  webdriver.ChromeOptions()
        if (len(proxy) != 0):
            opts.add_argument("--proxy-server=" + proxy)
        if (hide):
            opts.add_argument("--headless")
        driver = webdriver.Chrome('chromedriver.exe', chrome_options=opts)

        driver.get("https://www.riddle.com/showcase/268048/opinion-poll")
        time.sleep(3)
        iframe = driver.find_element_by_xpath('//*[@id="content"]/div/div/section/div/iframe')
        driver.switch_to.frame(iframe)
        driver.find_element_by_xpath("/html/body/rid-riddle/div[2]/rid-riddle-type/rid-poll/div[2]/div/div[3]/div[2]/div[2]/div[2]/div").click()
        time.sleep(3)
        solanvote -= 1
        driver.close()
    except Exception as e:
        print(str(e))

print("Done")