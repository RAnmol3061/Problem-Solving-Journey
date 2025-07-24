## Problem Statement

The prime factors of **13195** are **5**, **7**, **13** and 29.

What is the largest prime factor of the number **600851475143**?

**Problem Statement Link** [https://projecteuler.net/problem=3]

## Thought Process

To find prime factors of the given number, we first need to know which number are prime to divide with given number

So first we are focusing on find prime number

After finding prime number, we will divide the given number by smallest possible prime number

### Method 1 

Implementing my thought process, first we will find prime numbe by looping till an arbitary number. The reason for looping to an arbitary number is that this approach is too inefficient for large number.

```python
#Method 1
given_no = 600851475143
prime_no = []

#1st Part
for i in range(2,10000): # I have choosen an aribitary upper limit
    c = 0
    for j in range(1, (i//2)+1): #(i//2)+1 because a number more than half of original number cannot be a factor
        if i%j ==0:
            c += 1
            if c >= 2: 
                break
    if c ==1:
        prime_no.append(i)

#2nd Part
a = []
prime_no_index = 0

while given_no > 1 and prime_no_index < len(prime_no):
    current = prime_no[prime_no_index]
    while given_no % current == 0:
        given_no /= current
        a.append(current)
    prime_no_index += 1

print(max(a))
```

**Quick Summary**

- We first find the prime number till 10000.
- If anyone is wondering why ```if c ==1:``` not ```if c==2:``` because the loop will never reach the number itself, so the only factor we should find is 1.
- 2nd part of the program, divides prime number with given number till it given number is not 1
- Why I have taken 10000 as the upper limit? By trail and error, there is no inhernt logic behind it. It just works


#### Time and Space Complexity

- Time Complexity is $O(N^2)$. As there is a loop inside a loop
- Space Complexity is $O(N)$. As we are only saving prime numbers and prime factors

### Method 2

This method will be significantly more efficient than Method 1. We would be using two new concepts (which I also didn't know before) - 

1) Sieve of Eratosthenes
2) Checking till square root of given number
