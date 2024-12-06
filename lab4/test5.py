intent_feelings = compare_intent(feelings_response.lower() , intent_threshold )
# Prints feeling according to user emotion inputted
if ('feelings _user_positive' in intent_feelings ) or ('feelings_user_negative' in intent_feelings ) :
    print (f" { chatbot_name }: { intent_feelings [1]} " )