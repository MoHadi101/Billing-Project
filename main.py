from tkinter import *
import os
from tkinter import messagebox
import random
from tkinter import font
from turtle import clear
import smtplib

#Functionality Part
def clear():
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)
#     billnumberEntry.insert(0, str(billnumber))  # Reset to current bill number
    bathsoapEntry.delete(0, END)
    bathsoapEntry.insert(0, "0")
    facecreamEntry.delete(0, END)
    facecreamEntry.insert(0, "0")
    facewashEntry.delete(0, END)
    facewashEntry.insert(0, "0")
    hairsprayEntry.delete(0, END)
    hairsprayEntry.insert(0, "0")
    hairgelEntry.delete(0, END)
    hairgelEntry.insert(0, "0")
    bodylotionEntry.delete(0, END)
    bodylotionEntry.insert(0, "0")
    riceEntry.delete(0, END)
    riceEntry.insert(0, "0")
    potatoEntry.delete(0, END)
    potatoEntry.insert(0, "0")
    breadEntry.delete(0, END)
    breadEntry.insert(0, "0")
    milkEntry.delete(0, END)
    milkEntry.insert(0, "0")
    tomatoEntry.delete(0, END)
    tomatoEntry.insert(0, "0")
    oilEntry.delete(0, END)
    oilEntry.insert(0, "0")
    cocacolaEntry.delete(0, END)
    cocacolaEntry.insert(0, "0")
    fantaEntry.delete(0, END)
    fantaEntry.insert(0, "0")
    spriteEntry.delete(0, END)
    spriteEntry.insert(0, "0")
    redbullEntry.delete(0, END)
    redbullEntry.insert(0, "0")
    smoothyEntry.delete(0, END)
    smoothyEntry.insert(0, "0")
    cosmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    drinkspriceEntry.delete(0,END)
    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    drinkstaxEntry.delete(0,END)
    textarea.delete(1.0,END)
       

def email_bill():
       def send_gmail():
            try:
              ob=smtplib.SMTP("smtp.gmail.com", 587)
              ob.starttls()
              ob.login(senderEntry.get(), passwordEntry.get())
              message =email_textarea.get(1.0, END)
              reciever_address = recipientEntry.get()
              ob.sendmail(senderEntry.get(), reciever_address, message)
              ob.quit()
              messagebox.showinfo("Success", "Email sent successfully",parent=root1)
              root1.destroy()
            except:
              messagebox.showerror("Error", "Failed to send email. Please check the credentials and try again.", parent=root1)



       if textarea.get(1.0, END).strip() == "":
              messagebox.showerror("Error", "No bill to email")
       else:
             root1=Toplevel()
             root1.grab_set()#not able to click another button in the main window system to stay in the email requriments
             root1.title("Email Bill")
       #       root1.geometry("1000x700")
             root1.config(bg="gray20")
             root1.resizable(False, False)# oder root1.resizable(0, 0)
             

             senderFrame = LabelFrame(root1, text="SENDER",font=("Arial", 16, "bold"), bd=6, bg="gray20", fg="gold")
             senderFrame.grid(row=0, column=0, padx=40, pady=20)

             gmailIdLabel = Label(senderFrame, text="Sender's Email:", font=("Arial", 14, "bold"), bg="gray20", fg="white")
             gmailIdLabel.grid(row=0, column=0, padx=10, pady=8)

             senderEntry = Entry(senderFrame,font=("Arial", 14, "bold"),bd=3, width=30,relief=RIDGE)
             senderEntry.grid(row=0, column=1, padx=10, pady=8)

             passwordLabel = Label(senderFrame, text="Sender's Password:", font=("Arial", 14, "bold"), bg="gray20", fg="white")
             passwordLabel.grid(row=1, column=0, padx=10, pady=8)

             passwordEntry = Entry(senderFrame,font=("Arial", 14, "bold"),bd=3, width=30,relief=RIDGE, show="*")
             passwordEntry.grid(row=1, column=1, padx=10, pady=8)


             recipientFrame = LabelFrame(root1, text="RECIPIENT",font=("Arial", 16, "bold"), bd=6, bg="gray20", fg="gold")
             recipientFrame.grid(row=1, column=0, padx=40, pady=20)

             recieverLabel = Label(recipientFrame, text="Recipient's Email:", font=("Arial", 14, "bold"), bg="gray20", fg="white")
             recieverLabel.grid(row=0, column=0, padx=10, pady=8)
             
             recipientEntry = Entry(recipientFrame,font=("Arial", 14, "bold"),bd=3, width=30,relief=RIDGE)
             recipientEntry.grid(row=0, column=1, padx=10, pady=8)

             messageLabel = Label(recipientFrame, text="Message:", font=("Arial", 14, "bold"), bg="gray20", fg="white")
             messageLabel.grid(row=1, column=0, padx=10, pady=8)

             email_textarea = Text(recipientFrame, font=("Arial", 14, "bold"), width=42, height=11, bd=3, relief=SUNKEN)
             email_textarea.grid(row=2, column=0, columnspan=2, padx=10, pady=8)
             email_textarea.delete(1.0, END)  # Clear previous content
             email_textarea.insert(END, textarea.get(1.0, END).replace("=", "").replace("-", "").replace("\t\t\t", "\t"))  # Insert bill content into the email textarea

             sendButton = Button(root1, text="SEND", font=("Arial", 16, "bold"), bd=3, width=15, pady=10,command=send_gmail)
             sendButton.grid(row=2, column=0, columnspan=2, pady=20)

             root1.mainloop()

