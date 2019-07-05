# 강사님이 풀어주신 것

def baedal(a, k):
   def print_line(width, count):
       print(('+' + '-' * width) * count + '+')

   def print_num(width, num):
       print('|' + ' ' * (width - len(str(num))) + str(num), end='')

   max_width = len(str(max(a)))
   for i in range(len(a)):
       if i % k == 0:
           print_line(max_width, k)
       print_num(max_width, a[i])
       if i % k == k-1:
           print('|')
   if len(a) % k != 0:
       print('|')
       print_line(max_width, len(a) % k)
   if len(a) % k == 0:
       print_line(max_width, k)


baedal([1, 15, 326, 17, 672, 1000, 1, 2], 2)
