import sys
import time

from requests_html import HTMLSession

session = HTMLSession()
url = 'https://docs.google.com/forms/d/e/1FAIpQLSeKZSgSp_TtQtqtKD0xF0BI10P8fEWN1vM_S5abDe16ybihuw/viewform'
url_send = 'https://docs.google.com/forms/d/e/1FAIpQLSeKZSgSp_TtQtqtKD0xF0BI10P8fEWN1vM_S5abDe16ybihuw/formResponse'

"""
Кукисы копируйте сюда
"""
google_cookies = {
    '1P_JAR': '2019-2-20-21',
    'APISID': 'Z53kWRoJFICw0WU4/AIbc1hdHtHCBjTTzD',
    'GOOGLE_ABUSE_EXEMPTION': 'ID=82d2222b71a9ad9f:TM=1550689522:C=r:IP=46.0.101.157-:S=APGng0svrAJPLx-rdXokiP7XIK77HN-64A',
    'HSID': 'ALJd8ykHxq2N2w943',
    'NID': '160=KDU8ThGP_xWTQ-uRFIeNKLcwIPb-KE30mZ1SBwHRwXXZBo-pQILPVCD-MIHwVX8ke9raM6C--zVj95FxX1DghWAXCvy9EwZRAvVBvl9kAaAH4Atn1Jcu5L1mjuO0vVUWlSVPuBYZ0g9MPTHjvA5F_BuLRXcdYjH5n12ASbQkzmuH0RtQ4IYqRbYPQYggBUtsOQUOABKZxHibxy51gNVp',
    'OGP': '-19010494:',
    'OGPC': '19010494-1:',
    'S':'spreadsheet_forms=HfKXaqHf87heZm-PCA_TDIOACwctSoWf',
    'SAPISID': 'Ow87CDTdVgGHz2ld/AaLK02x8zRQvRmuA0',
    'SID': '0Aablma7ljCsrZQI5dIp2rKXuZ1L4PXhCJtFKxQlyD_AGg6oLY3eFv-qXT_E9jcfMX0LnA.',
    'SIDCC': 'AN0-TYtf8GPbm8tQqunw7FA057NL-KhEoAX3Smt5JhDnDrggQ2GfWOBl_NgNBE9ZnRmoUVVLe_57',
    'SSID': 'Akajyg4lOQhFaNXvC'
}

while True:
    r = session.get(url, cookies=google_cookies)
    selected_form = r.html.find('#mG61Hd', first=True)
    if selected_form:
        inputs = selected_form.find('input')
        fbzx_input = inputs[-1]
        fbzx_value = fbzx_input.attrs.get('value')
        data_list = ['Maxim Tarabrin'
                     ]
        new_data = {}
        for id, input in enumerate(inputs):
            try:
                new_data[input.attrs.get('name')] = data_list[id]
            except Exception:
                new_data[input.attrs.get('name')] = input.attrs.get('value')
        new_r = session.post(url=url_send, data=new_data)
        try:
            print(new_r.html.find('.freebirdFormviewerViewResponseConfirmationMessage', first=True).text)
        except Exception:
            print('При отправке формы произошла ошибка')
    else:
        try:
            print(r.html.find('#innerContainer', first=True).text)
        except Exception:
            print(r.html.find('.freebirdFormviewerViewResponseConfirmContentContainer',first=True).text)
            sys.exit()
    time.sleep(2)
