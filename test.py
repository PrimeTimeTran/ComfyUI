# import math
# # prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
# prime_numbers = [7, 11]

# def isPrime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, math.isqrt(n) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# def isPrime(n):
#   limit = math.floor(math.sqrt(n))
#   for i in range(2, limit):
#     if (n % i) == 0:
#       return False
#   return True

# def isPrime(n):
#   factors = [n for n in range(2, n)]
#   factors2 = [n for n in range(2, n)]
#   for i in factors2:
#     if n % i != 0:
#       factors.remove(i)
#   if len(factors) > 0:
#     return False
#   return True

# def isPrime(n):
#   for i in range(1, n+1):
#     if i != 1 and i != n and (n % i) == 0:
#       return False
#   return True

# def check_primes(nums):
#   for n in nums:
#     if isPrime(n):
#       print('Prime', n)
#     else: 
#       print('Not Prime', n)

# check_primes(prime_numbers)

def create_staircase(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

# print(create_staircase([1,2,3,4,5,6]))
# print(create_staircase([1,2,3,4,5,6,7]))

from collections import Counter 

store = {}

def map_lines(line):
  value = line.split()
  store[value[0]] = value[1]

def read_file(filename):
  with open(filename, 'r') as file:
    file_contents = file.read()
  return file_contents

def generate_cipher(filename):
  with open(filename, 'r') as file:
    for line in file:
      map_lines(line)

def generate_triangle():
  counter = Counter(store)
  sorted_words = sorted(counter.items(), key=lambda x: int(x[0]))
  words = []
  for _, value in sorted_words:
    words.append(value)

  step = 1
  rows = []
  while len(words) != 0:
    if len(words) >= step:
      rows.append(words[0:step])
      words = words[step:]
      step += 1
  return rows

def decode(input):
  generate_cipher(input)
  rows = generate_triangle()
  resp = ' '.join(r[-1] for r in rows)
  return resp

encoded = 'coding_qual_input.txt'
print(decode(encoded))

