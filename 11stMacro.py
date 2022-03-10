
import asyncio
from asyncio.windows_events import NULL
from operator import truediv
from pickle import FALSE
from secrets import choice
import unittest

import time

import base64

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.alert import Alert


from PIL import ImageGrab
from PIL import Image
from pytesseract import *

# 로그인url
url1 = "https://login.11st.co.kr/auth/login.tmall?returnURL=http%253A%252F%252Fm.11st.co.kr%252FMW%252FMyPage%252FmypageHome.tmall"
# 상품url
#url2 = 'http://m.11st.co.kr/products/m/2884903780?prdNo=2884903780&trTypeCd=MAS84&trCtgrNo=950076'
#orderURL=('https://buy.m.11st.co.kr/MW/Order/orderBasicFirstStep.tmall?prdDlvCstStlTyp=01&method=&isPopup=&prdNo=2884903780&mstrPrdNo=0&selMthdCd=01&dispCtgrNo=1162941&ldispCtgrNo=1162906&optCnt=1&selOptCnt=1&insOptCnt=0&isFast=&prePointDisCard=&iscpn=N&selStatCd=103&optString=0%A2%D31%21%3D%212_+%40%3D%40%3A%3D%3A&optQtyString=1%3A%3D%3A&optPrcString=1000%3A%3D%3A&optStckNoString=12647228579%3A%3D%3A&selPrc=7900&incommingCode=01&prdAppmtDbDlvCd=01&xzone=&xfrom=&brd_cd=&brd_no=&trTypeCd=MAS84&trCtgrNo=950076&mobileYn=N&bcktExYn=N&addAllSelPrc=8900&done=Y&isSelMinLimit=false&selMinLimitQty=-1&prdTypCd=01&minusOptYn=&cuponPrc=0&optDscPrc=0&catalogNo=&lowest_yn=&catalog_no=&limitTypCd=&ordObjLimit=N&sendGiftYn=N&freePackageType=01&isMart=N&martNo=999999999&strNo=&mailNo=&strDlvClfCd=&mailNoSeq=&martPrmtNm=&martPrmtSeq=&martPrmtCd=&syrupPayYn=N&soDscAmt=0&moDscAmt=0&selMnbdNo=0&desSelMnbdNo=thNDZ0uymLNgv5hEBSrMRw%3D%3D&mDispCtgrNo=1162911&sDispCtgrNo=1162941&cupnIssNo1Str=0%2C&cupnIssNo2Str=0%2C&dlvCupnIssNo=0&issueCupnExptCd=&oneClickPayYn=N&oneClickPrdYn=N&changeCupnYN=N&ordType=&syrupCupnYn=Y&rntlOrdPrtblTel=&rakeTrTypeCd=&dispSpceId=&dispSpceRank=0&optTextNameStr=-1%3A2-1.2m&optionStckNo=12647228579&optionPrc=1000&optionOriginalPrc=1000&soCupnAmt=0&moCupnAmt=0&optionStockHid=999928&optArr=1%3A2%2C&optPrdNm=1.2m&optionImageUrl=&optionNm=1.2m&cupnIssNo1=0&addDscAmt=0&cupnIssNo2=0&bonusDscAmt=0&plusDscAmt=0&calcOptRstVal=&calcOptionText=&calcOptionName=&optionStock=1&optNmList=%B1%E6%C0%CC')
# 3070ti
#url2 = 'http://m.11st.co.kr/products/m/3747348290'
#orderURL = 'https://buy.m.11st.co.kr/MW/Order/orderBasicFirstStep.tmall?prdDlvCstStlTyp=01&prdNo=3747348290&incommingCode=01&optionStckNo=14417742470&optionPrc=0&optionStock=1&'

# 3080ti
url2 = 'http://m.11st.co.kr/products/m/3534443331'
orderURL = 'https://buy.m.11st.co.kr/MW/Order/orderBasicFirstStep.tmall?prdDlvCstStlTyp=01&prdNo=3534443331&incommingCode=01&optionStckNo=13558839702&optionPrc=0&optionStock=1&'


caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"

chrome_option1= Options()
chrome_options = Options()
#디버깅 모드 크롬 킨다음에 이미지 block설정하고 11번가 로그인해놓은다음에 쓰셈
#디버깅 모드 연결
#chrome_options.add_experimental_option('debuggerAddress','127.0.0.1:9222')
#chrome_options.headless = True
chrome_options.add_argument("window-size=1920x1080") # 화면크기(전체화면)
#chrome_options.add_argument("disable-gpu") 
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_experimental_option("mobileEmulation",{"deviceName" : "iPhone X"})
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
#chrome_options.add_argument('--blink-settings=imagesEnabled=false')
prefs = {'profile.default_content_setting_values': {
    'images':2,
    'plugins' : 2, 
    'popups': 2, 
    'geolocation': 2, 
    'notifications' : 2, 
    'auto_select_certificate': 2, 
    'fullscreen' : 2, 
    'mouselock' : 2, 
    'mixed_script': 2, 
    'media_stream' : 2, 
    'media_stream_mic' : 2, 
    'media_stream_camera': 2, 
    'protocol_handlers' : 2, 
    'ppapi_broker' : 2, 
    'automatic_downloads': 2, 
    'midi_sysex' : 2, 
    'push_messaging' : 2, 
    'ssl_cert_decisions': 2, 
    'metro_switch_to_desktop' : 2, 
    'protected_media_identifier': 2, 
    'app_banner': 2, 
    'site_engagement' : 2, 
    'durable_storage' : 2,
    }
} 
#chrome_options.add_experimental_option('prefs', prefs)
#driver2 = webdriver.Chrome("./chromedriver.exe",options=chrome_options,desired_capabilities=caps)

