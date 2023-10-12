class Solution:
    def intToRoman(self, num: int) -> str:
        
        # Define a dictionary that maps integer values to their corresponding Roman numeral symbols
        # Sorted ascending to use the keys in the for loop
        RomanDict ={
            1000: "M", 
            900: "CM",
            500: "D", 
            400: "CD",
            100: "C",
            90: "XC",
            50: "L", 
            40: "XL",
            10: "X", 
            9: "IX",
            5: "V",    
            4: "IV",
            1: "I",
        }
        # Initalizting string for the Roman Symbols
        Roman = ''
        # Iterate through the keys (integer values) in the RomanDict dictionary
        for i in RomanDict.keys():
            # While the current integer value is less than or equal to the input 'num'
            while i <= num:
                # Append the corresponding Roman numeral symbol to the 'Roman' string
                Roman += RomanDict[i]
                # Subtract the integer value from 'num' to track the remaining value
                num -= i

        return Roman