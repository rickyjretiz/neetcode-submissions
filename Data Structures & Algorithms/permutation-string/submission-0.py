class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)

        window_size = len(s1)

        window_count = Counter(s2[:window_size])

        if s1_count == window_count:
            return True

        for i in range(window_size, len(s2)):

            window_count[s2[i]] += 1

            left_char = s2[i -  window_size]

            window_count[left_char] -= 1

            if window_count[left_char] == 0:
                del window_count[left_char]

            if s1_count == window_count:
                return True

        return False



