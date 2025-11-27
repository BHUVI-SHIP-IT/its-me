class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        def back(start,path):
            if len(path)==4:
                if start==len(s):
                    res.append(".".join(path))
                return
            for length in range(1,4):
                if start+length>len(s):
                    break
                part=s[start:start+length]
                if (part.startswith('0') and length >1) or int(part)>255:
                    continue
                back(start+length,path+[part])
                    
        back(0,[])
        return res

        