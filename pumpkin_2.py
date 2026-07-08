#Having another conversation with Red Hood
print("Hey, who goes there? What's your name traveler?\n")
name=input()
print("Oh... well I've never heard of a", name , "can you tell me more about yourself?\n")
self=input()
print("Wow... that's quite the background", name , ".So if you don't mind me asking...what brings you here?\n")
brings=input()
print("wait wait wait...you're telling me that's why you're here? I mean I get that err how should I say this. What brings you here specifically?\n")
here=input()
print("Well... now I feel quite honored that you would choose a place like this as a rest stop. Let me make you something to eat real quick. What would you like?\n")

print("Choose between these three food options: cheeseburger with fries, hot wings with celery and carrot sticks, or a panini with your choice of ingredients.\n")

#food choice


food=input("Which would you like?:").strip().lower()
valid= False

while not valid:
    if "cheese" in food or "cheeseburger" in food:
        valid=True
        print("Great - How would you like your burger cooked? Well done or rare?\n")
    
        done=input()
        print("Okay! one", done , "Cheeseburger with fries coming up!\n")
        

    elif "wing" in food or "wings" in food:
        valid=True
        print("Hot wings with celery and carrot sticks, got it.\n")
        

    elif "panini" in food:
        valid=True
        print("A panini - What ingredients would you like?\n")
        ingredients=input()
        
        print("A panini with:", ingredients , ", coming right up", name , "!\n")
    else:
        print("Sorry, we don't serve that here. Please choose the three I suggested.\n")
        food=input("Which would you like?:").strip().lower()
        
        #Re-Direct conversation

print("So", name , ", I know it's none of my business or anything, but what do you mean by 'confront' your so called err 'savior'?\n")
confront=input()
print("Ah... I see.\n")
see=input()
print("Well I'm glad to at least be the one to fill your stomach up with something good before you go on this journey of yours.\n")
journey=input()
print("Stay safe", name , ", and I'll keep an eye on the news for the grand", name , ",and no matter what you'll always be welcomed here.\n")
grand=input()
print("Until next time.")