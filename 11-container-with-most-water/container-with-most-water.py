class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        final_area=0
        #conditon
        while left<right:
            width=right-left
            length=min(height[left],height[right])
            area=width*length
            if area>final_area:
                final_area=area
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return final_area
        