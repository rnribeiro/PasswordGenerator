import tkinter as tk
import clipboard
window = tk.Tk()
window.geometry('200x135')
def copy():
    clipboard.copy(password)

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    window_width = width + 2 * frm_width
    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    window_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth() // 2 - window_width // 2
    y = window.winfo_screenheight() // 2 - window_height // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.deiconify()

def newpassword():
    global password_label
    global password
    lenght = int(pass_lenght_input.get())
    if lenght < 4:
        messagebox.showinfo('Error!', 'Password lenght is too short\nTry again!')
        pass_lenght_input.delete(0, tk.END)
        pass_lenght_input.delete(0, '')
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.sample(chars , lenght))
        pass_label.configure(text = password)

pass_lenght_label = tk.Label(window, text = 'Enter password lenght:')
pass_lenght_label.pack()
pass_lenght_input = tk.Entry(window)
pass_lenght_input.pack()
pass_generator_button = tk.Button(window, text = 'Generate', command = newpassword)
pass_generator_button.pack()
password_label = tk.Label(window, text = 'Password:')
password_label.pack()
pass_label = tk.Label(window, text = '')
pass_label.pack()
copy_button = tk.Button(window, text = 'Copy Password', command = copy)
copy_button.pack()
center_window(window)
window.mainloop()