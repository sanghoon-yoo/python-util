from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


###############################################
#Options Setting
###############################################
#service = Service(ChromeDriverManager(version="119").install())
options = Options()

user_data = r"C:\Users\sanghoon.yoo\AppData\Local\Google\Chrome\User Data"

options.add_argument(f"user-data-dir={user_data}")

driver = webdriver.Chrome(r'C:\Users\sanghoon.yoo\chromedriver_win32\chromedriver.exe', options = options)

driver.implicitly_wait(10)

ACCOUNT_INFO = {'Senario1.userId':''
                , 'Senario1.passwd':''}

PAY_INFO = {}

###############################################
# AhnLabMall QA Start
###############################################
driver.get('https://shop.ahnlab.com')  
print(driver.title + "Access.")

driver.implicitly_wait(10)

###############################################
# Senario1. 개인 신규 카드구매 당일반품
###############################################
#로그인화면 이동
driver.execute_script(
  "(function() { " +
  "goLogin();" + 
  "})();"
)

driver.implicitly_wait(10)

#로그인정보 입력
driver.find_elements(By.ID, 'userId')[0].click()
sleep(1)
driver.find_elements(By.ID, 'userId')[0].clear()
sleep(1)
driver.find_elements(By.ID, 'passwd')[0].click()
sleep(1)
driver.find_elements(By.ID, 'passwd')[0].clear()
sleep(1)
driver.find_elements(By.ID, 'userId')[0].send_keys(ACCOUNT_INFO.get('Senario1.userId'))
driver.find_elements(By.ID, 'passwd')[0].send_keys(ACCOUNT_INFO.get('Senario1.passwd'))

driver.implicitly_wait(10)

#로그인
driver.find_elements(By.ID, 'loginBtn')[0].click()

driver.implicitly_wait(10)

print("Senario1.Login Success")

#제품상세이동
driver.execute_script(
  "(function() { " +
  "goProduct('P000014038');" + 
  "})();"
)

driver.implicitly_wait(10)
print("Senario1.Product Detail Success")

#제품구입이동
driver.execute_script(
  "(function() { " +
  "goLoginByGuest('P000014038');" + 
  "})();"
)

driver.implicitly_wait(10)
print("Senario1.Product OrderPage Success")

#약관동의
driver.execute_script(
  "(function() { " +
  "document.getElementById('agreeV3Clinic').checked = true;" + 
  "})();"
)

driver.implicitly_wait(10)
print("Senario1.Product Agree Check Success")

#이니시스 결제창 오픈
driver.execute_script(
  "(function() { " +
  "orderPay(document.OrderForm);" + 
  "})();"
)

inicis_script="""if($('#inputAll').prop('checked')){
		$payForm.find('input[name=check]').prop('checked',true);
	}else{
		$payForm.find('input[name=check]').prop('checked',false);
	}
	
	if(selectMenuId == 'Card') {
		if(($('#inputChk3').prop('checked') && $('#inputChk4').prop('checked')) && ($('.btnPaymnt').hasClass('selected') || ($('#spanSelectCardCode .dropdown').find('dt a span.value').length > 0 && $('#spanSelectCardCode .dropdown').find('dt a span.value').html() != '') || ($('#spanSelectPayCode .dropdown').find('dt a span.value').length > 0 && $('#spanSelectPayCode .dropdown').find('dt a span.value').html() != ''))) {
			$('.bottomBtn').removeClass('btnDis');
			$('.btnType09').css('color', $('input[name=colorView]').val());
			var page = $('#curPage').val();
			setCardBtnTitle('');
			//$('#'+page+'Btn').focus();
		} else {
			$('.bottomBtn').addClass('btnDis');
			$('.btnType09').css('color', '');
			$('#CardBtn').attr('title','');
			$('#inputFocus').focus();
		}
	}"""

driver.implicitly_wait(10)
print("Senario1.Inicis Opener Success")

#이니시스 약관동의
content = driver.find_element_by_id("ORDER_PAY")
driver.switch_to.frame(content)
content = driver.find_element_by_id("iframe")
driver.switch_to.frame(content)

sleep(2)

driver.execute_script(
  "(function() { " +
  "document.getElementById('inputAll').checked = true;" + 
  "})();"
)

driver.execute_script(
  "(function() { " +
  inicis_script + 
  "})();"
)

driver.execute_script(
  "(function() { " +
  "document.getElementById('14').click();" + 
  "})();"
)
print("Senario1.Inicis Agree Check Success")

#카드결제 선택
driver.execute_script(
  "(function() { " +
  "document.getElementById('CardBtn').click();" + 
  "})();"
)

driver.implicitly_wait(10)
print("Senario1.Inicis PayKind Select Success")

#신한카드 결제정보입력
content = driver.find_element_by_id("overlayFrame")
driver.switch_to.frame(content)

sleep(2)

driver.execute_script(
  "(function() { " +
  "onLoadHandlerFan();" + 
  "})();"
)

sleep(5)
driver.implicitly_wait(10)

driver.find_elements(By.ID, 'app_pwd')[0].click()

driver.implicitly_wait(10)

#비밀번호가 123456일 경우
driver.execute_script(
  "(function() { " +
  "document.querySelectorAll('.kpd-data')[1].click();" +
  "document.querySelectorAll('.kpd-data')[2].click();" +
  "document.querySelectorAll('.kpd-data')[3].click();" +
  "document.querySelectorAll('.kpd-data')[4].click();" +
  "document.querySelectorAll('.kpd-data')[5].click();" +
  "document.querySelectorAll('.kpd-data')[6].click();" +
  "document.querySelectorAll('.kpd-data')[13].click();" +
  "})();"
)

driver.implicitly_wait(10)

driver.execute_script(
  "(function() { " +
  "doSubmit2();" + 
  "})();"
)

driver.implicitly_wait(10)
print("Senario1.Inicis Card ShinhanPay Success")

#이니시스 최종결제
driver.switch_to_default_content()

content = driver.find_element_by_id("ORDER_PAY")
driver.switch_to.frame(content)
content = driver.find_element_by_id("iframe")
driver.switch_to.frame(content)

driver.implicitly_wait(10)

driver.find_elements(By.ID, 'payDoneBtn')[0].click()

driver.implicitly_wait(10)

driver.switch_to_default_content()

driver.implicitly_wait(10)
print("Senario1.AhnLabMall Card Pay Success")
sleep(3)

#반품
driver.execute_script(
  "(function() { " +
  "location.href = '/jump/fp/member/viewOrder.do?cmd=viewOrder&ordId=' + document.querySelectorAll('.fcBlue')[3].textContent;" + 
  "})();"
)

driver.implicitly_wait(10)

driver.find_elements(By.ID, 'btn_cancel')[0].click()

driver.implicitly_wait(10)
sleep(3)

driver.switch_to_window(driver.window_handles[1])

driver.implicitly_wait(10)

#driver.get_window_position(driver.window_handles[1])

driver.implicitly_wait(10)

#사유입력
driver.execute_script(
  "(function() { " +
  "document.getElementById('resultMsg').innerHTML = '자동화 QA TEST';" + 
  "})();"
)

driver.implicitly_wait(10)

driver.find_elements(By.ID, 'btn_cancel_request')[0].click()

print("Senario1.AhnLabMall Card Refund Success")
sleep(5)

#driver.quit()

###############################################
# Senario2. 기업 신규 카드구매 당일반품
###############################################
