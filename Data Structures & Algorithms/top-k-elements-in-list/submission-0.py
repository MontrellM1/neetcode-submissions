from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = defaultdict(int)


        for n in nums:
            d[n] += 1

        l = sorted((d.items()), reverse=True, key=lambda value:value[1])
        output = []

        for i in range(k):
            val = l[i][0]
            output.append(val)
        return output
        

        


       



       
    
      
            
            