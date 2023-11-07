class Solution:
    def decodeString(self, s: str) -> str:
        stack = []        
        # Iterate over each character in the input string
        for char in s:
            # If the character is not a closing bracket, add it to the stack
            if char !=']':
                stack.append(char)
            else:
                # Initialize an empty string to hold the current sequence of characters
                current = ''
                # Pop characters from the stack until an opening bracket is found
                while stack:
                    val = stack.pop()
                    if val == '[':
                        break
                    # Add the popped character to the beginning of the current sequence
                    current = val + current
                
                # Initialize an empty string to hold the current multiplier
                num = ''
                # Pop digits from the stack to form the multiplier
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                
                # Multiply the current sequence by the multiplier and add it back to the stack
                stack.append(int(num) * current)
        
        # Join all the elements in the stack to form the final decoded string
        return ''.join(stack)
