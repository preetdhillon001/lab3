#declaring dictonary
shoppingCart={}
#introducing variable
i=0
j=0
#print statements
print("WELCOME TO THE AMANDO SHOPPING SITE")
print("1.Add product to the cart")
print("2.Search the product")
print("3.Delete the product from the cart")
print("4.Quit")


#while loop
while(i!=4):
 i=int(input("ENTER YOUR OPTION:"))

#option for adding item
 if(i==1):
    p=int(input("ENTER NUMBER OF ITEMS TO ADDED: "))
    g=0
    
    while(g<p):
     if(p<5):
      b=input("Enter an item:")
      a=input("Enter brand name:")
  #updating dictionary
      shoppingCart.update({b:a})
      print("you added following items to the cart successfully")
      
     else:
       pass
       
       if(g==0):
        print("Cart is full")
        g=g+1
    #output after addition of items
    print(shoppingCart)
#option for searching item
  
 elif(i==2):
   b=input("Enter an item:")
   x=0
   for j in shoppingCart.keys():
      if (j==b):
        #displaying searched item
       print(j+":"+shoppingCart[j])
       x=1
      else:
       pass
   
   if(x==0):
      print("No product exists with this name")

#option for deleting item
 elif(i==3):
   b=input("Enter an item:")
   
   shoppingCart.pop(b)
   #output after deleting items
   print("Cart is empty, no item is found") 
#option for quiting
 else:
  print("Quiting")

  