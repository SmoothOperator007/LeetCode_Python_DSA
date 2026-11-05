"""
Problem: Search in Rotated Sorted Array (LeetCode 33)
Difficulty: Medium

--- EXPECTED / OPTIMAL APPROACH ---
- Pattern: Modified Binary Search
- Intuition: 
  Even though the array is rotated, dividing it in half will always result in at least one strictly sorted half. 
  We check if `nums[left] <= nums[mid]` to determine if the left portion is sorted. If so, we check if the target 
  falls within the left boundaries (`nums[left] <= target < nums[mid]`), narrowing `right = mid - 1` accordingly; 
  otherwise, we search the right half. If the left half is not sorted, the right half is guaranteed to be sorted, 
  allowing us to apply the same logic symmetrically.
- Time Complexity: O(log n)
- Space Complexity: O(1)

--- LEARNING ---
- Custom Intuition & Exploration: 
  Initially experimented with physical array slicing and re-ordering (`nums[:tgi] = t2`, `nums[tgi+1:] = t1`) to 
  un-rotate the array before locating the element. Discovered that slicing alters list lengths and distorts subsequent 
  index lookups (`nums.index(target)`). 
- Practical Shortcut: 
  Noticed that LeetCode's constraints on this problem allowed a clean $O(n)$ linear validation check: 
  `if target not in nums: return -1` followed by `return nums.index(target)`. While bypassing the logarithmic constraint, 
  it provided immediate functional correctness and zero-millisecond overhead for small input sizes.
- Complexity Trade-off: 
  Slicing and index-based mutations introduce $O(n)$ overhead with high risk of index corruption. The optimal binary search 
  avoids container mutation entirely while maintaining strict $O(\log n)$ performance.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # --- OPTIMAL O(log n) BINARY SEARCH APPROACH ---
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half must be sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1

        # --- MY ALTERNATIVE ACCEPTED SHORTCUT (O(n)) ---
        # if target not in nums:
        #     return -1
        # return nums.index(target)