def print_bill():
     if textarea.get(1.0, END).strip() == "":
          messagebox.showerror("Error", "No bill to print")
     else:
          bill_content = textarea.get(1.0, END)
          with open("temp_bill.txt", "w") as f:
               f.write(bill_content)
          os.startfile("temp_bill.txt", "print")

# def search_bill():
#       for i in os.listdir("bills/"):
#         if i.split(".")[0] == billnumberEntry.get():
#               f=open(f"bills/{i}", "r")
#               textarea.delete(1.0, END)
#               for data in f:
#                        textarea.insert(END, data)
#               f.close()
#               break
#         else:
#               messagebox.showerror("Error", "Invalid Bill Number")
def search_bill():
    bill_num = billnumberEntry.get().strip()  # Leerzeichen entfernen
    if not bill_num:
        messagebox.showerror("Error", "Please enter a bill number")
        return

    if not os.path.exists("bills"):
        messagebox.showerror("Error", "No bills found. Please save a bill first.")
        return

    found = False
    for filename in os.listdir("bills"):
        if filename.endswith(".txt") and filename.split(".")[0] == bill_num:
            with open(f"bills/{filename}", "r") as f:
                textarea.delete(1.0, END)
                textarea.insert(END, f.read())
            found = True
            break

    if not found:
        messagebox.showerror("Error", "Invalid Bill Number")
            


def save_bill():
    global billnumber
    result = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
    if result:
          bill_content = textarea.get(1.0, END)
          if not os.path.exists("bills"):
              os.makedirs("bills")
          file=open(f"bills/{billnumber}.txt", "w")
          file.write(bill_content)
          file.close()
          messagebox.showinfo("Saved", f"Bill saved as {billnumber}.txt")
          billnumber = random.randint(500, 1000)# Generate a new bill number for the next bill  

