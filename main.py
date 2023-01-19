'''
3. Multiples of 3 or 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23. We are looking for a method that given a positive integer 𝑛, it finds the sum of all the multiples
of 3 or 5 below 𝑛.
a) Implement this method.
b) Print out the results on the following inputs to see whether your method gives you what you expect:
i. 5
ii. 10
iii. 500 (it should return 57918)
iv. 1000 (it should return 233168)
v. 333
'''
from typing import List


def multiplesOf3or5(x: int):
    multiple_sum = 0
    for i in range(x - 1, 0, -1):
        if i % 3 == 0 or i % 5 == 0:
            multiple_sum += i
    return multiple_sum


# print(multiplesOf3or5(333))


def removeDupes(nums):
    if len(nums) == 1:
        return nums
    else:
        i = 1
        while i < len(nums):
            if len(nums) == 1:
                return nums
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                i -= 1
            else:
                i += 1
    return nums


# print(removeDupes([0,0,0]))


'''
Number of Words
Given a paragraph (as a string), we need a method that returns the number of words in that paragraph. All the
words are separated by blanks or newline, and no words are crossing lines. The following are some example
inputs and outputs of this method with explanations:
“It’s a closed-book-closed-notes exam.” => 4 (“It’s” is one word, “closed-book-closed-notes” is one word)
“““-How much money do you have?
-50 dollars.””” => 8 (‘50’ is one word)
“www.google.com is a website.” =>4 (the address counts as one word)
The method split can be useful for this question.
“a*b*c*d*”.split(‘*’) returns [‘a’, ’b’, ‘c’, ‘d’, ‘’]
a) Implement this method.
b) Print out results on inputs from the above examples. Then print out the results on the following
inputs:
i. “““Starting the Fall of 2021, the Academic Resource Center is
moving to in person tutoring for most subject areas. There are some online
tutoring sessions available for some subjects.”””
ii. “Academic Calendar\nAcademic Programs- Graduate\nAcademic Programs- Undergraduate”
'''


def numOfWords(x: str):
    # wordCounter = 1
    # for i in x:
    #     if i == " ":
    #         wordCounter += 1
    # return wordCounter
    counter = 0
    if "\n" in x:
        print('yes')

    print(x.splitlines())
    splitedList = x.split(" ")
    print(splitedList)

    return len(splitedList) + counter


print(numOfWords("""-How much money do you have?
-50 dollars."""))
