print("your current todos are:") #Used to display your current todos
todos = ["Roblox","Fortnite","Apex"]#Your list of todos
while 1 != 2:#makes the loop go on forever

    print("______________________________________")# used to bar off the lines to give more order
    print(todos) #Prints your current todos
    print("______________________________________")
    q= input("do you want to add one more todo to your todos? Y/N")# used to see if the user wants to add an item to their list
    if q=="Y" or q=="y": #used to make sure the user can put upper and lower case answers
        todos.append(input({"Add your new todo:"}))#asks to add todos if you chose yes
    elif q=="N" or q=="n":#used to make sure the user can put upper and lower case answers
        z=input("do you want to remove one todo from your todos? Y/N")#used to see if the user wants to remove an item form their todo
        if z== "Y" or z=="y": #used to make sure the user can put upper and lower case answers
            todos_removal = (input("Enter the todo you would like to remove:"))#Used if the user chose yes
            del todos[int(todos_removal) - 1]#removes the item the user chose
        else:
            continue# used if the user chose no
