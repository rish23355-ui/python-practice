#1: Odd or Even (string)
#Plain English: Take string and count the numbers of characters if the count comes as even return true and if odd return false 
def odd_or_even(s):
    if len(s) % 2 == 0:
        return True 
    else:
        return False


#2: Default Mood
def mood_today(mood="neutral"):
    return f"Today, I am feeling {mood}"


#3: How Many Vowels
def count_vowels(s):
    count = {}
    count = 0
    for letter in s:
        if letter in s:
             count += 1
    return count


#4: Luke, I Am Your...
#Plain English: We have to take the information given in the box of luke relations with others and make a dictionary of those relations to help him remind of who is who 
def relation_to_luke(name):
 relations = {
"Darth Vader": "Luke, I am your father.",
    "Leia": "Luke, I am your sister.",
		"Han": "Luke, I am your brother in law.",
    "R2D2": "Luke, I am your droid."
}
 return relations [name]


#5: Sum of Resistance in Series Circuits
# Plain English: Take an arrays of values resistance that are connected in series and calculates the total resistance of the circuit in ohms
def series_resistance(lst):
    total = 0
    for r in lst:
     total += r
    return total

	
#6: Instant JAZZ
def jazzify(lst):
    result = []
    for chord in lst:
        if chord[-1] == '7':
            result.append(chord)
        else:
            result.append(chord + '7')
    return result


#7: Find the Odd Integer
#Plain English: Take a list and finds the intergers that appears an odd number of times and there will be one will intergers that will
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


#8: Two Sum
def two_sums(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i


#9: Contains Duplicate
#Plain English: Take an array and see if any value if appeared atleast twice then return true and if every value is differnt return false using if else and dictionary
class Solution(object):
    def containsDuplicate(self, nums):
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1
        return False               
    

#10: Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        counts_s ={}
        for letter in s:
            if letter in counts_s:
                counts_s[letter] += 1
            else:
                counts_s[letter] = 1
        counts_t ={}
        for letter in t:
            if letter in counts_t:
                counts_t[letter] += 1
            else:
                counts_t[letter] = 1
        return counts_s == counts_t


#11: Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit > profit
        return max_profit        


#12: Maximum Subarray
#Plain English: Take an array and find the subarray with the largest sum and return its sum
class Solution(object):
    def maxSubArray(self, nums):
        current_sum = 0
        max_sum = float('-inf')
        for num in nums:
            current_sum = current_sum + num
            max_sum = max(current_sum, max_sum) 
            if current_sum < 0:
                current_sum = 0
        return max_sum

