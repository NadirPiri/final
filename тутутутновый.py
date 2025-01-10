import tkinter as tk
from tkinter import messagebox
import json
import os

if not os.path.exists("users.json"):
    with open("users.json", "w") as file:
        json.dump([], file)


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry("300x200")

        tk.Button(self, text="Sign Up", command=self.open_sign_up).pack(pady=10)
        tk.Button(self, text="Sign In", command=self.open_sign_in).pack(pady=10)

    def open_sign_up(self):
        self.destroy()
        SignUp().mainloop()

    def open_sign_in(self):
        self.destroy()
        SignIn().mainloop()


class SellerPanel(tk.Tk):
    def __init__(self, username):
        super().__init__()
        self.title("Seller Panel")
        self.geometry("400x300")
        self.username=username
        tk.Label(self, text=f"Welcome to TechnoShop, {username} (Seller)").pack(pady=10)
        tk.Button(self, text="Add Product", command=self.add_product).pack(pady=10)
        tk.Button(self, text="View Products", command=self.view_products).pack(pady=10)
        tk.Button(self, text="Go back", command=self.back).pack(pady=10)

    def back(self):
        self.destroy()
        SignIn().mainloop()



    def add_product(self):
        self.destroy()
        Addp().mainloop()



    def view_products(self):
        self.destroy()
        Newpanel().mainloop()


class Addp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Add Product")
        self.geometry("800x800")
        self.newbtnbtn=tk.Button(self,text="ADD IPHONE 15 PRO MAX",command=self.addiphone15)
        self.newbtnbtn.pack(pady=20)
        self.newbtnbtn2 = tk.Button(self, text="ADD SAMSUNG WATCH", command=self.addss)
        self.newbtnbtn2.pack(pady=40)
        tk.Button(self,text="Go back",command=self.back).pack(pady=10)


    def back(self):
        self.destroy()
        SellerPanel("username").mainloop()

    def addss(self):
        self.destroy()

        new_panel = Newpanel()
        new_panel.add_product2()

    def addiphone15(self):

        self.destroy()

        new_panel = Newpanel()
        new_panel.add_product()

class CustomerPanel(tk.Tk):
    def __init__(self, username):
        super().__init__()
        self.title("Customer Panel")
        self.geometry("400x300")
        tk.Label(self, text=f"Welcome to TechnoShop, {username} (Customer)").pack(pady=10)
        tk.Button(self, text="View Products", command= self.view_products).pack(pady=10)
        tk.Button(self,text="Go back",command=self.back).pack(pady=10)
    def back(self):
        self.destroy()
        SignIn().mainloop()
    def view_products(self):
        self.destroy()
        Newpanel().mainloop()



class Newpanel(tk.Tk):

    def __init__(self):
        super().__init__()



        self.title("Products")
        self.geometry("800x800")
        self.display_initial_products()

        tk.Button(self, text="Go back", command=self.back).place(x=700,y=700)

    def display_initial_products(self):
        self.watch = tk.PhotoImage(file="applewatchson.png")
        self.watch_resized=self.watch.subsample(3,2)
        self.watch_label = tk.Label(self, image=self.watch_resized)
        self.watch_label.place(x=0,y=0)
        self.wbutton=tk.Button(self,text="BUY AN APPLE WATCH",command=self.deletewatch)
        self.wbutton.place(x=0,y=200)

        self.iphone=tk.PhotoImage(file="iphonewww.png")
        self.iphone_resized=self.iphone.subsample(5,5)
        self.iphone_label=tk.Label(self,image=self.iphone_resized)
        self.iphone_label.place(x=300,y=0)
        self.ibutton = tk.Button(self, text="BUY AN IPHONE 16", command=self.deletephone)
        self.ibutton.place(x=300, y=200)

        self.smasung=tk.PhotoImage(file="my_samsung.png")
        self.samsung_resized=self.smasung.subsample(3,3)
        self.samsung_label=tk.Label(self,image=self.samsung_resized)
        self.samsung_label.place(x=600,y=0)
        self.sbutton = tk.Button(self, text="BUY SAMSUNG S24 ", command=self.deletesamsung)
        self.sbutton.place(x=600, y=200)
    def add_product(self):
        self.iphone15 = tk.PhotoImage(file="iphone15.png")
        self.iphone15_resized = self.iphone15.subsample(4, 4)
        self.iphone15_label = tk.Label(self, image=self.iphone15_resized)
        self.iphone15_label.place(x=0, y=400)
        self.i15button = tk.Button(self, text="BUY AN IPHONE 15 PRO MAX", command=self.delete15)
        self.i15button.place(x=0, y=700)
    def add_product2(self):
        self.ss = tk.PhotoImage(file="watchsamsung.png")
        self.ss_resized = self.ss.subsample(6, 6)
        self.ss_label = tk.Label(self, image=self.ss_resized)
        self.ss_label.place(x=300, y=400)
        self.ss_btn = tk.Button(self, text="BUY SAMSUNG WATCH", command=self.deletess)
        self.ss_btn.place(x=300, y=700)



    def back(self):
        self.destroy()
        SignIn().mainloop()
    def deletewatch(self):
        self.watch_label.destroy()
        self.wbutton.destroy()
        messagebox.showinfo("SOLD","CONGRATULATIONS YOU BOUGTH  APPLE WATCH")
    def deletess(self):
        self.ss_label.destroy()
        self.ss_btn.destroy()
        messagebox.showinfo("SOLD","CONGRATULATIONS YOU BOUGTH SAMSUNG WATCH")

    def delete15(self):
        self.iphone15_label.destroy()
        self.i15button.destroy()
        messagebox.showinfo("SOLD", "CONGRATULATIONS YOU BOUGTH  IPHONE 15 PRO MAX")
    def deletephone(self):
        self.iphone_label.destroy()
        self.ibutton.destroy()
        messagebox.showinfo("SOLD","CONGRATULATIONS YOU BOUGTH  IPHONE 16")

    def deletesamsung(self):
        self.samsung_label.destroy()
        self.sbutton.destroy()
        messagebox.showinfo("SOLD", "CONGRATULATIONS YOU BOUGTH SAMSUNG S24")
