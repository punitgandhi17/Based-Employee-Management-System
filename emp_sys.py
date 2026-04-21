import pandas as pd
from datetime import datetime 
import os

file_name="Data.xlsx"
user = {"admin": "1234", "user": "0000"}
attempts = 3

if os.path.exists(file_name):
    try:
        df=pd.read_excel(file_name)
        #print("Existing data loaded.")
    except:
        df = pd.DataFrame(columns=['EmpID', 'Name', 'Age','Gender','Department','Salary','Experience_Yrs','performance_Rate','City'])
else:
    df = pd.DataFrame(columns=['EmpID', 'Name', 'Age','Gender','Department','Salary','Experience_Yrs','performance_Rate','City'])


def genId():
    if df.empty:
        return 1
    else:
        return df['EmpID'].max() + 1


while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in user and user[username] == password:
        print("-"*20)
        print("Login Successfully!!")
        print(f"Login Time:{datetime.now().strftime("%H:%M:%S")}")
        print("-"*20)

        is_admin = (username == "admin")

        while True:
            print("\n1:Add\n2:Remove\n3:Search\n4:Display\n5:Save & Exit")
            ch = int(input("Enter choice: "))

            if ch == 1:
                if not is_admin:
                    print("-"*20)
                    print("Access Denied: Admin only.")
                    print("-"*20)
                    continue

                User_id = genId()
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                gender=input("Enter Gender:")
                department=input("Enter Department:")
                salary = float(input("Enter Salary: "))
                exp_yrs=int(input("Enter EperienceYear:"))
                perform_rate=float(input("Enter Performance Rate(out of 5):"))
                city=input("Enetr City:")

            

                df.loc[len(df)] = [User_id, name, age,gender,department,salary,exp_yrs,perform_rate,city]
                
                print("-"*10)
                print("User Added Successfully!!")
                print("-"*10)

            elif ch == 2:
                if not is_admin:
                    print("-"*20)
                    print("Access Denied: Admin only.")
                    print("-"*20)
                    continue

                find_id = int(input("Enter ID: "))
                df.drop(df[df['EmpID'] == find_id].index, inplace=True)
                print("User deleted (if existed).")

            elif ch == 3:
                find_id = int(input("Enter ID: "))
                result = df[df['EmpID'] == find_id]

                print(result if not result.empty else "User not found")

            elif ch == 4:
                if df.empty:
                    print("-"*20)
                    print("No records!!")
                    print("-"*20)
                else:
                    print("\n Data")
                    print("-"*100)
                    print(df)
                    print("-"*100)

            elif ch == 5:
                df.to_excel("Data.xlsx", index=False)
                print("Data Saved. Exiting..")
                exit()

            else:
                print("-"*20)
                print("Invalid choice!")
                print("-"*20)

    else:
        attempts -= 1
        print("-"*20)
        print(f"Invalid login. Attempts left: {attempts}")
        print("-"*20)

print("*"*20)
print("Too many attempts!!!")
print("*"*20)