import sys
class Xor:
    XorKey=[0xB3, 0x19, 0xB9, 0x51, 0x91, 0x1D, 0x43, 0x47]
    def __init__(self):
        pass
    @classmethod
    def enc(self,src):
        j,result=0,""
        bt=bytes(src,'ascii')
        h=len(bt)
        for i in range(h):
           result=result+hex(bt[i]^(self.XorKey[j]))[2:]
           j=(j+1)%8
        return result
a=Xor()
print(a.enc(sys.argv[1]))
