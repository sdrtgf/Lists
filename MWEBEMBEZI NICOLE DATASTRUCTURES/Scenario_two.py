#Scenario 2

#the following names are being added to the list
beatles = []
beatles.append("John Lennon")
beatles.append("Paul MacCartney")
beatles.append("George Harrison")
print(beatles)#Printing out new list


for i in range(1):
    names = input('Enter the names (Stu Stucliffe and Pete Best):')# the user enters the names
    beatles.append(names)# the names enered are added to the list
    
    
    
del(beatles[3])#removing the name Stu Stucliffe from the list
del(beatles[4])#removing the name Pete Best from the list

beatles.insert(0,'Ringo Starr')#Placing the name Ringo Starr at the beginning of the list
print(beatles)