billnumber = random.randint(500, 1000)
def total():
    global soapprice,facecreamprice, facewashprice, hairsprayprice, hairgelprice, bodylotionprice, riceprice, potatoprice, breadprice, milkprice, tomatoprice, oilprice, cocacolaprice, fantaprice, spriteprice, redbullprice, smoothyprice, pepsiprice
    # Calculate total price for cosmetics
    soapprice = int(bathsoapEntry.get()) * 20 #20 ist der Preis pro Einheit
    facecreamprice = int(facecreamEntry.get()) * 50
    facewashprice = int(facewashEntry.get()) * 100
    hairsprayprice = int(hairsprayEntry.get()) * 150
    hairgelprice = int(hairgelEntry.get()) * 80
    bodylotionprice = int(bodylotionEntry.get()) * 60

    totalcosmeticprice = soapprice + facecreamprice + facewashprice + hairsprayprice + hairgelprice + bodylotionprice
    cosmeticpriceEntry.delete(0, END)  # Clear previous value
    cosmeticpriceEntry.insert(0, f"{totalcosmeticprice} EUR")

    #tax calculation for cosmetics

    cosmetictax = totalcosmeticprice * 0.1  # Assuming 10% tax
    cosmetictaxEntry.delete(0, END)
    cosmetictaxEntry.insert(0, f"{cosmetictax} EUR")

    # Calculate total price for grocery
    riceprice = int(riceEntry.get()) * 30
    potatoprice = int(potatoEntry.get()) * 20
    breadprice = int(breadEntry.get()) * 25
    milkprice = int(milkEntry.get()) * 15
    tomatoprice = int(tomatoEntry.get()) * 10
    oilprice = int(oilEntry.get()) * 50

    totalgroceryprice = riceprice + potatoprice + breadprice + milkprice + tomatoprice + oilprice 
    grocerypriceEntry.delete(0, END)  # Clear previous value
    grocerypriceEntry.insert(0, f"{totalgroceryprice} EUR")

    #tax calculation for grocery

    grocerytax = totalgroceryprice * 0.2  # Assuming 20% tax
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, f"{grocerytax} EUR")

    # Calculate total price for cold drinks
    cocacolaprice = int(cocacolaEntry.get()) * 20
    fantaprice = int(fantaEntry.get()) * 20
    spriteprice = int(spriteEntry.get()) * 20
    redbullprice = int(redbullEntry.get()) * 20
    smoothyprice = int(smoothyEntry.get()) * 20
    pepsiprice = int(pepsiEntry.get()) * 20
    totalcolddrinksprice = cocacolaprice + fantaprice + spriteprice + redbullprice + smoothyprice + pepsiprice
    drinkspriceEntry.delete(0, END)  # Clear previous value
    drinkspriceEntry.insert(0, f"{totalcolddrinksprice} EUR")

    #tax calculation for cold drinks

    drinkstax = totalcolddrinksprice * 0.4  # Assuming 40% tax
    drinkstaxEntry.delete(0, END)
    drinkstaxEntry.insert(0, f"{drinkstax} EUR")
    # Calculate total bill
    global totalbill
    totalbill = totalcosmeticprice + totalgroceryprice + totalcolddrinksprice + cosmetictax + grocerytax + drinkstax
    # ---------------------------------------------
def bill_area():
        if nameEntry.get() == "" or phoneEntry.get() == "":
            messagebox.showerror("Error", "Customer details are required")
        elif cosmeticpriceEntry.get() == "" and grocerypriceEntry.get() == "" and drinkspriceEntry.get() == "":
            messagebox.showerror("Error", "No products selected")
        elif cosmeticpriceEntry.get() == "0 EUR" and grocerypriceEntry.get() == "0 EUR" and drinkspriceEntry.get() == "0 EUR":
            messagebox.showerror("Error", "No products selected")
        else:
             textarea.delete(1.0, END)  # Clear previous bill
             textarea.insert(END, f"Welcome to Online/Retail Billing System\n")
             textarea.insert(END, f"\nBill Number: {billnumber}\n")
             textarea.insert(END, f"\nCustomer Name: {nameEntry.get()}\n")
             textarea.insert(END, f"\nPhone Number: {phoneEntry.get()}\n")
             textarea.insert(END, f"\n=======================================")
             textarea.insert(END, f"\nProducts\t\tQty\t\tPrice")
             textarea.insert(END, f"\n=======================================\n")
             if bathsoapEntry.get() != "0":
                 textarea.insert(END, f"Bath Soap\t\t{bathsoapEntry.get()}\t\t{soapprice} EUR\n")
             if hairgelEntry.get() != "0":
                 textarea.insert(END, f"Hair Gel\t\t{hairgelEntry.get()}\t\t{hairgelprice} EUR\n")
             if facecreamEntry.get() != "0":
                 textarea.insert(END, f"Face Cream\t\t{facecreamEntry.get()}\t\t{facecreamprice} EUR\n")
             if facewashEntry.get() != "0":
                 textarea.insert(END, f"Face Wash\t\t{facewashEntry.get()}\t\t{facewashprice} EUR\n")
             if hairsprayEntry.get() != "0":
                 textarea.insert(END, f"Hair Spray\t\t{hairsprayEntry.get()}\t\t{hairsprayprice} EUR\n")
             if bodylotionEntry.get() != "0":
                 textarea.insert(END, f"Body Lotion\t\t{bodylotionEntry.get()}\t\t{bodylotionprice} EUR\n")
                 #=======for grocery
             if riceEntry.get() != "0":
                    textarea.insert(END, f"Rice\t\t{riceEntry.get()}\t\t{riceprice} EUR\n")
             if potatoEntry.get() != "0":
                    textarea.insert(END, f"Potato\t\t{potatoEntry.get()}\t\t{potatoprice} EUR\n")
             if breadEntry.get() != "0":
                    textarea.insert(END, f"Bread\t\t{breadEntry.get()}\t\t{breadprice} EUR\n")
             if milkEntry.get() != "0":
                    textarea.insert(END, f"Milk\t\t{milkEntry.get()}\t\t{milkprice} EUR\n")
             if tomatoEntry.get() != "0":
                    textarea.insert(END, f"Tomato\t\t{tomatoEntry.get()}\t\t{tomatoprice} EUR\n")
             if oilEntry.get() != "0":
                    textarea.insert(END, f"Oil\t\t{oilEntry.get()}\t\t{oilprice} EUR\n")
                    #=======for cold drinks
             if cocacolaEntry.get() != "0":
                    textarea.insert(END, f"Coke\t\t{cocacolaEntry.get()}\t\t{cocacolaprice} EUR\n")
             if pepsiEntry.get() != "0":
                    textarea.insert(END, f"Pepsi\t\t{pepsiEntry.get()}\t\t{pepsiprice} EUR\n")
             if spriteEntry.get() != "0":
                    textarea.insert(END, f"Sprite\t\t{spriteEntry.get()}\t\t{spriteprice} EUR\n")
             if fantaEntry.get() != "0":
                    textarea.insert(END, f"Fanta\t\t{fantaEntry.get()}\t\t{fantaprice} EUR\n")
             if redbullEntry.get() != "0":
                    textarea.insert(END, f"Red Bull\t\t{redbullEntry.get()}\t\t{redbullprice} EUR\n")
             if smoothyEntry.get() != "0":
                    textarea.insert(END, f"Smoothy\t\t{smoothyEntry.get()}\t\t{smoothyprice} EUR\n")
             textarea.insert(END, f"\n-----------------------------------------------------------------------")

             if cosmetictaxEntry.get() != "0 EUR":
                textarea.insert(END, f"\nCosmetic Tax\t\t\t\t{cosmetictaxEntry.get()}")
             if grocerytaxEntry.get() != "0 EUR":
                    textarea.insert(END, f"\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}")
             if drinkstaxEntry.get() != "0 EUR":
                    textarea.insert(END, f"\nCold Drinks Tax\t\t\t\t{drinkstaxEntry.get()}")
        textarea.insert(END,f"\n\nTotal Bill \t\t\t\t{totalbill} EUR")
        textarea.insert(END, f"\n-----------------------------------------------------------------------")
        save_bill()

