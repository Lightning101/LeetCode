class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1=m-1
        p2 = n-1
        idx = (m+n)-1
        
        while(p1 != -1 and p2 != -1):
            if(nums1[p1] >= nums2[p2]):
                nums1[idx] = nums1[p1]
                p1-=1 
            else:
                nums1[idx] = nums2[p2]
                p2-=1 
            idx-=1

        if(p1 == -1):
            nums1[0:idx+1] = nums2[:p2+1]
        
        if(p2 == -1):
            nums1[0:idx+1] = nums1[:p1+1]
            

        return nums1
    
s = Solution()

# print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))
# print(s.merge([1],1,[],0))
print(s.merge([0],0,[1],1))