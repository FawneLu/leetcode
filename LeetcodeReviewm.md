#LeetcodeReview  
- Counter can be used in sequence object(string,list,tuple,set).
##BitManipulation  
**Always pay attention to bit operations**  

- &：Can be used to count how many '1' are there in the binary. We can count n*(n-1) when n>0.  


####136.Single Number  
- Normal Way  
Create a new Dictionary, if element in the list exists(in the form of key) in the dictionary, then the value will add 1.  
If the the element doesn't have a corresponding key, then the value equals to 1.  
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:  
         nums_dict = {}  
         for num in nums:  
             if num not in nums_dict:  
                 nums_dict[num] = 1  
             else:  
                 nums_dict[num] += 1  
```

- Use built-in function Counter  
Counter to count the number of the appearance of the element in the list.  
Key of the dictionary refers to the element;  
Value of the dictionary refers to the number of appearance.  
```python
from collections import Counter  

class Solution:  
    def singleNumber(self, nums: List[int]) -> int:  
         nums_dict = Counter(nums)  
         for key,value in nums_dict.items():  
             if value == 1:  
                 return key  
```

- Bit Operation  
XOR: If the 2 numbers are the same, then the result is 0. 0 and any other number do the XOR operation, the result is that number. So we can apply XOR operation in this problem.  The result of the XOR operation in this problem is the number which appear once.  
**Best time complexity:O(n); Best sapce complexity O(1)**  
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
         ini = 0
         for num in nums:
             ini ^= num
         return ini
```
We can also use built-in operator 'xor' and built-in functool 'reduce'.  
```python
from operator import xor
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
         return reduce(xor,nums)
```

####191.Number of 1 Bits  
- Use built-in function Counter  
Counter to count the number of the appearance of the element in the list.  
Key of the dictionary refers to the element;  
Value of the dictionary refers to the number of appearance.   
First , using bin() to change the int to string, then return the value whose key is 1.  
```python
from collections import Counter

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=bin(n)
        print(a)
        num_dict=Counter(a)
        print(num_dict["1"])
```  
- Bit Operation   
AND: When the two numbers are 1, the the result is 1. Otherwise, results are 0.  
We can apply AND operation in this problem, that n=n&(n-1)(in n-1, the least significant 1 in n will change into 0). When n=0, the number of calculation is the number of 1.  
**Best time complexity:O(n); Best sapce complexity O(1)**  
```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        count=0
        while n!=0:
            n &=n-1
            count+=1
        return count

```

####190.Reserve Bits  

- Use built-in function reverse    
Firstly, we can use '{:032b}'.format(n) to change the int to binary, then we change it to the list and use .reverse() to reverse it. FInally we chang it into string and then into int.  
```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #print(type(n))
        num = '{:032b}'.format(n)
        #print(num)
        l=list(num)
        l.reverse()
        b="".join(l)
        #print(type(b))
        b=int(b,2)
        return b
```  
- Bit Operation  
Just think about reversing an int(mod and divide).  
Left shift equals multipling the number by 2, right shift equals dividing the number by 2.  
**Best time complexity:O(n); Best sapce complexity O(1)**
```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        result=0
        for i in range(32):
            result=(result<<1)+n%2
            n=n>>1
        return result
```

####231.Power of Two  
- Use built-in function Counter  
Firstly, we need to judge whether the input is above 0 or below 0. If it is less than 0, then the input is not the power of two. If it is larger or equal 0, then we use Counter to count the number of 1 and 0. If the number of 1 is 1, then the input is the power of 2.  
**This one is bad!!! Terribly bad**
```python
from collections import Counter
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n>0):
            a=bin(n)
            num_dict=Counter(a)
            if(num_dict["1"]==1):
                return 1
            else:
                return 0
        else: 
            return 0
```  
Or, we can just use count.  
```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        else:
            return bin(n).count('1')==1
```  
- AND:When the two numbers are 1, the the result is 1. Otherwise, results are 0.  
We apply this way in the problem, if we do the and operation between n and n-1 then the result must be 0 if the input is power of 2. Otherwise return false.  
**Best time complexity:O(1); Best sapce complexity O(1)**  
```python
from collections import Counter
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and (n&(n-1))==0
```  
####342.Power of Four  
The difference between this problem and the 'power of two' is that in the binary, the 1 must be on the odd position.  

