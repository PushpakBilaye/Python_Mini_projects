'''
raw:

candy=100
rs=2
while ch==y else break
candy=candy-input
'''


print("******************************")
print("**********CANDY JAR***********")
print("******************************")
print("Candies in a jar = 100")
candy=100
rs=2
ch='y'
while ch=='Y' or ch=='y':
    candies= int(input("How many candies do you want? "))
    if candies < candy or candies == candy:
        total=candies*rs
        print("Here are your",candies,"candies. Your have to pay Rs.",total)
        print(candy-candies,"candies left in the jar.\n!! THANK YOU !!")
        ch=input("Do you want more?(Y/N):")    
    
    else:
        print("SORRY !! WE DONT HAVE ",candies,"CANDIES.")
        print("COME TOMMORROW")
        break
    candy= candy-candies

