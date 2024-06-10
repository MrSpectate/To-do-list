def add_task(tasks):
    tasks.append(input("Enter your fucking task : "))

def View_task(tasks):
    if tasks:
        for i,tasks in enumerate(tasks, start = 1):
            print(f"{i}. {tasks}")


def delete_task(tasks):
    View_task(tasks)
    del_num = int(input("Enter a number for deleting a task : "))
    if 1 <= del_num <= len(tasks):
      del_task =  tasks.pop(del_num - 1)
    print(f"Task {del_task } Deleted !")

def main():
    tasks = []
    while True:
        print("\nTo do application\n")
        options = [

              "1. ADD TASK",
              "2. VIEW TASK",
              "3. DELETE TASK",
              "4. EXIT"

  ]
        
        for option in  options:
            print(option)

        
        user = int(input("\nEnter a number for selecting : "))
        
        if user == 1:
            print("\nADD TASK\n")
            add_task(tasks)
        elif user == 2:
            print("\nVIEW TASK\n")
            View_task(tasks)
        elif user == 3:
            print("\nDELETE TASK\n")
            delete_task(tasks)
        elif user == 4:
            print("Good bye !")
            break
        else:
            print("lota sai number dal !")

if __name__ == "__main__":
    main()
