import math;

max_range=raw_input('Please input a range,then we will output all prime numbers:');

output = '1 2 3'
i = 5;
while i <= int(max_range):
      j = 2;
      while j <= int(math.sqrt(i)):
            if i%j != 0 and j == int(math.sqrt(i)):
               output = output + ' ' + str(i);
               break;
            elif i%j == 0:
               break;
            else:
               j += 1;
      i+=1;

print output

