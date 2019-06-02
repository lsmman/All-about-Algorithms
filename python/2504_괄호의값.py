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
        else :
            return self[-1]

stack = Stack()

mul_depth = 1
total_sum = 0
impossible = 0
leng = len(input_data)

for idx in range(leng):
  brk = input_data[idx]
  if brk.__eq__("("):
    mul_depth = mul_depth * 2
    stack.push(brk)
  elif brk.__eq__("["):
    mul_depth = mul_depth * 3
    stack.push(brk)
  elif brk.__eq__(")"):
    if input_data[idx-1].__eq__('('):
        total_sum += mul_depth
    if stack.peek().__eq__("("):
        mul_depth = mul_depth / 2
        stack.pop()
    else : 
        impossible = 1
        break
  elif brk.__eq__("]"):
    if input_data[idx-1].__eq__('['):
        total_sum += mul_depth
    if stack.peek().__eq__("["):
        mul_depth = mul_depth / 3
        stack.pop()
    else : 
        impossible = 1
        break
if (stack.is_empty == 0) or impossible:
    print(0)
else :
    print(int(total_sum))

  


# 2*(2+3*3)+2*3