class Deque:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return True if len(self.queue) == 0 else False

    def add_first(self, item):
        self.queue.insert(0, item)
        return self
    def remove_first(self):
        return None if not self.queue else self.queue.pop(0)
    def add_last(self, item):
        self.queue.append(item)
        return self
    
    def remove_last(self):
        if self.queue:
            return self.queue.pop()

       
queue = Deque()
while True:
    print("===== Deque Class ========")
    print("1. Add First")
    print("2. Add Last")
    print("3. Remove First")
    print("4. Remove Last")
    print("5. Check if Deque is Empty")
    print("6. Display")
    print("7. Exit")
    choice = input("Enter your choice: ")   
    if choice == "1":
        item = input("Enter item to add: ")
        queue.add_first(item)
        print("Item added to the front of the deque: ", item)
    elif choice == "2":
        item = input("Enter item to add: ")
        queue.add_last(item)
        print("Item added to the end of the deque: ", item)
    elif choice == "3":
        item = queue.remove_first()
        if item:
            print("Item removed from the front of the deque: ", item)
    elif choice == "4":
        item = queue.remove_last()
        if item:
            print("Item removed from the end of the deque: ", item)
    elif choice == "5":
        print("Deque is empty: ", queue.is_empty())
    elif choice == "6":
        print("Deque: ", queue.queue)
    elif choice == "7":
        break
    


     
        
    