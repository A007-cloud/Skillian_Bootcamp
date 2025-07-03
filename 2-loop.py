emails = ['aditya788@gamil.com',
          'aditya788@gamil.in',
          '@gamil.com',
          'aditya.com',
          'aditya788gamil.com']
import re
def is_valid_email(emails):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    for email in emails:
        # print(email);
        if re.match(pattern, email):
            print('Valid Email')
        else:
            print('Invalid Email')


is_valid_email(emails)