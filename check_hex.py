def check_selection(values):
    hexs = ["A", "B", "C", "D", "E", "F",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for value in values:
        if value.upper() not in hexs:
            print("Not a hexidecimal!")
            return(False, True)
    return(True, False)    
    

def main():
    good_selection = False 
    while not good_selection:
        selection = input("Provide a hexidecimal number:")
        good_selection = check_selection(selection)
    print("Good job",selection,"is a hexidecimal number!")

    


if __name__ == "__main__":
    main()