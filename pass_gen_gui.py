import rnribeiro as rr
import clipboard
window = rr.tk.Tk()
window.geometry('200x135')
def copy():
    clipboard.copy(password)
def newpassword():
    global password_label
    global password
    lenght = int(pass_lenght_input.get())
    if lenght < 4:
        rr.messagebox.showinfo('Error!', 'Password lenght is too short\nTry again!')
        pass_lenght_input.delete(0, rr.tk.END)
        pass_lenght_input.delete(0, '')
    else:
        chars = rr.string.ascii_letters + rr.string.digits + rr.string.punctuation
        password = ''.join(rr.random.sample(chars , lenght))
        pass_label.configure(text = password)

pass_lenght_label = rr.tk.Label(window, text = 'Enter password lenght:')
pass_lenght_label.pack()
pass_lenght_input = rr.tk.Entry(window)
pass_lenght_input.pack()
pass_generator_button = rr.tk.Button(window, text = 'Generate', command = newpassword)
pass_generator_button.pack()
password_label = rr.tk.Label(window, text = 'Password:')
password_label.pack()
pass_label = rr.tk.Label(window, text = '')
pass_label.pack()
copy_button = rr.tk.Button(window, text = 'Copy Password', command = copy)
copy_button.pack()
rr.center_window(window)
window.mainloop()