# GUI Part
root = Tk()
root.title("Online/Retail Billing System")
root.geometry("1270x685")
# root.iconbitmap("icon.ico")
import sys
if getattr(sys, 'frozen', False):
    # Wenn wir als .exe laufen, ist das Icon im gleichen Ordner wie die .exe
    base_path = os.path.dirname(sys.executable)
else:
    # Im Entwicklungsmodus: das Icon liegt neben main.py
    base_path = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_path, "icon.ico")
root.iconbitmap(icon_path)

headingLabel = Label(root, text="Online/Retail Billing System", font=("Arial", 30, "bold"), bg="gray20", fg="gold", bd=5, relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame = LabelFrame(root, text="Customer Details", font=("Arial", 15, "bold"), bd=5, relief=GROOVE, fg="gold", bg="gray20")
customer_details_frame.pack(fill=X)   # kein Abstand

nameLabel = Label(customer_details_frame, text="Name:", font=("Arial", 15, "bold"), bg="gray20", fg="white")
nameLabel.grid(row=0, column=0, padx=20)

nameEntry = Entry(customer_details_frame, font=("Arial", 15, "bold"), bd=3, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel = Label(customer_details_frame, text="Phone Number:", font=("Arial", 15, "bold"), bg="gray20", fg="white")
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customer_details_frame, font=("Arial", 15, "bold"), bd=3, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

billnumberLabel = Label(customer_details_frame, text="Bill Number:", font=("Arial", 15, "bold"), bg="gray20", fg="white")
billnumberLabel.grid(row=0, column=4, padx=20, pady=2)

billnumberEntry = Entry(customer_details_frame, font=("Arial", 15, "bold"), bd=3, width=18)
billnumberEntry.grid(row=0, column=5, padx=8)
# billnumberEntry.insert(0, str(billnumber))  # Insert default bill number

searchButton = Button(customer_details_frame, text="SEARCH", font=("Arial", 12, "bold"), bg="gray20", fg="gold", bd=5, relief=RAISED, width=10,command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

# ----------------------------------------------------------------------------
productFrame = Frame(root)
productFrame.pack(fill=BOTH)   # expand=True entfernt – keine Höhendehnung mehr

productFrame.grid_columnconfigure(0, weight=1)
productFrame.grid_columnconfigure(1, weight=1)
productFrame.grid_columnconfigure(2, weight=1)
productFrame.grid_columnconfigure(3, weight=1)

cosmeticsFrame = LabelFrame(productFrame, text="Cosmetics", font=("Arial", 15, "bold"), bd=5, relief=GROOVE, fg="gold", bg="gray20")
cosmeticsFrame.grid(row=0, column=0, sticky="nsew")

# ---
bathsoapLabel = Label(cosmeticsFrame, text="Bath Soap", font=("Arial", 15, "bold"), bg="gray20", fg="white")
bathsoapLabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")

bathsoapEntry = Entry(cosmeticsFrame, font=("Arial", 15, "bold"), bd=3, width=10)
bathsoapEntry.grid(row=0, column=1, pady=9, padx=10)
bathsoapEntry.insert(0, "0")  # Default value

facecreamLabel = Label(cosmeticsFrame, text="Face Cream", font=("Arial", 15, "bold"), bg="gray20", fg="white")
facecreamLabel.grid(row=1, column=0, pady=9, padx=10, sticky="w")

facecreamEntry = Entry(cosmeticsFrame, font=("Arial", 15, "bold"), bd=3, width=10)
facecreamEntry.grid(row=1, column=1, pady=9, padx=10)
facecreamEntry.insert(0, "0")  # Default value

facewashLabel = Label(cosmeticsFrame, text="Face Wash", font=("Arial", 15, "bold"), bg="gray20", fg="white")
facewashLabel.grid(row=2, column=0, pady=9, padx=10, sticky="w")

facewashEntry = Entry(cosmeticsFrame, font=("Arial", 15, "bold"), bd=3, width=10)
facewashEntry.grid(row=2, column=1, pady=9, padx=10)
facewashEntry.insert(0, "0")  # Default value

hairsprayLabel = Label(cosmeticsFrame, text="Hairspray", font=("Arial", 15, "bold"), bg="gray20", fg="white")
hairsprayLabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")

hairsprayEntry = Entry(cosmeticsFrame, font=("Arial", 15, "bold"), bd=3, width=10)
hairsprayEntry.grid(row=3, column=1, pady=9, padx=10)
hairsprayEntry.insert(0, "0")  # Default value

hairgelLabel = Label(cosmeticsFrame, text="Hair Gel", font=("Arial", 15, "bold"), bg="gray20", fg="white")
hairgelLabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")

hairgelEntry = Entry(cosmeticsFrame, font=("Arial", 15, "bold"), bd=3, width=10)
hairgelEntry.grid(row=4, column=1, pady=9, padx=10)
hairgelEntry.insert(0, "0")  # Default value

bodylotionLabel = Label(cosmeticsFrame, text="Body Lotion", font=("Arial", 15, "bold"), bg="gray20", fg="white")
bodylotionLabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")

bodylotionEntry = Entry(cosmeticsFrame, font=("Arial", 15, "bold"), bd=3, width=10)
bodylotionEntry.grid(row=5, column=1, pady=9, padx=10)
bodylotionEntry.insert(0, "0")  # Default value

# ------------------------------------
groceryFrame = LabelFrame(productFrame, text="Grocery", font=("Arial", 15, "bold"), bd=5, relief=GROOVE, fg="gold", bg="gray20")
groceryFrame.grid(row=0, column=1, sticky="nsew")

# -----
riceLabel = Label(groceryFrame, text="Rice", font=("Arial", 15, "bold"), bg="gray20", fg="white")
riceLabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")


riceEntry = Entry(groceryFrame, font=("Arial", 15, "bold"), bd=3, width=10)
riceEntry.grid(row=0, column=1, pady=9, padx=10)
riceEntry.insert(0, "0")  # Default value

potatoLabel = Label(groceryFrame, text="Potato", font=("Arial", 15, "bold"), bg="gray20", fg="white")
potatoLabel.grid(row=1, column=0, pady=9, padx=10, sticky="w")

potatoEntry = Entry(groceryFrame, font=("Arial", 15, "bold"), bd=3, width=10)
potatoEntry.grid(row=1, column=1, pady=9, padx=10)
potatoEntry.insert(0, "0")  # Default value

breadLabel = Label(groceryFrame, text="Bread", font=("Arial", 15, "bold"), bg="gray20", fg="white")
breadLabel.grid(row=2, column=0, pady=9, padx=10, sticky="w")

breadEntry = Entry(groceryFrame, font=("Arial", 15, "bold"), bd=3, width=10)
breadEntry.grid(row=2, column=1, pady=9, padx=10)
breadEntry.insert(0, "0")  # Default value

milkLabel = Label(groceryFrame, text="Milk", font=("Arial", 15, "bold"), bg="gray20", fg="white")
milkLabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")

milkEntry = Entry(groceryFrame, font=("Arial", 15, "bold"), bd=3, width=10)
milkEntry.grid(row=3, column=1, pady=9, padx=10)
milkEntry.insert(0, "0")  # Default value

tomatoLabel = Label(groceryFrame, text="Tomato", font=("Arial", 15, "bold"), bg="gray20", fg="white")
tomatoLabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")

tomatoEntry = Entry(groceryFrame, font=("Arial", 15, "bold"), bd=3, width=10)
tomatoEntry.grid(row=4, column=1, pady=9, padx=10)
tomatoEntry.insert(0, "0")  # Default value

oilLabel = Label(groceryFrame, text="Oil", font=("Arial", 15, "bold"), bg="gray20", fg="white")
oilLabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")

oilEntry = Entry(groceryFrame, font=("Arial", 15, "bold"), bd=3, width=10)
oilEntry.grid(row=5, column=1, pady=9, padx=10)
oilEntry.insert(0, "0")  # Default value

# ----------------------------------------------
drinksFrame = LabelFrame(productFrame, text="Cold Drinks", font=("Arial", 15, "bold"), bd=5, relief=GROOVE, fg="gold", bg="gray20")
drinksFrame.grid(row=0, column=2, sticky="nsew")

# ---------------
cocacolaLabel = Label(drinksFrame, text="Coca Cola", font=("Arial", 15, "bold"), bg="gray20", fg="white")
cocacolaLabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")

cocacolaEntry = Entry(drinksFrame, font=("Arial", 15, "bold"), bd=3, width=10)
cocacolaEntry.grid(row=0, column=1, pady=9, padx=10)
cocacolaEntry.insert(0, "0")  # Default value
fantaLabel = Label(drinksFrame, text="Fanta", font=("Arial", 15, "bold"), bg="gray20", fg="white")
fantaLabel.grid(row=1, column=0, pady=9, padx=10, sticky="w")

fantaEntry = Entry(drinksFrame, font=("Arial", 15, "bold"), bd=3, width=10)
fantaEntry.grid(row=1, column=1, pady=9, padx=10)
fantaEntry.insert(0, "0")  # Default value

spriteLabel = Label(drinksFrame, text="Sprite", font=("Arial", 15, "bold"), bg="gray20", fg="white")
spriteLabel.grid(row=2, column=0, pady=9, padx=10, sticky="w")

spriteEntry = Entry(drinksFrame, font=("Arial", 15, "bold"), bd=3, width=10)
spriteEntry.grid(row=2, column=1, pady=9, padx=10)
spriteEntry.insert(0, "0")  # Default value

redbullLabel = Label(drinksFrame, text="Red Bull", font=("Arial", 15, "bold"), bg="gray20", fg="white")
redbullLabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")

redbullEntry = Entry(drinksFrame, font=("Arial", 15, "bold"), bd=3, width=10)
redbullEntry.grid(row=3, column=1, pady=9, padx=10)
redbullEntry.insert(0, "0")  # Default value

smoothyLabel = Label(drinksFrame, text="Smoothy", font=("Arial", 15, "bold"), bg="gray20", fg="white")
smoothyLabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")

smoothyEntry = Entry(drinksFrame, font=("Arial", 15, "bold"), bd=3, width=10)
smoothyEntry.grid(row=4, column=1, pady=9, padx=10)
smoothyEntry.insert(0, "0")  # Default value

pepsiLabel = Label(drinksFrame, text="Pepsi", font=("Arial", 15, "bold"), bg="gray20", fg="white")
pepsiLabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")

pepsiEntry = Entry(drinksFrame, font=("Arial", 15, "bold"), bd=3, width=10)
pepsiEntry.grid(row=5, column=1, pady=9, padx=10)
pepsiEntry.insert(0, "0")  # Default value

# ---------------------------------------------------
billframe = Frame(productFrame, bd=5, relief=GROOVE, bg="gray20")
billframe.grid(row=0, column=3, sticky="nsew")

billareaLabel = Label(billframe, text="Bill Area", font=("Arial", 15, "bold"), bg="gray20", fg="white", bd=5, relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billframe, font=("Arial"), width=50, height=18, yscrollcommand=scrollbar.set)
textarea.pack(fill=BOTH, expand=True)
scrollbar.config(command=textarea.yview)

# ------------------------------------------------
billmenuFrame = LabelFrame(root, text="Bill Menu", font=("Arial", 15, "bold"), bd=5, relief=GROOVE, fg="gold", bg="gray20")
billmenuFrame.pack(fill=X)   # kein Abstand

#----------------
cosmeticpriceLabel = Label(billmenuFrame, text="Cosmetic Price", font=("Arial", 14, "bold"), bg="gray20", fg="white")
cosmeticpriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky="w")

cosmeticpriceEntry = Entry(billmenuFrame, font=("Arial", 14, "bold"), bd=3, width=10)
cosmeticpriceEntry.grid(row=0, column=1, pady=6, padx=10)

grocerypriceLabel = Label(billmenuFrame, text="Grocery Price", font=("Arial", 14, "bold"), bg="gray20", fg="white")
grocerypriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky="w")

grocerypriceEntry = Entry(billmenuFrame, font=("Arial", 14, "bold"), bd=3, width=10)
grocerypriceEntry.grid(row=1, column=1, pady=6, padx=10)

drinkspriceLabel = Label(billmenuFrame, text="Cold Drinks Price", font=("Arial", 14, "bold"), bg="gray20", fg="white")
drinkspriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky="w")

