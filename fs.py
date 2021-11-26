class food:

    def __init__(self, type, name, price = 0 ):
        self.type=type
        self.name=name
        self.price = price

class foodstall:

    foods = []
    selectedfoods = []

    def __init__(self, type,name, price ):
        f = food(type,name=name, price = price)
        self.foods.append(f)
    
    def show(self):
        print("********** AVAILBALE ITEMS **********")
        
        pos=0

        for food in self.foods:
            print("********* ", pos, " ******") 
            pos += 1   
            self.display(food)
            
    
    def select(self):
        print("******* SELECT AN FOOD ITEM  ******")
        print("====== HOW MANY ITEMS YOU WANT? ======")
        neededfoods = int(input())

        for i in range(0, neededfoods ):
            print("====== INPUT THE  FOOD ITEM NO ======")
            selectedfoods= int(input())
            print("========== SELECTED  FOOD ITEM =======")
            f = self.getfoodById(selectedfoods - 1)
            self.selectedfoods.append(f)
            print(self.display(f))

    def getfoodById(self, position):
        return self.foods[position]

    def display(self, foods):
        print("Food type: ", foods.type)
        print("Food name : ", foods.name)
        print("Food Price : ", foods.price)

    def selectedfd(self):
        return self.selectedfoods


class cart:

    fd = []
    def __init__(self, myBooks):
        self.fd = myBooks
    
    def display(self):
        pos = 0
        for foods in self.fd:
            print("============ Bill counter ========")
            pos += 1
            print("============  FOOD ITEM NO", pos,"========")
            print("Food type : ", foods.type)
            print("Food nmae : ", foods.name)
            print("Food Price : ",foods.price)

    def getTotal(self):
        total = sum(map(lambda f : f.price, self.fd))
        print("=========== TOTAL PRICE =======")
        print(total)
   
    def delete(self):
        print("=========== DO YOU WANT DELETE? 1 = YES, 0 = NO")
        choice = int(input())
        if (choice == 1):
            print("=========== ENTER FOOD ITEM NUMBER =======")
            position = int(input())
            self.fd.remove(self.getfoodsById(position))
        else:
            print("=========== NO ITEMS DELETED =========")

    def getfoodsById(self, position):
        return self.fd[position - 1]

    
if "__MAIN__":

    print("========== WELCOME TO FOOD STALL ==========")

    fs = foodstall("Indian", "idli", 55)
    fs = foodstall("Indian", "Dosa", 70)
    fs = foodstall("North", "roti and curry", 100)
    fs = foodstall("Indian", "Full meals", 150)
    fs = foodstall("North", "Full meals", 170)
    
    
    fs.show()

    fs.select()

    selectedfd = fs.selectedfd()
    
    print(selectedfd)

    c = cart(selectedfd)

    c.display()

    c.delete()

    c.getTotal()
