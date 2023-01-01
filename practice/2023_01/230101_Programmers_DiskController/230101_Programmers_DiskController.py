from heapq import heapify, heappush, heappop

def solution(jobs):
    len_jobs = len(jobs)
    jobs_count = 0
    current_time = 0
    total_time = 0
    
    wait_queue = []

    heapify(jobs)
    heapify(wait_queue)
    
    while jobs_count < len_jobs:
        if jobs:
            if not wait_queue and jobs[0][0] > current_time:
                job = heappop(jobs)
                heappush(wait_queue, [job[1], job[0]])
                current_time = job[0]
            else:
                while jobs and jobs[0][0] <= current_time:
                    job = heappop(jobs)
                    heappush(wait_queue, [job[1], job[0]])

        current_job = heappop(wait_queue)
        total_time += current_job[0] + current_time - current_job[1]
        current_time += current_job[0]
        jobs_count += 1
    
    return total_time // len_jobs