- Normal Way  
Firstly, we use bin operation to judge whether there's only one '1' in the binary and then we judge whether the odd position is '1'.  
```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num>0 and (num&(num-1))==0 ):
            n = '{:032b}'.format(num)
            l=list(n)
            #print(l)
            for i in range(len(l)):
                #print(i)
                if(i%2==1 and l[i]=="1"):
                    return True
        else: return False

```  
- Tricky Mask  
We can use AND operation betwwen '0b01010101010101010101010101010101' and input to judge whether the only 1 is on the odd position(num& 0b01010101010101010101010101010101==num).  
**Best time complexity:O(1); Best sapce complexity O(1)**
```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num>0 and (num&(num-1))==0 and (num&0b01010101010101010101010101010101==num))
```  

####401.Binary Watch  
- Violence Way  
Firstly, we can count the number of '1' in the num. Then we use a violence algorithm to calculate all the possibilities of the time and compare with the num.  
```pyhthon
class Solution(object):
    
    def countBit(self,num):
        count = 0
        while num:
            num &= (num - 1)
            count += 1
        return count
        
    
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res =[]
        for hour in range(12):
            for minutes in range(60):
                time = "{}:{:02d}".format(hour,minutes)
                if self.countBit(hour)+ self.countBit(minutes) == num:
                    res.append(time)
        return res
```  

####461.Hamming Distance  
- Bin Manipiulation  
We can use ^ to get the number(position of different number between the two inputs is 1, the same is 0). Then we can use &(n&n-1) to count the number of '1's.  
```python
class Solution(object):
    def Count(self,num):
        count=0
        while num:
            num &=num-1
            count+=1
        return count
    
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return self.Count(x^y)
```  

####645.Set Mismatch  
- Normal Way  
We can use a dictionary to count the number of appearance of the value in the list. If the value in the dictionary is 2, then we return the corresponding index.  Then we use the difference(差) to get the missing value.(应有的list减去（input-重复值）)  
```python
from collections import Counter
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        rep_num = None
        tmp_dict = Counter(nums)
        for key, value in tmp_dict.items():
            if value == 2:
                rep_num = key
        
        return [rep_num, sum(range(1,len(nums)+1)) - (sum(nums) - rep_num)]
```  

- Position Reverse  
This is a tricky way. If the number in the list isn't replicated, then we make the number multiply -1. Before this, we need to judge whether the number is smaller than 0. If so, means the number has been existed. Then we get the replicated number.  
```python
class Solution(object):
    def findErrorNums(self, nums):
        res = []
        for index in nums:
            if nums[abs(index)-1]<0:
                res.append(abs(index))
            else:
                nums[abs(index)-1]*=-1
        
        for i,num in enumerate(nums):
            if num>0:
                res.append(i+1)
        
        return res
```

####137.Single NumberII  
- Use built-in function  
We can create a dictionary and use counter to count all the numbers in the list. If the value equals to 1, then we return the key.  
```python
from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict=Counter(nums)
        for key, value in num_dict.items():
            if value==1:
                return key
```  

- Sort  
Firstly, we can sort the nums then we use range with the interval equals to 3.  
```python
class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        for i in range(0,len(nums)-1,3):
            if nums[i]!=nums[i+1]:
                return nums[i]
            
        return nums[-1]
```
- Reference from Master Zhang  
```python
from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        a = 0; b = 0
        for i in range(len(nums)):
            b = b^nums[i] & ~a
            a = a^nums[i] & ~b

        return b
```

####371.Sum of Two Integers  
- use sum  
```python  
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        return (sum([a,b]))
```  
- Bin Operation  
我们用异或去计算两个数的模2加，用两个数的与，右移1位来表示他们的进位。这两个位运算的数相加即是两数之和。 python 用来实现这种方法不现实，因为会不停地进位，循环就不会暂停。用C语言或者C++可以实现。
```python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b:
            tmp = a & b
            a = a ^ b
            b = tmp << 1
        return a
```
####268.Missing Number  
- Sort  
We can sort the list first and return the number which is not equal to the index.  
```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)
```
- Minus  
We can return the sum of non-missing list minus sum of the input list.  
```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums)+1))-sum(nums)
```
- Bin Operation  
We can define x=0. Then we use ^. Since the index and the number need to equal to each other, so we can return x^index^nums[index].  
```python
def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in range(1,len(nums)+1):
            x = x^i^nums[i-1]
        return x
```  

####762.Prime Number of Set Bits in Binary Representation  
- Just One Way  
First we count the number of ones in the range, then we judge whether the number is prime.
```python
class Solution(object):
    def Counter(self,num):
        count=0
        while num:
            num &=num-1
            count+=1
        return count
    
    def Prime(self,p):
        if p==1:
            return False
        for i in range(2,int(p**0.5)+1):
            if p%i==0:
                return False
        return True
    
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        result=0
        for n in range(L,R+1):
            num_bit=self.Counter(n)
            if self.Prime(num_bit):
                result+=1
        return result
```

