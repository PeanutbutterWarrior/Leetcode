from itertools import zip_longest

def add_binary(self, a: str, b: str) -> str:
        carry = False
        new_string = []
        a = a[::-1]
        b = b[::-1]
        
        for item1, item2 in zip_longest(a, b, fillvalue=0):
            item1 = int(item1)
            item2 = int(item2)
            
            new_string.append(str(item1 ^ item2 ^ carry))
            carry = ((item1 ^ item2) & carry) | (item1 & item2)
        if carry:
            new_string.append('1')
        
        return ''.join(new_string[::-1])

# A faster solution that uses less memory, but sidesteps the problem

def add_binary_easy(self, a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]
