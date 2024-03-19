from collections import OrderedDict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        tasks_counter = Counter(tasks)
        for task, count in tasks_counter.items():
            heappush(heap, (0, -count, task))

        time = 0
        while heap:
            min_time, count, task = heappop(heap)
            if min_time > time:
                heappush(heap, (min_time, count, task))
            else:
                if count < -1:
                    min_time += n+1
                    count += 1
                    heappush(heap, (min_time, count, task))
            time += 1
        return time
        
        