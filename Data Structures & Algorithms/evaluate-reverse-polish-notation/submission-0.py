class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        n = len(tokens)

        for i, token in enumerate(tokens):
            if token in {"+", "-", "*", "/"}:
                b = st.pop()  # Pop second operand
                a = st.pop()  # Pop first operand

                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                elif token == '/':
                    res = int(a / b)
                st.append(res)
            else:
                st.append(int(token))

        return st[0]


            



