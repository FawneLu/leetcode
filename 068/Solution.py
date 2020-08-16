class Solution:
    def fullJustify1(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        cur=[]
        count=0
        
        for word in words:
            if count+len(word)+len(cur)>maxWidth:
                for i in range(maxWidth-count):
                    cur[i%(len(cur)-1 or 1)]+=' '
                
                res.append(''.join(cur))
                cur=[]
                count=0
            
            cur+=[word]
            count+=len(word)
        
        res.append(' '.join(cur).ljust(maxWidth))
        
        return res


    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def textJustify(left, right, words, maxwidth):
            if right - left == 0:
                return words[left] + fillSpace(maxwidth - len(words[left]))

            isLastLine = right == len(words) -1 

            tmp_words = words[left:right+1]
            words_len = getlen(tmp_words)
            space_total = maxwidth - words_len
            space_word = len(tmp_words) - 1
            space_avg = " " if isLastLine else fillSpace(space_total // space_word)
            space_remain = 0 if isLastLine else space_total % space_word

            res = ""

            for i in range(len(tmp_words) - 1):
                res += tmp_words[i]
                res += space_avg
                res += " " if space_remain > 0 else ""
                space_remain -= 1

            res += tmp_words[-1]
            res += fillSpace(maxwidth - len(res))

            return res

        def findRight(left, words, maxwidth):
            right = left
            char_total  = len(words[right])
            right += 1
            while right < len(words) and char_total + len(words[right]) + 1 <= maxwidth:
                char_total += len(words[right]) + 1
                right += 1
            return right - 1


        def fillSpace(n):
            ans = ""
            for i in range(n):
                ans += " "
            return ans


        def getlen(words):
            count = 0
            for word in words:
                count += len(word)
            return count
        
        
        left = 0
        res = []
        while left < len(words):
            right = findRight(left, words, maxWidth)
            res.append(textJustify(left, right, words, maxWidth))
            left = right + 1
        return res