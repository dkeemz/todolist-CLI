class Todo:
    todolist =[]
    def __init__(self,text):
        self.text = text
        self.todolist.append(self.text)

    def add_to_list(self,data):
        self.data = data
        self.todolist.append(self.data)
    
    def remove_last(self):
        if self.todolist:
            return self.todolist.pop()
        print("Can\'t remove!, there is nothing in your list. \n \n \n")
    
    def show_list(self):
        if len(self.todolist) > 0:
            for i in self.todolist:
                print(i)
        else:        
            print("Nothing in the List")

choice = input("""Select what you want to do:
1. select 'A' if you want to ADD to the list
2. select 'B' if you want to remove the last item of the list
3. select 'C' if you want to show items in the list
4. select 'Q' to quit
    >> """)

newList = Todo("")
while choice.lower() != "q":

    if choice.lower() == 'a':
        entry = input("What do you want to add to the list >> ") 
        newList.add_to_list(entry)

    elif choice.lower() == "b":    
        newList.remove_last()

    elif choice.lower() == "c":
        newList.show_list()

    elif choice.lower() == "q":
        break

    else:
        print ("Please Select from the choices above \n \n \n")
    
    choice