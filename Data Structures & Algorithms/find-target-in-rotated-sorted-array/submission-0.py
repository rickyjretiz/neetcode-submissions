class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        # Create while loop and find mid.

        while left <= right:
            mid = (left + right)//2

            # Is my target mid?

            if nums[mid] == target:
                return mid

            # Is my left half sorted?

            if nums[left] <= nums[mid]:

                # If yes, is the target in the left half of set?

                if nums[left] <= target < nums[mid]:

                    # If yes, go left. Set right to mid - 1

                    right = mid - 1
                else:

                    # If no, go right. Set left to mid + 1

                    left = mid +1

                # left wasn't sorted, so right is sorted

            else:

                # Is target in right half of set?

                if nums[mid] < target <= nums[right]:

                    # 

                    left = mid + 1

                else:
                    right = mid -1

        return -1



