#Homework Projects
#1.To-do list Application:
# class Task:
#     def __init__(self, title, description, due_date, status):
#         self.title=title
#         self.description=description
#         self.due_date=due_date
#         self.status=status
#     def __str__(self):
#         return f"{self.title} | {self.description} | Due: {self.due_date} | Status: {self.status} "
    
class ToDoList:
    def __init__(self):
        self.tasks=[]
    def add_task(self):
        title = input("Enter title: ")
        description = input("Enter description: ")
        due_date = input("Enter due date: ")
        status = input("Enter status (Complete✅/Incomplete❌): ").capitalize()
        task = Task(title, description, due_date, status)
        self.tasks.append(task)
        print(f"Task is added successfully")
    def mark_complete(self):
        marked =input("Which task you have finished?")
        for task in self.tasks:
            if task.title==marked:
                task.status='Complete'
    def list_all_tasks(self):
       return "\n".join(str(task) for task in self.tasks)
    def incomplete_tasks(self):
        incomplete=[]
        for task in self.tasks:
            if task.status=='Incomplete':
                incomplete.append(task)
        return "\n".join(str(task) for task in incomplete)


ToDo = ToDoList()
def print_menu():
    print("\nChoose an option: ")
    print("1. Add task")
    print("2. Mark task as complete")
    print("3. Show all tasks")
    print("4. Show incomplete tasks")
    print("5. Exit")

while True:
    print_menu()
    command = input("Enter a number: ")
    if command == '1':
        ToDo.add_task()
    elif command == '2':
        ToDo.mark_complete()
    elif command == '3':
        print(ToDo.list_all_tasks())
    elif command == '4':
        print(ToDo.incomplete_tasks())
    else:
        exit()


#Simple Blog System
class Post:
    def __init__(self, title, content,author):
        self.title=title
        self.content=content
        self.author=author
    def __str__(self):
        return f"{self.title} | Content: {self.content} | Author: {self.author} "
class Blog:
    def __init__(self):
        self.posts=[]
    def add_post(self):
        title = input("Enter title: ")
        content= input("Enter content: ")
        author = input("Enter author: ")
        blog_post = Post(title,content,author)
        self.posts.append(blog_post)
        print(f"Post is added successfully")
    def list_all_posts(self):
       return "\n".join(str(blog_post) for blog_post in self.posts)
    def display_by_author(self):
        name=input("Enter author: ")
        matching_author=[]
        for post in self.posts:
            if post.author == name:
                matching_author.append(post)
        if matching_author!=[]:
            return "\n".join(str(obj) for obj in matching_author)
        else:
            return f"No posts by this author."
Blogging= Blog()
def print_menu():
    print("\nChoose an option: ")
    print("1. Add post")
    print("2. List all posts")
    print("3. Display posts by author")
    print("4. Exit")
while True:
    print_menu()
    command = input("Enter a number: ")
    if command == '1':
        Blogging.add_post()
    elif command == '2':
       print(Blogging.list_all_posts())
    elif command == '3':
        print(Blogging.display_by_author())
    else:
        exit()


#3. Simple Banking System
import datetime
class Account:
    def __init__(self,holder_name):
        opened_date = datetime.datetime.today()
        self.holder_name = holder_name
        self.opened_date = opened_date
        self.id = 0
        self.balance = 0
        self.closed_date = None
    def deposit_money(self,deposit):
        self.balance += deposit
        return self.balance
    def withdraw_money(self,withdraw):
        if self.balance >= withdraw:
            self.balance -= withdraw
            return True
        return False
    def close_account(self):
        self.closed_date = datetime.datetime.today()
    def __str__(self):
        return f"Account Number: {self.id} | Holder Name: {self.holder_name} | Balance: {self.balance}"
class Bank:
    account_list = []
    last_id = 0
    def __init__(self,name):
        self.name  = name
    def add_account(self):
        self.last_id += 1
        holder_name = input("Enter Your Name: ")
        account_obj = Account(holder_name)
        account_obj.id = self.last_id
        self.account_list.append(account_obj)
        print(f"Acccount Number {self.last_id} was added successfully")
    def search(self,id):
        for obj in self.account_list:
            if obj.id == id:
                return obj
        return False
    def deposit_account(self,id):
        a = self.search(id)
        if isinstance(a,Account):
            deposit_amount = int(input("Enter your deposit amount! ex: 1000$ 💸 "))
            balance = a.deposit_money(deposit_amount)
            print(f"Depositing Process is completed successfully | Current Balance: {balance}")
        else:
            print(f"Account Number {id} is not found")
    def withdraw_account(self,id):
        a = self.search(id)
        if isinstance(a,Account):
            withdraw_amount = int(input("Enter withdraw amount "))
            result = a.withdraw_money(withdraw_amount)
            if result:
                print(f"The withdraw process completed successfully! withdraw Amount: {withdraw_amount} | Current Balance: {a.balance}")
            else:
                print(f"Your account has not available amount! Amount: {withdraw_amount} | Current Balance: {a.balance}")
    def show_accounts_details(self):
        for i in self.account_list:
            print(i)
    def show_specific_account(self,id):
        a =  self.search(id)
        print(a)
    def close_account(self,id):
        a = self.search(id)
        a.close_account()
        print(f"Account Number {a.id} is closed")

milly_bank = Bank('milliy bank')
def print_menu():
    print("\nBank Account Management Menu:")
    print("1. Add an account")
    print("2. List all accounts")
    print("3. deposit money")
    print("4. withdraw money")
    print("5. Account details")
    print("6. Exit")
while True:
    print_menu()
    command = input("Enter a number: ")
    if command == '1':
        milly_bank.add_account()
    elif command == '2':
        milly_bank.show_accounts_details()
    elif command == '3':
        account_number = int(input("Enter account Number: "))
        milly_bank.deposit_account(account_number)
    elif command == '4':
        account_number = int(input("Enter account Number: "))
        milly_bank.withdraw_account(account_number)
    elif command == '5':
        account_number = int(input("Enter account Number: "))
        milly_bank.show_specific_account(account_number)
    else:
        exit()


