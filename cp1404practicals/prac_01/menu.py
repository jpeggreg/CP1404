
name = input("Enter name: ")
print("(H)ello \n(G)oodbye \n(Q)uit")
choice = str(input("\n>>>").lower())
while choice != 'q':
    if choice == 'h':
        print("Hello " + name)
        print("(H)ello \n(G)oodbye \n(Q)uit")
    elif choice == 'g':
        print("Goodbye " + name)
        print("(H)ello \n(G)oodbye \n(Q)uit")
    else:
        print("Invalid menu choice")
        print("(H)ello \n(G)oodbye \n(Q)uit")
    choice = str(input("\n>>>").lower())
print("Finished")