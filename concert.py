
concerts = {
    "Halsey": {"date": "2024-10-01", "location": "New york","tickets": 100},
    "Grinko": {"date": "2024-10-05", "location": "Chicago", "tickets": 150},
    "John mayer": {"date": "2024-10-10", "location": "Los Angles","tickets": 200}
}

def show_concerts():
    print("\nAvailable Concerts:")
    # اینجا دوتا پارامتر داریم اولی رو keyو دومی روvalue در نظر میگیره
    for name, details in concerts.items():
        print(f"{name}: Date: {details["date"]}, Location: {details["location"]}, Tickets Available: {details["tickets"]}")

def reserve_tickets(concert_name, number_of_tickets, user_name):
    if concert_name in concerts:
        if concerts[concert_name]["tickets"] >= number_of_tickets:
            # اینجا تعداد بلیت موردنظر کاربر رو از کل بلیتا کم میکنه
            # کم کردن مقدار سمت راست از متغیر سمت چپ استفاده می‌شود و نتیجه را به همان متغیر سمت چپ اختصاص می‌دهد.
            concerts[concert_name]["tickets"] -= number_of_tickets
            print(f"\nReserved {number_of_tickets} tickets of {concert_name}'s concert for {user_name}: ")
            return True
        else:
            print("Not enough tickets available.")

    else:
        print("Concert not found.")
        

def check_ticket_availability(concert_name):
    if concert_name in concerts:
        return concerts[concert_name]["tickets"]
    else:
        print("Concert not found.")
     

def main():
    user_name=input("Enter your name: ")
    while True:
        show_concerts()
        
        concert_name = input("\nEnter the name of the concert you want to reserve tickets for: ")
        number_of_tickets = int(input("Enter the number of tickets you want to reserve: "))
      
        
        if reserve_tickets(concert_name, number_of_tickets, user_name):
            print(f"Dear {user_name} your reservation for {number_of_tickets} tickets to {concert_name}'s conncert is confirmed. ")
        else:
            print("Reservation failed.")
        
        continue_program = input("\nDo you want to continue (yes/no)? ")
        if continue_program != "yes":
            print("Exiting the program.")
            break
main()
