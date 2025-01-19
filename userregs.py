import customtkinter as ctk

root = ctk.CTk()
root.title("Gateway")
root.geometry("400x500")

user_infos = []

def sign_in():
    global user_infos
    global email_bar,pw_bar
    user_input = email_bar.get()
    pw = pw_bar.get()
    user_infos.append(pw)
    user_infos.append(user_input)

    if not user_input.strip():
        return
    if not pw.strip():
        return

    for widget in main_frame.winfo_children():
        widget.destroy()

    label_1 = ctk.CTkLabel(master=main_frame,text="Sign In \nSuccessful.",font=("Bahnschrift SemiBold",50))
    label_1.pack(pady=100)

    back_btn = ctk.CTkButton(master=main_frame,text="Go Back",font=("Bahnschrift SemiBold",20),height=40,width=100,command=home_page)
    back_btn.pack(pady=5)

    label_0 = ctk.CTkLabel(master=main_frame,text="You're all catch up for now.",font=("Bahnschrift SemiBold",15))
    label_0.pack(pady=30)

def home_page():
    for widget in main_frame.winfo_children():
        widget.destroy()

    headline = ctk.CTkLabel(master=main_frame,text="Gateway",font=("Bahnschrift SemiBold",80))
    headline.pack(pady=20)

    global email_bar,pw_bar
    email_bar = ctk.CTkEntry(master=main_frame,placeholder_text="Email",font=("Arial",15),height=35,width=270)
    email_bar.pack(pady=5)

    pw_bar = ctk.CTkEntry(master=main_frame,placeholder_text="Password",font=("Arial",15),height=35,width=270)
    pw_bar.pack(pady=5)

    login_btn = ctk.CTkButton(master=main_frame,text="Login",font=("Bahnschrift SemiBold",20),height=40,width=100,command=login)
    login_btn.pack(pady=20)

    new_user = ctk.CTkLabel(master=main_frame,text="New user ? Click Sign In.",font=("Arial",15))
    new_user.pack()

    signin_btn = ctk.CTkButton(master=main_frame,text="Sign In",font=("Bahnschrift SemiBold",20),height=40,width=100,command=sign_in)
    signin_btn.pack(pady=5)

def popup_disable():
    feedback.configure(text="")

def login():
    global user_infos
    global email_bar,pw_bar
    user_input = email_bar.get()
    pw = pw_bar.get()

    if not user_input.strip():
        return
    if not pw.strip():
        return

    if user_input in user_infos and pw in user_infos:   
        for widget in main_frame.winfo_children():
            widget.destroy()

        label_1 = ctk.CTkLabel(master=main_frame,text="Login Successful.",font=("Bahnschrift SemiBold",40))
        label_1.pack(pady=100)

        back_btn = ctk.CTkButton(master=main_frame,text="Go Back",font=("Bahnschrift SemiBold",20),height=40,width=100,command=home_page)
        back_btn.pack(pady=5)

        label_0 = ctk.CTkLabel(master=main_frame,text="You're all catch up for now.",font=("Bahnschrift SemiBold",15))
        label_0.pack(pady=50)
    else:
        global feedback
        feedback = ctk.CTkLabel(master=main_frame,text="User Not Found.",font=("Arial",10),text_color="Red")
        feedback.pack()
        root.after(3000,popup_disable)
        return


main_frame = ctk.CTkFrame(master=root)
main_frame.pack(expand=True,fill="both",padx=20,pady=20)

headline = ctk.CTkLabel(master=main_frame,text="Gateway",font=("Bahnschrift SemiBold",80))
headline.pack(pady=20)

email_bar = ctk.CTkEntry(master=main_frame,placeholder_text="Email",font=("Arial",15),height=35,width=270)
email_bar.pack(pady=5)

pw_bar = ctk.CTkEntry(master=main_frame,placeholder_text="Password",font=("Arial",15),height=35,width=270)
pw_bar.pack(pady=5)

login_btn = ctk.CTkButton(master=main_frame,text="Login",font=("Bahnschrift SemiBold",20),height=40,width=100,command=login)
login_btn.pack(pady=20)

new_user = ctk.CTkLabel(master=main_frame,text="New user ? Click Sign In.",font=("Arial",15))
new_user.pack()

signin_btn = ctk.CTkButton(master=main_frame,text="Sign In",font=("Bahnschrift SemiBold",20),height=40,width=100,command=sign_in)
signin_btn.pack(pady=5)

root.mainloop()