from re import X


def shopy(item):
    shoes={"jogers":"1200rs","snickers":"1000rs","boots":"2000rs"}

    if item.lower()=="shoes":
        for a,x in enumerate(shoes.keys()):
            print(a+1,x)
        
        print("What you want to buy?")
        buy=input("Enter product name please")
        if buy.lower()=="jogers":
            print (shoes["jogers"])
        elif buy.lower()=="snickers":
            print (shoes["snickers"])
        elif buy.lower()=="boots":
            print(shoes["boots"])
        else:
            print("you have enter wrong item")



        