class SignIn(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sign In")
        self.geometry("300x200")

        tk.Label(self, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack()

        tk.Button(self, text="Sign In", command=self.sign_in).pack(pady=10)
        tk.Button(self, text="Go back", command=self.back).pack(pady=10)

    def back(self):
        self.destroy()
        MainApp().mainloop()

    def sign_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            with open("users.json", "r") as file:
                users = json.load(file)
            for user in users:
                if username == user["username"] and password == user["password"]:
                    self.destroy()
                    if user["role"] == "seller":
                        SellerPanel(username).mainloop()
                    elif user["role"] == "customer":
                        CustomerPanel(username).mainloop()
                    return

            messagebox.showerror("Error", "Invalid username or password")
        except FileNotFoundError:
            messagebox.showerror("Error", "No users found, please sign up first.")


class SignUp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sign Up")
        self.geometry("300x500")

        tk.Label(self, text="First Name").pack(pady=5)
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.pack()

        tk.Label(self, text="Last Name").pack(pady=5)
        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.pack()

        tk.Label(self, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack()

        tk.Label(self, text="Phone").pack(pady=5)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.pack()

        tk.Label(self,text="Age").pack(pady=5)
        self.age_entry=tk.Entry(self)
        self.age_entry.pack()

        tk.Label(self, text="Email").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Label(self, text="Role (seller/customer)").pack(pady=5)
        self.role_entry = tk.Entry(self)
        self.role_entry.pack()

        tk.Button(self, text="Sign Up", command=self.sign_up).pack(pady=10)
        tk.Button(self, text="Go back", command=self.back).pack(pady=10)
    def back(self):
        self.destroy()
        MainApp().mainloop()

    def sign_up(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        phone = self.phone_entry.get()
        age=self.age_entry.get()
        email=self.email_entry.get()
        role = self.role_entry.get()

        if not (8 <= len(username) <= 16):
            messagebox.showerror("Error", "Username must be 8-16 characters long")
            return

        if not (8 <= len(password) <= 16):
            messagebox.showerror("Error", "Password must be 8-16 characters long")
            return

        if not phone.isdigit():
            messagebox.showerror("Error", "Phone number must contain only digits")
            return
        if not age.isdigit():
            messagebox.showerror("Error", "Age must contain only digits")
            return
        if "@"not in email:
            messagebox.showerror("Error","inpoper email")
            return
        if role not in ["seller", "customer"]:
            messagebox.showerror("Error", "Role must be 'seller' or 'customer'")
            return

        new_user = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "password": password,
            "phone": phone,
            "age":age,
            "email":email,
            "role": role
        }

        with open("users.json", "r+") as file:
            users = json.load(file)

            users.append(new_user)
            file.seek(0)
            json.dump(users, file, indent=4)

        messagebox.showinfo("Success", "Sign Up Successful!")
        self.destroy()
        MainApp().mainloop()


if True:
    app = MainApp()
    app.mainloop()