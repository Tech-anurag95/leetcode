from collections import Counter

class Solution:
    def characterReplacement(self,s:str,k:int)->int:
        left=0
        count=Counter()
        max_freq=0
        bda=0
        for right in range(len(s)):    #saare element ko consider krenge 
            count[s[right]]+=1         #jaise hi wo element window me ghusa usi frequency ko 1 bdha denge 
            max_freq=max(max_freq,count[s[right]])   #current max frequency ko consider krenge 
            while right-left+1-max_freq>k:   #jitne element change kr skte hain wo agar k se bda ho jayega to humko windoiw size chota krna pdega n 
                count[s[left]]-=1  #jo element nikalenge uski count ko 1 kam kr denge 
                left+=1   #window ko choti kr denge 
            bda=max(bda,right-left+1)  #valid max length window ko consider krenge 
        return bda