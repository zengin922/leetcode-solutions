from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Dictionary to store numbers we have already seen
        # Format: {number: index}
        seen = {}

        # Loop through the list while getting both
        # the index and the number itself
        for i, num in enumerate(nums):

            # Calculate the number we need
            # to reach the target
            needed = target - num

            # Check if the needed number
            # has already been seen
            if needed in seen:

                # Return the index of the needed number
                # and the current index
                return [seen[needed], i]

            # Store the current number and its index
            # in the dictionary for future lookups
            seen[num] = i

        # Return empty list if no solution exists
        return []


# Create an instance of the Solution class
solution = Solution()

# Call the twoSum method and print the result
print(solution.twoSum([2, 7, 11, 15], 9))