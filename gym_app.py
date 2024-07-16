import tkinter as tk
from tkinter import simpledialog, messagebox
import uuid
from dbutils import insert_user,get_time_period,get_count
# Create a Tkinter root widget
root = tk.Tk()
root.withdraw()  # Hide the main Tkinter window
# Configure some styling options
root.option_add('*Dialog.msg.font', 'Helvetica 12')
root.option_add('*Dialog.msg.width', 30)
root.option_add('*Dialog.msg.wrapLength', '4i')


class Gym:
    name = 'Talvalkars'
    
    def __init__(self):
        self.gym_name = None
        self.members_present = get_count()
        self.__members_allowed = 200
        self.user_name = None
        self.password = None
        self.age = None
        self.users = {}
        self.menu()


    def menu(self):
        while True:
            input_ = simpledialog.askstring("input","""1.take addmision\n2.check remaining time period\n3.check no of members present\n4.exit\n""")
            if input_ == "1":
                if self.members_present == self.__members_allowed:
                    messagebox.showinfo("sorry","addmisions are not allowed.")
                else:
                    self.user_name = simpledialog.askstring("username","Enter your username")
                    self.password = simpledialog.askstring("password","Enter your password")
                    self.age = simpledialog.askstring("age","Enter your age")
                    self.admission()

            elif input_ == "2":
                self.user_name = simpledialog.askstring("username","Enter your username")
                self.password = simpledialog.askstring("password","Enter your password")
                
                remaining_time = get_time_period(self.user_name, self.password)
                if remaining_time is not None:
                    messagebox.showinfo("Thank you",f"remaining time for user {self.user_name} is {remaining_time} days")
                else:
                    messagebox.showinfo("invalid Credentials","action not allowed.")
                
                
            elif input_ == "3":
                messagebox.showinfo("Input",f"current members present are {self.members_present}")


            elif input_ == "4":
                username = simpledialog.askstring("input","username")
                password = simpledialog.askstring("input","password")
                if username==self.__author and password==self.__password:
                    numbers_of_members = simpledialog.askstring("input","how many members we should set?")
                    self.set_allowed_members(numbers_of_members)
                    messagebox.showinfo("Thank you",f"successfully members are set to {self.__members_allowed}")
                else:
                    messagebox.showinfo("invalid credentials","username and password are not matching.")


            elif input_ == "5":
                messagebox.showinfo("Current users",f"current active users are {list(self.users.keys())}")

            else:
                break



    def admission(self):
        input_ = simpledialog.askstring("input",""" 1.monthly admission\n 2.quaterly admission\n 3.Yearly admission\n""")
        if input_ == "1":
            fees_ = int(simpledialog.askstring("input","please pay 1000 rs.\n"))

            if fees_==1000:
                messagebox.showinfo ('Thank you',f'one month admission for user {self.user_name} is succesfull.')
                insert_user(self.user_name,self.password,self.age,Period=30)
                
            elif fees_>1000 or fees_<1000:
                messagebox.showinfo('incorrect amount entered','please pay correct amount')

        
        if input_ == "2":
            fees_ = int(simpledialog.askstring("input","please pay 4000 rs.\n"))
            if fees_==4000:
                messagebox.showinfo ('Thank you',f'quaterly admission for user {self.user_name} is succesfull.')
                insert_user(self.user_name,self.password,self.age,Period=90)
            elif fees_>4000 or fees_<4000:
                messagebox.showinfo('incorrect amount entered','please pay correct amount')
            
            
        if input_ == "3":
            fees_ = int(simpledialog.askstring("input","please pay 10000 rs.\n"))
            if fees_==10000:
                messagebox.showinfo ('Thank you',f'one year admission for user {self.user_name} is succesfull.')
                insert_user(self.user_name,self.password,self.age,Period=365)
            elif fees_>10000 or fees_<10000:
                messagebox.showinfo('incorrect amount entered','please pay correct amount')
            

            
        
        


gym1 = Gym()