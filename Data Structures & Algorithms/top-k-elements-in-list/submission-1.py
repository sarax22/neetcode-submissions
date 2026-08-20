class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]   #only has to be as big as the number of numbers there is

        for num in nums:
            count[num] = 1 + count.get(num, 0)      #increment count each time we see that number
        
        for num, c in count.items():
            freq[c].append(num)                 #num occurs c number of times (index = freq, value = n)

        res = []
        for i in range(len(freq) - 1, 0, -1):        #going from the top down to get top k frequent items
            for num in freq[i]:                                 
                res.append(num)     

                if len(res) == k:                   #only appends k times
                    return res
