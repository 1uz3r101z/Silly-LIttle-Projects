#having a conversation 
print("Hello, who may you be?\n")
name=input()
print("Hey", name , ". It's been a while, how's it going?\n")
# print(f"Hey {name}. It's been a while, how's it going?\n")
going=input()

print("Oh, wow... that sure sounds like an eventful err few years. Well, how's the weather where you are at?\n")
print("Enter the temperature in celcius (Enter Numbers Between (-30 to 60)):\n")
weather=input()

print("Ah, I'm not used to  hearing about the weather in celcius mode... do you think you can be kind enough to convert it to fahrenheit,please?\n")
convert=input()
celcius=input()
while True:

    try:
        celcius= float(input("Enter the temperature in celcius (numbers between -30 and 60):\n"))
    except ValueError:
        print("Enter a valid number bro...")
        continue
    if not -30 <= celcius <=60:
        print("Warning: Bro c'mon the temp is out of range... please enter a valid number between -30 and 60")
        continue 
    fahrenheit = (celcius * 9/5) + 32
    print("fahrenheit =", fahrenheit)
    break   

    

print("Thank you", name, "I'm sorry I didn't reach out after everything went down...I do sure hope you understand.\n")
understand=input()
print("I'm glad to see that you're alive and breathing...Listen if you don't mind me asking... because I do worry. Are you financially well after leaving the manor?\n")
breathing=input()
print("If you don't mind me asking how many hours are you working, what's your rate of pay and your weekly gross pay?\n")
pay=input()
hours=int(input("input hour:\n"))
rate=float(input("input rate:\n"))
print("gross pay=", hours*rate)
print("But if I get lucky and work the same hours the second week and save up, my gross pay would be", (hours*rate)+(hours*rate))
print("Well, my dear", name, "I'm glad to hear that you you're alive and well. I just received a message that Bruce is on the way... I'm sorry to say this, but you must be on your way now.\n")
Bruce=input()
print("Take care", name, "and stay safe out there.")