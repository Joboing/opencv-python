import collections


class Solution:

    def groupAnagrams(self, strs):
        hash_list = {}
        for i in strs:
            key = tuple(sorted(i))
            if key not in hash_list:
                hash_list[key] = []
                hash_list[key].append(i)
            else:
                hash_list[key].append(i)
        return list(hash_list.values())

if __name__ == '__main__':
    a = Solution()
    a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))