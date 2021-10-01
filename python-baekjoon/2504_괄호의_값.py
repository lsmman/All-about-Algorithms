input_data = input()
# input_data = "(()[[]])([])"


class Stack(list):
    push = list.append

    def is_empty(self):
        if not self:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return ""
        else:
            return self[-1]


stack = Stack()

mul_depth = 1
total_sum = 0
impossible = 0
s = 0
l = 0
leng = len(input_data)

for idx in range(leng):
    brk = input_data[idx]
    if brk.__eq__("("):
        s += 1
        mul_depth = mul_depth * 2
        stack.push(brk)

    elif brk.__eq__("["):
        l += 1
        mul_depth = mul_depth * 3
        stack.push(brk)

    elif brk.__eq__(")"):
        s -= 1
        if not stack.peek().__eq__("("):
            impossible = 1
            break

        if input_data[idx - 1].__eq__("("):
            total_sum += mul_depth

        mul_depth = mul_depth / 2
        stack.pop()

    elif brk.__eq__("]"):
        l -= 1
        if not stack.peek().__eq__("["):
            impossible = 1
            break

        if input_data[idx - 1].__eq__("["):
            total_sum += mul_depth

        mul_depth = mul_depth / 3
        stack.pop()

if (stack.is_empty == 0) or impossible or l or s:
    print(0)
else:
    print(int(total_sum))
