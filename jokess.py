import pyjokes as pj

def tell_some_jokes():
    print("I am your jocks telling bot. type 'yes' or 'no' =  ")
    response=input("Do you want jokes(yes/no) = ").lower()
    while True:
        if(response=='yes'):
            joke=pj.get_joke()
            print(joke)
        elif(response=='no'):
            print("thanks tata!")
            break
        else:
            print("invalid response! Type yes/no")

tell_some_jokes()