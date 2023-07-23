class wedding:
    def __init__(self):
        print("Hello Abdullah ")

    def congr(self):
        print("""'
    *********************************************
    *    Best wishes on this wonderful journey, *
    *    as you build your new lives together.' *
    *********************************************

        """)

    def Gift (self):
        print("""
        
 ---->CONGRAGULATIOIN MY DEAR FRIEND<----

_______¶¶¶_¶¶¶
______¶¶__¶__¶¶
______¶¶_____¶¶
_______¶¶___¶¶
________¶¶¶¶¶
_________¶¶¶
__________¶

           """)

        he = input("Are you accept my gift? [y/n].")
        if he == "y":
            print("""
            ___________________________
            *   Thank you my friend. *
            ___________________________
            """)

        else:
            print()
            print("""
            __________________________________________
               ----->Fuck your Beautiful wife.<-----
            __________________________________________
            
            """)

obj = wedding()
if __name__ == '__main__':
    while True:

        print("""
        1.  FOR CONGRAGULATION.
        2.  FOR GIFT.
        3.  Exit.    
        """)

        choice = int(input("Enter your choice."))
        if choice == 1:
            obj.congr()
        if choice == 2:
            obj.Gift()
        if choice == 3:
            exit(1)

