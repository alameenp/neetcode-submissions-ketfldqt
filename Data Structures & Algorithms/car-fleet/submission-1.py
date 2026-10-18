class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count_fleets = len(position)
        combined = sorted([list(item) for item in zip(position,speed)],reverse=True)
        stack = []
        for item in combined:
            time = (target - item[0])/item[1]
            item.append(time)

        for i in combined:
            if not stack:
                stack.append(i[2])

            elif i[2] > stack[-1]:
                stack = []
                stack.append(i[2])
            else:
                slow = stack.pop()
                stack.append(i[2])
                stack.append(slow)
                count_fleets-=1
        return count_fleets


        

        

        
        