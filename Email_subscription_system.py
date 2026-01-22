subscribers = []

def add_subscriber():
    email = input("Enter email address: ")
    subscribers.append(email)
    print("Email subscribed successfully")

def view_subscribers():
    if not subscribers:
        print("No subscribers found")
    else:
        for email in subscribers:
            print(email)

def main():
    while True:
        print("1. Add Subscriber")
        print("2. View Subscribers")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_subscriber()
        elif choice == "2":
            view_subscribers()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
