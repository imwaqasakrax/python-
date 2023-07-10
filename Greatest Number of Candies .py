class Solution(object):
  def kidsWithCandies(self ,candies, extraCandies):
    max_candies = max(candies)
    result = [candy + extraCandies >= max_candies for candy in candies]
    return result
