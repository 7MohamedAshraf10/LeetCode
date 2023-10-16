class Solution:
    def compress(self, chars: List[str]) -> int:
        # there's nothing to compress, so we return 0.
        if not chars:
            return 0
        # track the current position where we are writing compressed characters
        write =0
        # represents the count of consecutive characters.
        count = 1
        for i in range(1 , len(chars)):
            #  check if the current character is the same as the previous character
            if chars[i] == chars[i - 1]:
                count+=1
            else:
                chars[write] = chars[i-1]
                write +=1
                if count > 1:
                    for dig in str(count):
                        chars[write]=dig
                        write+=1
                count = 1
        # handle the last character and its count    
        chars[write] = chars[-1]
        write += 1
        #  if there's a count greater than 1 for the last character, we convert it to a string and split it into digits
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

        return write
