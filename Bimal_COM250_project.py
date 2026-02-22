'''
Author: Bimal Kumal
Company: Best Buy

This program simulates the daily sales operations of a Best Buy store by tracking the daily sales summary of each department and generating the report of daily sales.
This program allows the users to enter the daily sales summary,display the records,process the order and save the record to a text file.
Best Buy is a large electronic retailer and well known for its wide range of electronic devices and essential home appliance.
I chose this company because I often go there to buy electronic devices and its business model aligns well with a sales-tracking system.
The company also offers Geek Squad Protection plans which check the condition of each returned items or pre-owned items. 

'''

# Created function to save the record into a file
# it will take data as an argument and appends it to the CompanyReport.txt
# open the file in a append mode to ensure all records are saved permanently
# We can reuse it multiple time 
def save_to_record(data):
    rec=open("CompanyReport.txt","a")
    rec.write(data+"\n")
    rec.close()

# Function to enter the sales of each department 
# only four categories of items can be entered in this case

def enter_sales_by_dept():
    print("----Please Enter the today's sales from each department---")
    date=input("Enter the today's date: ")

# This will ensure that user enter the sales in a correct format instead of crashing
# This will validate the numeric input
    while True: 
        try:
            CS_transaction=int(input("Enter the number of transaction for Laptops & Desktops:"))
            CS_sales=float(input("Enter the Sales for Laptops & Desktops: $"))
            Phone_transaction=int(input("Enter the number of transaction for Cell Phones & Accessories :"))
            Phone_sales=float(input("Enter the Sales for Cell Phones & Accessories : $"))
            TV_transaction=int(input("Enter the number of transaction for TV & Projectors:"))
            TV_sales=float(input("Enter the Sales for TV & Projectors : $"))
            Apple_transaction=int(input("Enter the number of transaction for Apple products:"))
            Apple_sales=float(input("Enter the Sales for Apple Products: $"))
            break # if the input is valid, it will exit loop
        except ValueError:
            print("Error: please enter valid number.")
    print("----------------------------------------------------")        
    print("Sales Data Successfully entered.")
    print("")
    return CS_transaction,CS_sales,Phone_transaction,Phone_sales,TV_transaction,TV_sales, Apple_transaction, Apple_sales,date

# Function to calculate the total sales by adding the sales from each department
# it will take sales values as arguments and calculate the total sales amount and returns it 
def calculate_total_sales(CS_sales,Phone_sales,TV_sales,Apple_sales):
    total_sales_amount=CS_sales+Phone_sales+TV_sales+Apple_sales
    return total_sales_amount

# Function to generate the organized formatted daily sales record using all department sales and total sales
# save the record permanently to the CompanyReport.txt file
def save_sales_report(CS_transaction,CS_sales,Phone_transaction,Phone_sales,TV_transaction,TV_sales, Apple_transaction,Apple_sales,date,total_sales):
    record_1= "sales summary for "+str(date)+"\n"+\
        "-----------------------------\n"+\
            f"No of Transaction for Laptops & Desktops:{CS_transaction}"+"\n"+"Total sales(Laptops & Desktops): ${:.2f}".format(CS_sales)+"\n"+\
                f"No of Transaction for Cell Phone & Accessories:{Phone_transaction}"+"\n"+"Total sales(Cell Phone & Accessories): ${:.2f}".format(Phone_sales)+"\n"+\
                    f"No of Transaction for TV & Projectors:{TV_transaction}"+"\n"+"Total sales(TV & Projectors): ${:.2f}".format(TV_sales)+"\n"+\
                        f"No of Transaction for Apple Products:{Apple_transaction}"+"\n"+"Total sales(Apple products): ${:.2f}".format(Apple_sales)+"\n"+\
                            "-----------------------\n"+\
                                "The total sales :${:.2f}".format(total_sales)+"\n"
    save_to_record(record_1)
    print("record saved successfully to CompanyReport.txt")


def display_sales_report(CS_transaction,CS_sales,Phone_transaction,Phone_sales,TV_transaction,TV_sales,Apple_transaction,Apple_sales):
    print("")
    print("--------------DAILY SALES REPORT ----------------")
    print("The number of transaction for Laptop & Desktops :",CS_transaction, "\nThe total sales(Laptop & Desktops): $%.2f"%CS_sales)
    print("The number of transaction for Cell Phones & Accessories :",Phone_transaction, "\nThe total sales(Cell Phones & Accessories): $%.2f"%Phone_sales)
    print("The number of transaction for TV & Projectors :",TV_transaction, "\nThe total sales(TV & Projectors): $%.2f"%TV_sales)
    print("The number of transaction for Apple products :",Apple_transaction, "\nThe total sales(Apple Products): $%.2f"%Apple_sales)
    total_sales=calculate_total_sales(CS_sales,Phone_sales,TV_sales,Apple_sales)
    print("The total sales :$%.2f"%total_sales)
    print("-------------------------------------------------")
    print("")

# This function will process the customers order 
# This will allow the user to enter how many items being purchased and use
# loop to control and calculate the sub total amount= item amount * quantity 
# also ask the user if they have membership ID or not 
# if they have membership ID then it will apply the 20% discount and if not it will show total amount during the checkout

