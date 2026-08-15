Plain English: take string and count the numbers of characters if the count comes as even return true and if odd return false 
def odd_or_even(s):
    if len(s) % 2 == 0:
        return "Even" 
    else:
        return "Odd"

print(odd_or_even("hello"))
print(odd_or_even("hi"))
print(odd_or_even("code"))

def mood_today(mood="neutral"):
    return f"Today, I am feeling {mood}"

print(mood_today("happy"))
print(mood_today("sad"))
print(mood_today())

def count_vowels(s):
    count = {}
    count = 0
    for letter in s:
        if letter in s:
             count += 1
    return count

print(count_vowels("rishabh"))        
print(count_vowels("Celebration"))  # should give 5
print(count_vowels("Palm"))         # should give 1
print(count_vowels("Prediction"))

We have to take the information given in the box of luke relations with others and make a dictionary of those relations to help him remind of who is who 
def relation_to_luke(name):
 relations = {
"Darth Vader": "Luke, I am your father.",
    "Leia": "Luke, I am your sister.",
		"Han": "Luke, I am your brother in law.",
    "R2D2": "Luke, I am your droid."
}
 return relations [name]

print(relation_to_luke("Darth Vader"))
print(relation_to_luke("Leia"))
print(relation_to_luke("Han"))
print(relation_to_luke("R2D2"))

Plain English: Take an arrays of values resistance that are connected in series and calculates the total resistance of the circuit in ohms
def series_resistance(lst):
    total = 0
    for r in lst:
     total += r
    return total


print(series_resistance([1, 5, 6, 3]))   # should give 15
print(series_resistance([20, 35, 4]))    # should give 59
	

def jazzify(lst):
    result = []
    for chord in lst:
        if chord[-1] == '7':
            result.append(chord)
        else:
            result.append(chord + '7')
    return result

print(jazzify(["G", "F" , "C7"]))

Plain English: Take a list and finds the intergers that appears an odd number of times and there will be one will intergers that will
def find_odd(lst):
	counts = {}
	for num in lst:
		if num in counts:
			counts[num] += 1
		else:
			counts[num] = 1
	for num in counts:
		if counts[num] % 2 != 0:
			return num

print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))  # → -1
print(find_odd([10]))                                     # → 10


def two_sums(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i

print(two_sums([2,7,11,9], 9))

Plain English: Take an array and see if any value if appeared atleast twice then return true and if every value is differnt return false using if else and dictionary
class Solution(object):
    def containsDuplicate(self, nums):
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1
        return False              
