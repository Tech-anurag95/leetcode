class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map=defaultdict(list) #creates a dictionary where every new key automatically gets an empty list []
        for word in strs:
            sorted_word =''.join(sorted(word)) #ye uss word ko sort krega join krega aur sorted word bnayega 
            anagram_map[sorted_word].append(word) #agar key phle se hui to uske value ke list me append kr dega word ko aur agar nhi hui to nya list bna dega with key=sorted word and value = anagram
        return list(anagram_map.values()) #sirf values ko print kra denge


    # class Solution:
    # def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    #     sorted_map = {}
    #     for s in strs:
    #         # Sort the characters to form the key
    #         key = "".join(sorted(s))
    #         # Initialize key in dictionary if not present
    #         if key not in sorted_map:
    #             sorted_map[key] = []
    #         # Append the original string to the corresponding list
    #         sorted_map[key].append(s)
    #     # Return the grouped anagram lists
    #     return list(sorted_map.values())


        
        
