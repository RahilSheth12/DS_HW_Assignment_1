# 1. Palindrome Number

def PalindromeChecker(self, x: int):
    return str(x)[::-1] == str(x)


# print(PalindromeChecker(0))
# print(PalindromeChecker(-121))
# print(PalindromeChecker(121))
# print(PalindromeChecker(2147447412))
# print(PalindromeChecker(12345432))

# 2. Remove Duplicates from Sorted Array
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
# print(removeDupes([1,1,2]))
# print(removeDupes([-5, -5, -3, -3, -1, -1]))
# print(removeDupes([0, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 100]))
# print(removeDupes([-10, -10, -10, -10, -10, -10, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]))


# 3. Multiples of 3 or 5
def multiplesOf3or5(x: int):
    multiple_sum = 0
    for i in range(x - 1, 0, -1):
        if i % 3 == 0 or i % 5 == 0:
            multiple_sum += i
    return multiple_sum


# print(multiplesOf3or5(5))
# print(multiplesOf3or5(10))
# print(multiplesOf3or5(500))
# print(multiplesOf3or5(1000))
# print(multiplesOf3or5(333))


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


# 4. Number of Words
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
