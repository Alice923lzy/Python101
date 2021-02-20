def totalAmounts(location,giftCardAmounts):
    #given the name of a location, return the total amount of the gift cards in the list for
    #that location
    totalNumber = 0
    for x in giftCardAmounts:
        if x[0]== location:
            totalNumber += int(x[1])   #count the total number
    return totalNumber


    #print("The total amount of the gift cards in the list for ",location," is ",totalNumber,". ")

    


def allTotals(giftCards):
    #given a list of tuples of the form (location, amount), print out a list formatted like this:
    #location  totalAmountofGiftCardsFromThatLocation
    #this function must make use of the function called totalAmounts defined above
    rstList =[]
    locations=[]
    for tuples in giftCards:
        if tuples[0] not in locations:  #check for duplicated locations
            locations.append(tuples[0])
    for l in locations:
        temp=(l,totalAmounts(l,giftCards))
        rstList.append(temp)     # add (location,totalAmountofGiftCardsFromThatLocation) tuple to result list
    
    
    print("This list shows the total amount of gift cards in each location now: ",rstList)

    

    


def increaseAmazonCards(giftCards):
    #increase the amount of each amazon gift card by $50.
    rstList=[]
    for tuples in giftCards:
        if tuples[0] == "amazon":   #distinguish amazon from others
            rstList.append((tuples[0],tuples[1]+50))   # add $50 
        else:
            rstList.append(tuples)

    print("This is the list after increasing the amount of each amazon gift card by $50: ",rstList)
    
    return rstList



def addNewCards(giftCardAmounts):
    #write the function to add a new card (and amount) to the list of gift cards.
    #this function will prompt the user for the card location and the amount and add
    #it to the list.
    print("Let's add a new card to the list")
    location = input("Please enter the card location: ")
    amount = input("Please enter the amount of this card: ")
    giftCardAmounts.append((location,amount))
    print("This is the new list: ",giftCardAmounts)

    return giftCardAmounts



def combineCards(giftCards):
    #write a function that will take the list of cards and combine the amounts for the
    #cards from the same location.
    #your function should not change the original list, but instead create a new list
    #containing only unique locations and the total of the cards for that location.
    #This new list should be returned.
    #The format should be [[location, totalAmount], [location, totalAmount] ...]
    
    rstList =[]
    locations=[]
    for tuples in giftCards:
        if tuples[0] not in locations:  #check for duplicated locations
            locations.append(tuples[0])
    for l in locations:
        temp=[l,totalAmounts(l,giftCards)]
        rstList.append(temp)     # add (location,totalAmountofGiftCardsFromThatLocation) tuple to result list
    
    
    # print("This list shows the total amount of gift cards in each location now: ",rstList)

    return rstList





def numberOfCards(location,giftCards):
    #this function should take as a parameter a location and it should return the number
    #of cards in the list for that particular location.
    #there should be NO USER INPUT in this function and no print() statements.
    rstNum =0
    for tuples in giftCards:
        if tuples[0] == location :   #compare
            rstNum += 1                  
    return rstNum

    

def main():
    #make your program user friendly by adding print statements telling the user what is happening
    giftCardAmounts = [("amazon", 200), ("mastercard", 250), ("amazon", 300),
                       ("esso", 250), ("mastercard", 300), ("semphora", 100),
                       ("semphora", 200), ("amazon", 400), ("esso", 200)]
    print("")
    
    #call totalAmounts() with locations equal to "semphora" and "amazon"
    totalAmounts("semphora",giftCardAmounts)
    totalAmounts("amazon",giftCardAmounts)


    #call allTotals()
    allTotals(giftCardAmounts)


    #call increaseAmazonCards()
    giftCardAmounts = increaseAmazonCards(giftCardAmounts)
    #call allTotals() again
    allTotals(giftCardAmounts)




    #call addNewCards()
    giftCardAmounts = addNewCards(giftCardAmounts)
    #call allTotals() again
    allTotals(giftCardAmounts)


    #call combineCards()
    #print the result
    print(combineCards(giftCardAmounts))



    #ask the user for a location
    location = input(" Please enter a location in the list to calculate number of cards: ")

    #call numberOfCards() and print the result
    
    print("There is/are ",numberOfCards(location, giftCardAmounts)," cards in the list for ",location)
    
main() 