# Simple string checking
if answer.isdigit () :
    print (f"{chatbot_name}: Your answer should not be a number ! " )
elif answer == '':
    print (f"{chatbot_name}: Your answer should not be empty ! " )
if seats_reserve not in range (seats_in_row) :
    print ('Please choose a seat within our cinema :')