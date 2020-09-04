class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(tasks)
        m = max(cnt.values())
        mCnt = 0
        for k in cnt:
            if cnt[k] == m:
                mCnt += 1

        l = len(tasks)
        gapCnt = (m - 1) * (n - (mCnt - 1))

        return max(gapCnt + m * mCnt, len(tasks))
