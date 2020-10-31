import string
import random
import clipboard
def newpassword(lenght):
    if lenght < 4:
        print('Error!', 'Password lenght is too short\nTry again!')
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.sample(chars , lenght))
        print(password)
        if input('Copy password (y/n): ') == 'y':
            clipboard.copy(password)
newpassword(int(input('Lenght: ')))