
## Problem Statement

If we list all the natural numbers below **10** that are multiples of **3** or **5**, we get **3**, **5**, **6**, and **9**. The sum of these multiples is **23**. Find the sum of all the multiples of **3** or **5** below **1000**.

[**Problem Statement Link**](https://projecteuler.net/problem=1)

## Thought Process

What I can understand from the initial reading of the question is that we need to find the sum of numbers that are multiples of 3 or 5. 

So, we have to make sure to avoid adding numbers like 15, 30 etc two times.

From my previous experience, the concept of A.P (Arthemitic Progression) would be useful here.

The formulas I know right now are: 
- $S = n/2(2a + (n-1)d)$
- $a_n= a + (n-1)d$
- $S = n/2(a + l)$

Where: - 
- S is the sum of the A.P
- $a_n$ is the last term of the A.P
- n is the no. of terms of an A.P
- a is the first term of an A.P
- d is the common difference an A.P

### Method 1

I am thinking brute forcing my way through it.

We can solve it by finding multiples of 3, 5 and 15. then we find the sum of multiples of 3, 5 and 15. We add the sum of 3 and 5 then subtract it with 15 to find the answer. 

```python

list_3 = [i for i in range(3,1000,3)] #I have written 1000 not (1000 + 1) because no. below 1000 is asked
list_5 = [i for i in range(5,1000,5)]
list_15 = [i for i in range(15,1000,15)]

ans = sum(list_3) + sum(list_5) - sum(list_15)
print(ans)
```
#### Time and Space Complexity

- Time Complexity is O(N)
- Space Complexity is O(N)

### Method 2

We solve it the same way, only difference is we are using loop instead of list comprehension

```python

sum = 0
for i in range(1,1000):
    if i % 3 ==0:
        sum += i
    elif i % 5 ==0: # If we had written "if" instead of "elif" then it would also include multiple of 15.
        sum += i 
print(sum)
```

#### Time and Space Complexity

- Time Complexity is O(N)
- Space Complexity is O(1)

### Method 3

We can try solving it using the formula $S = n/2(2a + (n-1)d)$, Where:

- S is the sum of A.P
- n is the number of terms in A.P
- a is the first term of A.P

To use this formula we have to know the 'n' - number of terms in A.P, to find 'n'

we have to use this formula $a_n = a + (n-1)d$ where,

- $a_n$ is the last term of A.P
- a is the first term of A.P
- n is the no. of term in A.P
- d is the common difference of A.P

Here we don't know both '$a_n$' and 'n' so we have to find last term first to proceed

```python

limit = 1000 #Given in Question

def sum_AP(limit,d):
    a = d # d is first term according to this question
    
    #Find last term 
    for i in range(limit-d, limit):
        if i%d == 0:
            l = i
            break
    #Find No. of terms in an AP
    n = round(((l - a)/d) + 1) # This is derived standard A.P formula

    sum_ap = (n/2)*(2*a + (n-1)*d)
    
    return sum_ap

sum_3 = sum_AP(limit,3)
sum_5 = sum_AP(limit,5)
sum_15 = sum_AP(limit,15)

print(sum_3 + sum_5 - sum_15)
```

#### Time and Space Complexity

- Time Complexity is O(1). It's almost constant because it won't take that much time to calcuate last term
- Space Complexity is O(1)

### Method 4

The only difference between Method 3 and Method 4 is the different way of finding the last term.

- In Method 3, I am looping to find the last term
- In Method 4, I am using a formula which workes here to find the last term

```python

# Method 4
def sum_AP(limit, d):

    a = d
    l = ((limit - 1) // d) * d     # Find the last term
    n = round(((l-a) / d) + 1)  # Find the number of terms in A.P    
    sum_ap = (n/2)*(2*a + (n-1)*d)
    
    return sum_ap

limit = 1000 #Given in Question

sum_3 = sum_AP(limit, 3)
sum_5 = sum_AP(limit, 5)
sum_15 = sum_AP(limit, 15)

ans = sum_3 + sum_5 - sum_15
print(ans)
```

#### Time and Space Complexity

- Time Complexity is O(1)
- Space Complexity is O(1)

------------------------------------x--------------------