import rnribeiro as rr
import clipboard
def newpassword(lenght):
    if lenght < 4:
        print('Error!', 'Password lenght is too short\nTry again!')
    else:
        chars = rr.string.ascii_letters + rr.string.digits + rr.string.punctuation
        password = ''.join(rr.random.sample(chars , lenght))
        print(password)
        if input('Copy password (y/n): ') == 'y':
            clipboard.copy(password)
newpassword(int(input('Lenght: ')))