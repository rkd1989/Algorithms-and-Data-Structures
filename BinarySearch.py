Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class BinarySearch(object):
    def __init__(self):
        pass
    
    def binarySearch(self,arr, num):
        min = 0
        max = len(arr) - 1
        
        while max >= min:
            mid = min + max //2
            guess = arr[mid]
            if guess == num:
                return mid
            if guess > mid:
                min = mid + 1
            elif guess < mid: 
                max = mid - 1
        return None

bs = BinarySearch()

print(bs.binarySearch([0,2,3,4,5],3))

print(bs.binarySearch([0,1,2,3,4,5],8))
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> 
