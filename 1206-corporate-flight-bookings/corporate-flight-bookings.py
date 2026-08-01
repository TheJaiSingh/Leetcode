class Solution(object):
    def corpFlightBookings(self, bookings, n):
        arr=[0]*n
        def update(arr,left,right,seat):
            arr[left]+=seat
            if right+1<len(arr):
                arr[right+1]-=seat
            
        for frist,last,seat in bookings:
            left=frist-1
            right=last-1
            update(arr,left,right,seat)
        answer=[0]*n
        answer[0]=arr[0]
        for right in range(1,len(arr)):
            answer[right]=arr[right]+answer[right-1]
        return answer
