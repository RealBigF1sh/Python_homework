import requests
import decimal


def currency_rates(currents):
    try:
        site = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        site_data = site.text
        cur = site_data.split(currents.upper())
        id_cur = (cur[1].find('Value'))
        course = str(cur[1][id_cur+6:id_cur+13])
        course = course.replace(',', '.')
        course = decimal.Decimal(course)
        print(course)
    except:
        print(None)