def process_order():
    while True:
        try:
            no_of_items=int(input("Enter the number of items being purchase?")) # Asking the user how many items are being purchased
            if no_of_items<=0:
                print("Number of items must be at least 1")
                continue
            else:
                break
        except ValueError:
            print("Invalid number.Please enter a whole number")

    sub_total_amount=0 # initialize the sub total amount to store the value 
    # using for loop to process each item one by one 
    for i in range(1,no_of_items+1):
        while True:
            try:
                item_amount=float(input("Enter the amount of an item:")) # Getting the amount of an item
                if item_amount<0:
                    print("Item price can not be negative!!")
                    continue
                else:     
                    break
            except:
                print("Invalid price. Enter a number.")
        while True:
            try: 
                quantity=int(input("Enter the quantity of an item:")) # Getting the quantity 
                if quantity<=0:
                    print("Quantity must be greater than 0.")
                    continue
                else:
                    break
            except:
                print("Invalid quantity. Please enter a whole number.")
        amount=item_amount*quantity # Calculating the total cost and
        sub_total_amount+=amount # adding it to the subtotal
    membership_status=input("Do you have membership ID?. Enter YES or NO: ") # Asking if they have membership ID or not
    # If they have membership ID then 20 % discount will be applied to the subtotal amount
    if membership_status.lower()=="yes": 
        DIS_RATE=0.20 # Black Friday Deal ; could be change later 
        discount_amount=DIS_RATE*sub_total_amount
        total_amount=(sub_total_amount)-discount_amount # Calculating the total amount after applying 20% discount
        print("-------------------------------------------")
        print("You are eligible for 20 % discount.")
        print(f"Your Subtotal is ${sub_total_amount:.2f}")
        print(f"Your Discount amount is ${discount_amount:.2f}")
        print(f"Your total amount after discount is ${total_amount:.2f}")
        # The Checkout Summary will be saved to the Record.txt file
        record_2 = (
            "---- Checkout Summary ----\n"
            f"No of items purchased: {no_of_items}\n"
            f"Subtotal: ${sub_total_amount:.2f}\n"
            f"Discount Applied: ${discount_amount:.2f}\n"
            f"Total After Discount: ${total_amount:.2f}\n"
            "------------------------------\n"
        )
        save_to_record(record_2)

        print("checkout summary successfully saved to the CompanyReport.txt ")
        print("--------------------------------------------\n")
    else: # If they do not have membership ID. then it will show the same subtotal amount without any discount
        print("----------------------------------------")
        print("You are not eligible for a discount.")
        print("Your total amount is ",sub_total_amount)
        # The Checkout Summary will be saved to the CompanyReport.txt file
        record_3 = (
            "---- Checkout Summary ----\n"
            f"No of items purchased: {no_of_items}\n"
            f"Subtotal: ${sub_total_amount:.2f}\n"
            "Discount Applied: None\n"
            f"Final Total: ${sub_total_amount:.2f}\n"
            "------------------------------\n"
        )

        save_to_record(record_3)
        print("checkout summary successfully saved to the CompanyReport.txt ")
        print("----------------------------------------\n")

#  Function to show the menu options to the user to perform the specific tasks
def menu():
    print("Welcome to the Best Buy Data Management System ")
    print("Enter 1 to enter Sales by each department ")
    print("Enter 2 to display the sales report")
    print("Enter 3 to save the sales record")
    print("Enter 4 to process order ") 
    print("Enter 5 to exit the program ")

# Main function to control the overal structure of the data management system
def main():
    sales_data_entered=False # no data at the beginning 
    go=True
    while go==True:
        menu() # Calling the menu function to show the menu options to the user 
     # Validation check to make sure user input the valid input    
        try:
            choice=int(input("Enter your choice :")) # Getting the user's choice
            if choice==1:
                CS_transaction,CS_sales,Phone_transaction,Phone_sales,TV_transaction,TV_sales, Apple_transaction,Apple_sales,date=enter_sales_by_dept()
                sales_data_entered=True # Sales data successfully entered into the record 

            elif choice==2:
                if sales_data_entered==False: # if the user input 2 before 1. this will show user no data message
                    print("No Data Found to Display !!!")
                    print("Please Enter the Sales data first ")
                else: 
                    # Calling this function to display the sales report to the user
                    display_sales_report(CS_transaction,CS_sales,Phone_transaction,Phone_sales,TV_transaction,TV_sales,Apple_transaction,Apple_sales)
            elif choice==3:
                if sales_data_entered==False: # same like above if user type choice=4 before 1 then it will show can not be saved and no data found
                    print("Cannot be Saved !!")
                    print("No Data Found !!!")
                    print("Please Enter the Sales data first ")
                else:
                    total_sales=calculate_total_sales(CS_sales,Phone_sales,TV_sales,Apple_sales) # Calling the calculate_total_sales function to calculate the sales and assigning the value to total_sales for future 
                    save_sales_report(CS_transaction,CS_sales,Phone_transaction,Phone_sales,TV_transaction,TV_sales, Apple_transaction,Apple_sales,date,total_sales) # Calling this function to generate the orginzed repord of our daily sales summary of each department and total sales               
            elif choice==4:
                # Calling the process order. 
                process_order()       
            elif choice==5: # This choice will exit the program and show following message to the user
                print("Thank you ! have a good day ")
                go=False # to keep asking the user to perform other tasl until user's choice is 5
            else:
                print("Invalid choice !!!") # if user type any other integer , it will show invalid message
        except ValueError:
            print("Error: choice must be an integer")
main() # Calling the main function to run the program

