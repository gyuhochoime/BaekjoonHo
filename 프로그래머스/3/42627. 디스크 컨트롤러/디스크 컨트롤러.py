import heapq
def solution(jobs):
    heap = []
    jobs.sort()
    time = 0
    tot = 0
    idx = 0
    while idx < len(jobs) or heap:
        while idx < len(jobs) and jobs[idx][0] <= time:
            st, et = jobs[idx]
            heapq.heappush(heap, (et, st))
            idx += 1
        if heap:
            et, st = heapq.heappop(heap)
            time += et
            tot += time - st
        else:
            time = jobs[idx][0]
    return tot // len(jobs)