chrome_option1.add_experimental_option('debuggerAddress','127.0.0.1:9222')
driver = webdriver.Chrome(chrome_options=chrome_option1,desired_capabilities=caps)

wait =  WebDriverWait(driver,2)

waitshort = WebDriverWait(driver,0.2)
buy = NULL
'''
for i in range(100000000):
    try:
        #buy = driver.find_element(By.CSS_SELECTOR,'body > div.buy_btn.open.animated > div > div.buy > button')
        #buy = waitshort2.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.buy_btn.open.animated > div > div.buy > button')))
        isOpt = driver.find_element(By.CSS_SELECTOR,'#optlst_0')
    except  Exception:
        print('새로고침')
        driver2.refresh()
        time.sleep(0.027)
    else:
        if buy == NULL:
            continue
        #if i < 5:
        #    print('새로고침1')
        #    driver.refresh()
        #    continue
        startTime = time.time()
        #time.sleep(0.08)
        break
    '''
# stockOption 을 가져오는 곳
#optlst_0
#optlst_0 > li.out                 품절된 옵션을 의미함
#optlst_0 > li:nth-child(2)
#optlst_0 > li:nth-child(3)
#optlst_0 > li:nth-child(4) > a

for i in range(100000000):
    try:
        driver.get(orderURL)
        gopay = wait.until(EC.element_to_be_clickable((By.ID,'doPaySubmit')))
        startTime = time.time()
    except  Exception as e:
        pass
    else:
        break
        
        
print("find buy time : ",time.time() - startTime)

#gopay = wait.until(EC.element_to_be_clickable((By.ID,'doPaySubmit')))
driver.execute_script("arguments[0].click();",gopay)
print("go sk pay time : ",time.time() - startTime)

# 서버에서 너무 빠르면 딜레이를 걸어버린다
time.sleep(0.1)

# 여기서 skpay 오류라고 진행이 안되는 경우가 있다
# 그때는 어쩔 수 없다 포기
newframe = NULL
for i in range(1000):
    try:
        newframe = driver.find_element(By.ID,'skpay-ui-frame')
    except:
        driver.execute_script("arguments[0].click();",gopay)
        pass
    else:
        driver.switch_to.frame(newframe)
        break

takeImage = NULL
for i in range(1000):
    try:
        takeImage = driver.find_element(By.XPATH,'//*[@id="keypad11pay-keypad-0"]/span')
        if takeImage == 0:
            print('0 come')
            continue
    except:
        driver.switch_to.default_content()
        driver.switch_to.frame(newframe)
        pass
    else:
        if takeImage == 0:
            continue
        break

#print(takeImage)
if takeImage == 0:
    print("-------bbom--------")
    driver.switch_to.default_content()
    driver.switch_to.frame(newframe)
    takeImage = driver.find_element(By.XPATH,'//*[@id="keypad11pay-keypad-0"]/span')
incoded = takeImage.get_attribute('style')

decodedByte = base64.b64decode(incoded[57:-28])
imageFile = open('test.png','wb')
imageFile.write(decodedByte)
imageFile.close()

result = image_to_string('test.png')
#print(result)
if result.count(' ') == 2:
    #print("warning : 1 뒤가 공백으로 처리됨")
    for i in range(len(result)):
        if result[i] == '1':
            #print('erase')
            result = result[:i+1] + result[i+2:]
            break
#print(result)
keyPad = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(result)):
    if  (result[i] != ' ') and ( result[i] != '\n'):
        keyPad[int(result[i])] = i
    if result[i] == ' ':
        i = i+1
print("skpay decode : ",time.time() - startTime)

#print(keyPad)

buttons = list()
for i in keyPad:
    xpath = '//*[@id="keypad11pay-keypad-'
    xpath += str(i)
    xpath += '"]/span'
    buttons.append(driver.find_element(By.XPATH,xpath))


# 내 비밀번호 889900
# print('비밀번호입력')

driver.execute_script("arguments[0].click();", buttons[8])
driver.execute_script("arguments[0].click();", buttons[8])
driver.execute_script("arguments[0].click();", buttons[9])
driver.execute_script("arguments[0].click();", buttons[9])
driver.execute_script("arguments[0].click();", buttons[0])
driver.execute_script("arguments[0].click();", buttons[0])


print("sk pay pwd Done: ",time.time() - startTime)
# 이후 ars는 자동화 안되어있으니 정신차리고 버튼 잘 누르세요~

# ars 로직이 두 가지 경우중 하나로 랜덤으로 나온다
# 하나는 ars를 해야합니다 확인창을 클릭해야만 넘어가고 버튼의 크기가 달라진다
# 둘째는 ars를 해야합니다 확인창이 없고 버튼의 크기가 "하나"와 다르게 반절이되어 오른쪽에 있다
ars = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#btn-req-auth')))
print("ars click : ",time.time() - startTime)
ars.click()

driver.switch_to.default_content()

print("done")

while True:
    pass
