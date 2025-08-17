import tkinter as tk 
from tkinter import messagebox, simpledialog 
import os

class ATMApp: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("ATM System") 
        self.root.geometry("400x400")
        self.accounts = {}
        self.name = ""
        self.load_accounts()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
        self.show_welcome()

    def load_accounts(self):
        try:
            with open("ATM2.txt", "r") as file:
                for line in file:
                    name, balance = line.strip().split(',')
                    self.accounts[name] = int(balance)
        except FileNotFoundError:
            self.accounts = {}
            self.save_accounts()

    def save_accounts(self):
        with open("ATM2.txt", "w") as file:
            for name, balance in self.accounts.items():
                file.write(f"{name},{balance}\n")

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_welcome(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Welcome to the ATM System!", font=("Arial", 16), fg="black").pack(pady=20)
        tk.Button(self.main_frame, text="Proceed", command=self.show_main_menu, width=20, bg="white", fg="black", activebackground="black", activeforeground="white").pack(pady=10)

    def show_main_menu(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Main Menu", font=("Arial", 14), fg="black").pack(pady=10)
        tk.Button(self.main_frame, text="Create New Account", command=self.create_account, width=25, bg="white", fg="black", activebackground="black", activeforeground="white").pack(pady=5)
        tk.Button(self.main_frame, text="Select Existing Account", command=self.select_account, width=25, bg="white", fg="black", activebackground="black", activeforeground="white").pack(pady=5)
        tk.Button(self.main_frame, text="Show All Accounts", command=self.show_all_accounts, width=25, bg="white", fg="black", activebackground="black", activeforeground="white").pack(pady=5)
        tk.Button(self.main_frame, text="Exit", command=self.root.quit, width=25, bg="white", fg="black", activebackground="black", activeforeground="white").pack(pady=20)

    def show_account_menu(self):
        self.clear_frame()
        tk.Label(self.main_frame, text=f"Welcome, {self.name}", font=("Arial", 14), fg="black").pack(pady=10)
        tk.Label(self.main_frame, text=f"Current Balance: {self.accounts[self.name]}", font=("Arial", 12), fg="black").pack(pady=5)
        tk.Button(self.main_frame, text="Deposit", command=self.deposit, width=25, bg="white", fg="black", activebackground="black", activeforeground="white").pack(pady=5)
        tk.Button(self.main_frame, text="Withdraw", command=self.withdraw, width=25, bg="white", fg="black", activebackground="black", activeforeground="white").pack(pady=5)
        tk.Button(self.main_frame, text="Check Account Detail", command=self.show_account_detail, width=25, bg="white", fg="black", activebackground="black", activeforeground="white").pack(pady=5)
        tk.Button(self.main_frame, text="Back to Main Menu", command=self.show_main_menu, width=25, bg="white", fg="black", activebackground="black", activeforeground="white").pack(pady=10)

    def create_account(self):
        self.name = simpledialog.askstring("New Account", "Enter New Account Name: ")
        if not self.name:
            return
        if self.name in self.accounts:
            messagebox.showerror("Exists", f"Account '{self.name}' already exists.")
        else:
            self.accounts[self.name] = 0
            self.save_accounts()
            messagebox.showinfo("Success", f"Account '{self.name}' created successfully!")
            self.show_account_menu()

    def deposit(self):
        try:
            amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:")
            if amount is None or amount <= 0:
                return
            self.accounts[self.name] += amount
            self.save_accounts()
            messagebox.showinfo("Deposited", f"{amount} deposited. New balance: {self.accounts[self.name]}")
        except ValueError:
            messagebox.showerror("Invalid", "Enter a valid number.")

    def withdraw(self):
        try:
            amount = simpledialog.askinteger("Withdraw", "Enter amount to withdraw:")
            if amount is None or amount <= 0:
                return
            if amount > self.accounts[self.name]:
                messagebox.showwarning("Insufficient", "Not enough balance.")
            else:
                self.accounts[self.name] -= amount
                self.save_accounts()
                messagebox.showinfo("Withdrawn", f"{amount} withdrawn. New balance: {self.accounts[self.name]}")
        except ValueError:
            messagebox.showerror("Invalid", "Enter a valid number.")

    def select_account(self):
        self.name = simpledialog.askstring("Select Account", "Enter your account name:")
        if self.name in self.accounts:
            messagebox.showinfo("Success", f"Welcome back, {self.name}!")
            self.show_account_menu()
        else:
            messagebox.showerror("Not Found", "Account not found.")

    def show_account_detail(self):
        if self.name in self.accounts:
            messagebox.showinfo("Account Detail", f"Name: {self.name}\nBalance: {self.accounts[self.name]}")

    def show_all_accounts(self):
        details = "\n".join([f"{name}: {balance}" for name, balance in self.accounts.items()])
        messagebox.showinfo("All Accounts", f"Total Accounts: {len(self.accounts)}\n\n{details}")

# if __name__== "main":
root = tk.Tk() 
app = ATMApp(root) 
root.mainloop()