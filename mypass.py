from tkinter import *
import random
import json


def pass_generator():
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=']

    # Use fixed values for password length in the GUI version
    al = 8  # Number of alphabets
    num = 4  # Number of numbers
    sym = 2  # Number of symbols

    password_list = []

    for _ in range(al):
        password_list.append(random.choice(alphabets))

    for _ in range(num):
        password_list.append(random.choice(numbers))

    for _ in range(sym):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    generated_password = ''.join(password_list)
    
    # Set the generated password in the password entry
    pass_entry.delete(0, END)
    pass_entry.insert(0, generated_password)



def save_to_file():
    website = web_entry.get()
    email_username = email_entry.get()
    password = pass_entry.get()
    new_data={
        website :{
            "email": email_username,
            "password": password
        }
    }
    
    # Check if any field is empty before saving
    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        warning = Tk()
        warning.title('warning')
        warning.config(padx=100, pady=100, bg="black")
        warning.minsize(600, 200)
        warning_label = Label(warning, text='YOU MUST FILL ALL THE GAPS', font=('arial', 20, 'bold'), bg="black", fg="red")
        warning_label.grid(column=0, row=0)

        def go_back():
            warning.destroy()

        ok = Button(warning, width=20 , text='Go Back' , command=go_back , font=('arial', 10, 'bold'),  fg="red")
        ok.grid(column=0,row=1)




        warning.mainloop()

    else:
        with open('data.json', 'r') as file:
            data= json.load(file)
            data.update(new_data)

        with open('data.json' , 'w') as file:
            json.dump(data , file , indent=4)


        saved = Tk()
        saved.title('saved succesfully')
        saved.config(padx=100, pady=100, bg="black")
        saved.minsize(600, 200)
        saved_label = Label(saved, text=f'The Password of {website.capitalize()} Is Added The Data Store', font=('Lucida Handwriting', 20, 'bold'), bg="black", fg="green")
        saved_label.grid(column=0, row=0)
        def go_back():
            saved.destroy()

        ok = Button(saved, width=20 , text='Go Back' , command=go_back , font=('arial', 10, 'bold'),  fg="green")
        ok.grid(column=0,row=1)

        # Clear input fields after saving
        web_entry.delete(0, END)
        email_entry.delete(0, END)
        pass_entry.delete(0, END)



def read_from_data():
    website = web_entry.get().lower()  # Convert to lowercase for consistency

    try:
        # Open the JSON file and load the data
        with open("data.json", "r") as file:
            data = json.load(file)

        # Check if the website exists in the data
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]

            search_window = Tk()
            search_window.title(website)
            search_window.config(padx=100, pady=100, bg="black")
            search_label = Label(search_window, text=f"website: {website}\n Email/Username: {email}\n Password: {password}", font=('arial', 20, 'bold'), bg="black", fg="green")
            search_label.grid(column=0, row=0)

            search_window.mainloop()

        else:
            # Show a warning if the website is not found
            warning = Tk()
            warning.title('Website not found')
            warning.config(padx=100, pady=100, bg="black")
            warning.minsize(600, 200)
            warning_label = Label(warning, text=f'No data found for {website.capitalize()}', font=('Lucida Handwriting', 20, 'bold'), bg="black", fg="red")
            warning_label.grid(column=0, row=0)

            def go_back():
                warning.destroy()

            ok = Button(warning, width=20 , text='Go Back' , command=go_back , font=('Lucida Handwriting', 10, 'bold'),  fg="red")
            ok.grid(column=0,row=1)

            warning.mainloop()

    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        error_window = Tk()
        error_window.title('Error')
        error_window.config(padx=100, pady=100, bg="black")
        error_label = Label(error_window, text='Data file not found.', font=('Lucida Handwriting', 20, 'bold'), bg="black", fg="red")
        error_label.grid(column=0, row=0)

        def go_back():
            error_window.destroy()

        ok = Button(error_window, width=20 , text='Go Back' , command=go_back , font=('Lucida Handwriting', 10, 'bold'),  fg="red")
        ok.grid(column=0,row=1)

        error_window.mainloop()


#########################################################################################################################################
window = Tk()
window.title("my passwords")
window.config(padx=100, pady=100, bg="black")
window.minsize(600, 600)

# Canvas and Image
canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
pic = PhotoImage(file='C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/my password (2).png')
canvas.create_image(110, 110, image=pic)  # Change coordinates for better centering
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website', font=('arial', 10, 'bold'), bg="black", fg="white")
website_label.grid(column=0, row=2)

email_username_label = Label(text='Email/Username', font=('arial', 10, 'bold'), bg="black", fg="white")
email_username_label.grid(column=0, row=3)

password_label = Label(text='Password', font=('arial', 10, 'bold'), bg="black", fg="white")
password_label.grid(column=0, row=4)

# Entry fields
web_entry = Entry(width=40)
web_entry.grid(column=1, row=2, columnspan=2)

email_entry = Entry(width=40)
email_entry.grid(column=1, row=3, columnspan=2)

pass_entry = Entry(width=40)
pass_entry.grid(column=1, row=4)

# Buttons
add_button = Button(text="Add", width=35 , command=save_to_file)
add_button.grid(column=1, row=5, columnspan=2)

generate_password_button = Button(text='Generate Password', command=pass_generator)
generate_password_button.grid(column=3, row=4)

search_button= Button(text="search" ,width=15 , command= read_from_data)
search_button.grid(column=3, row=2)




#########################################################################################################################################

window.mainloop()