drinkspriceEntry = Entry(billmenuFrame, font=("Arial", 14, "bold"), bd=3, width=10)
drinkspriceEntry.grid(row=2, column=1, pady=6, padx=10)

#----------------
cosmetictaxLabel = Label(billmenuFrame, text="Cosmetic Tax", font=("Arial", 14, "bold"), bg="gray20", fg="white")
cosmetictaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky="w")

cosmetictaxEntry = Entry(billmenuFrame, font=("Arial", 14, "bold"), bd=3, width=10)
cosmetictaxEntry.grid(row=0, column=3, pady=6, padx=10)

grocerytaxLabel = Label(billmenuFrame, text="Grocery Tax", font=("Arial", 14, "bold"), bg="gray20", fg="white")
grocerytaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky="w")

grocerytaxEntry = Entry(billmenuFrame, font=("Arial", 14, "bold"), bd=3, width=10)
grocerytaxEntry.grid(row=1, column=3, pady=6, padx=10)

drinkstaxLabel = Label(billmenuFrame, text="Cold Drinks Tax", font=("Arial", 14, "bold"), bg="gray20", fg="white")
drinkstaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky="w")

drinkstaxEntry = Entry(billmenuFrame, font=("Arial", 14, "bold"), bd=3, width=10)
drinkstaxEntry.grid(row=2, column=3, pady=6, padx=10)

buttonFrame = Frame(billmenuFrame, bd=5, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3, sticky="nsew")

totalButton = Button(buttonFrame, text="TOTAL", font=("Arial", 16, "bold"), bg="gray20", fg="white", bd=3, width=8, pady=10, command=total)
totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton = Button(buttonFrame, text="BILL", font=("Arial", 16, "bold"), bg="gray20", fg="white", bd=3, width=8, pady=10, command=bill_area)
billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton = Button(buttonFrame, text="EMAIL", font=("Arial", 16, "bold"), bg="gray20", fg="white", bd=3, width=8, pady=10, command=email_bill)
emailButton.grid(row=0, column=2, pady=20, padx=5)

printButton = Button(buttonFrame, text="PRINT", font=("Arial", 16, "bold"), bg="gray20", fg="white", bd=3, width=8, pady=10, command=print_bill)
printButton.grid(row=0, column=3, pady=20, padx=5)

clearButton = Button(buttonFrame, text="CLEAR", font=("Arial", 16, "bold"), bg="gray20", fg="white", bd=3, width=8, pady=10, command=clear)
clearButton.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()