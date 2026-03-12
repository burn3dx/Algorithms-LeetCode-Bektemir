class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for ch in s:
            if ch in '([{':
                st.append(ch)
            else:
                if not st:
                    return False
                top=st.pop()
                if top!=pairs[ch]:
                    return False

        return len(st)==0