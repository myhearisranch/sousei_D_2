from selenium import webdriver
from time import sleep

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])

print("学籍番号を入力してください。")
student_number = input()
print("パスワードを入力してください。")
password = input()

# chromeの鼓動
browser = webdriver.Chrome('chromedriver.exe')

# Googleにアクセスする
browser.get('https://tora-net.sti.chubu.ac.jp/portal/top.do')


elem_username = browser.find_element_by_name('userId')
elem_username.send_keys(student_number)

elem_password = browser.find_element_by_name("password")
elem_password.send_keys(password)

elem_login_button = browser.find_element_by_id("loginButton")
elem_login_button.click()


browser.quit()



# 参考文献
# ブラウザ自動ログイン
# https://www.youtube.com/watch?v=f8FXUUQ4uRA



# ChromeDriverのインストール
# https://www.mittsu-kosen.com/chromedriver%e3%82%92windows10%e3%81%a7%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%99%e3%82%8b%e6%96%b9%e6%b3%95%e3%80%90%e7%94%bb%e5%83%8f%e4%bb%98%e3%81%8d%e3%80%91

# エラー解決
# https://qiita.com/syoshika_/items/288fc8bf552672589f4c