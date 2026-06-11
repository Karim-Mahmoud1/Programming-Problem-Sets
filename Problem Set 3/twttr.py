def main():
    
    user_input = input("Input: ")
    
    print("Output: ", end="")
    
    
    for char in user_input:
        
        if char.lower() not in ["a", "e", "i", "o", "u"]:
           
            print(char, end="")
            
   
    print()

main()