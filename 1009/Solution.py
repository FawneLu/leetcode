class Solution:
    def bitwiseComplement(self, N: int) -> int:
        new_N=""
        for i in bin(N)[2:]:
            if i=="1":
                i="0"
            else:
                i="1"
            new_N+=i
        return int(new_N,2)