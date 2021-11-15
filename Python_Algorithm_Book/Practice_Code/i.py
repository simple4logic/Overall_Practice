from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let: List[str] = []
        dig: List[str] = []
        for a in logs:
            if a.split()[1].isdigit(): #in other words, when letter log
                dig.append(a)
            else:
                let.append(a)

        let.sort(key=lambda x:(x.split()[1], x.split()[0]))
        return let+ dig
            

#for testing
s = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
s.reorderLogFiles(logs)