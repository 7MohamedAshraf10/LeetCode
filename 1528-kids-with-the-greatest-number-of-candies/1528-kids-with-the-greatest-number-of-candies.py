class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # initalize list for results
        result = []
        # get the max number of candies in the list
        maxCandies = max(candies)
        # iterate thorw the list
        for i in range(len(candies)):
            # check if the (current candies + extra Candies) is bigger than or equal the max candies
            if candies[i] + extraCandies >= maxCandies:
                # if the condition applied, append True to the result list
                result.append(True)
            else:
                result.append(False)
        return result