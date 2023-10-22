class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left , right = k,k
        minVal = nums[k] #only one element, must be minimum
        maxScore = minVal #length is one, so the score is itself

        while left> 0 or right<len(nums)-1:
            if left == 0 or (right<len(nums)-1 and nums[right+1]>nums[left-1]):
                #when there are no more left elements, we have to go to right
                #Or, the next right one is greater than the next left one, keep in mind that left-1 is expanding to the left
                right +=1
            else:
                # with all conditions not satisfied, we expand to the left
                left -=1
            minVal = min(minVal, nums[left],nums[right]) # when a new element is added, the min is either the original one, or the added one
            maxScore = max(maxScore, minVal*(right - left+1))
        return maxScore
