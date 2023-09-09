
class Todo: 
    def __init__(self) -> None:
       self.tasklist = []     


    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"{self.tasklist}"
    
    __repr__ = __str__

    def maketodolist(self): 
        num =int(input("how many tasks do you want?: "))    
        count =1
        while count<=num:
            task = str(input("Task: "))
            self.tasklist += [task]
            count += 1
        return self.tasklist[0:]
    
    def addtask(self, task):
        self.tasklist.append(task)
    
    def deletetask(self, task):
        del self.tasklist[task]
        return self.tasklist[0:]
    
    def viewtask(self):
        count = 0
        while count<= len(self.tasklist):
            count += 1 
            print(count, self.tasklist[count])



Shouvik = Todo()

print(Shouvik.maketodolist())
Shouvik.deletetask("shower")
print(Shouvik.viewtask())