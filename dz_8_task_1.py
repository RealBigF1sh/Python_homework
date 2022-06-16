import re
pattern = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')
def email_parse(email):
    mail_info = pattern.findall(email)
    if mail_info:
        name, place = mail_info[0]
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, place)


email_parse('tarans.fishborn@gmail.com')
email_parse('RealBigF1sh@yandexru')
