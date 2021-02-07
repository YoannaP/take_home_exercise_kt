import operator

class Calculator:
    OPERATORS = {
        "+": operator.add, "-": operator.sub,
        "*": operator.mul, "/": operator.truediv
    }
    pass

class PrefixCalculator(Calculator):
    """
    Class to evaluate infix notation expression.
    """
    def __init__(self):
        self.stack = []

    def evaluate(self, expression):
        """
        Evaluates the expression in prefix notation.

        Parameters
        ----------
        expression (str): Prefix notation string to evaluate.

        Returns
        -------
        output (int): Evaluated result of prefix string.
        """

        #make input into a list, removing ' ', and reverse for iteration
        expression_lst = expression.split()
        expression_lst.reverse()

        for s in expression_lst:
            if s not in self.OPERATORS.keys():
                self.stack.append(s)
            else:
                # if you run into an operator - evaluate last two stack elems
                eval = self.OPERATORS[s](int(self.stack[-1]), int(self.stack[-2]))

                # remove the evaluated stack elems and replace with result
                self.stack.pop()
                self.stack.pop()
                self.stack.append(eval)

        # result is last/only left element in stack - convert to integer
        print(self.stack)
        return self.stack[0]


class InfixCalculator(Calculator):
    """
    Class to evaluate expression with infix notation.
    """
    PRECEDENCE = {'+':2, '-':2, '*':1, '/':1}
    BRACKETS = ['(', ')']

    def __init__(self):
        self.operators = []
        self.operands = []

    def evaluate(self, expression):
        """
        Evaluates expression in infix notation.
        """
        expression_lst = expression.split()

        for s in expression_lst:
            if s not in self.OPERATORS.keys() and s not in self.BRACKETS:
                self.operands.append(s)

            elif s in self.OPERATORS.keys():
                if len(self.operators)==0:
                    self.operators.append(s)

                else:
                    if self.operators[-1]=='(':
                        self.operators.append(s)
                    elif self.PRECEDENCE[s] <= self.PRECEDENCE[self.operators[-1]]:
                        self.operators.append(s)
                    else:
                        # Exception for when self.operators is empty and throws an error
                        try:
                            precedence_check = self.PRECEDENCE[s] <= self.PRECEDENCE[self.operators[-1]]
                        except:
                            precedence_check = False
                        while True:
                            if len(self.operators)==0 or precedence_check:
                                self.operators.append(s)
                                break
                            self._pop_and_push()
            elif s=='(':
                self.operators.append(s)
            elif s==')':
                while True:
                    if self.operators[-1]=='(':
                        self.operators.pop()
                        break
                    else:
                        self._pop_and_push()

        while len(self.operators)!=0:
            self._pop_and_push()

        return self.operands[0]


    def _pop_and_push(self):
        """
        Pops last two elements, A, B in operands and last element in operator X
        Appends to operands B X A.
        """
        print(self.operands)
        l_operand, sl_operand = self.operands[-1], self.operands[-2]
        l_operator = self.operators[-1]

        self.operators.pop()
        self.operands.pop()
        self.operands.pop()

        eval = int(self.OPERATORS[l_operator](int(sl_operand), int(l_operand)))
        self.operands.append(str(eval))

        return


if __name__=='__main__':
    prefixCalc = InfixCalculator()
    res = prefixCalc.evaluate('( ( ( 4 - 2 ) * 4 ) + 3 )')
    print(res)
