import math

def addition(a, b):
	return a+b

def add1(num):
	return num+1

def tri_area(base, height):
	return (base*height)/2

def next_edge(side1, side2):
	return (side1 + side2)-1

def remainder(x, y):
	return x%y

def string_int(txt):
	return int(txt)

def find_perimeter(length, width):
	return (length+width)*2

def sum_polygon(n):
	return (n-2)*180

def calculate_exponent(num, exp):
	return num**exp

def squared(b):
	return b*b

def to_int(txt):
	return int(txt)

def to_str(num):
	return str(num)

def concat(lst1, lst2):
	return lst1+lst2

def is_seven(x):
	return x==7

def swap(a, b):
	b1 = a
	a1 = b
	return [a1, b1]

def is_same_num(num1, num2):
	return num1 == num2

def less_than_or_equal_to_zero(num):
	return num<=0

def mod(m, n):
	return m%n

def even_or_odd(lst):
	if sum(lst)%2==0:
		return "even"
	else:
		return "odd"

def findLargestNum(nums):
	return sorted(nums)[-1]

def find_smallest_num(lst):
	return sorted(lst)[0]

def difference_max_min(lst):
	sm = sorted(lst)[0]
	bg = sorted(lst)[-1]
	return bg-sm

def difference(nums):
	bg = sorted(nums)[-1]
	sm = sorted(nums)[0]
	return bg-sm

def less_than_100(a, b):
	return (a+b)<100

def divisible_by_five(n):
	return n%5==0

def get_sum_of_elements(lst):
	return sum(lst)

def divisible(num):
	return num%100==0

def k_to_k(n, k):
	return k**k==n

def max_num(n1, n2):
	if n1 > n2:
		return n1
	else:
		return n2

def divides_evenly(a, b):
	return a%b==0

def makes10(a, b):
	if a==10 or b==10 or (a+b)==10:
		return True
	else:
		return False

def sum_lst(lst):
	return sum(lst)

def nth_even(n):
	return (n*2)-2

def return_negative(n):
	if n <= 0:
		return n
	else:
		return n-(n*2)

def list_less_than_100(lst):
	return sum(lst)<100

def make_pair(num1, num2):
	return [num1, num2]

def years_in_one_house(age, moves):
	return math.floor((age/(moves+1))+0.5)

def clean_up_list(lst):
	lst1 = []
	lst2 = []
	for i in lst:
		if int(i)%2==0:
			lst1.append(int(i))
		else:
			lst2.append(int(i))
	return [lst1, lst2]

def check_equals(lst1, lst2):
	return lst1 == lst2

is_even = lambda n : n % 2 == 0

calculator = lambda txt: eval(txt)

def is_odd(num):
  return num%2 != 0

def sum_cubes(n):
	lst = []
	num = 0
	for i in range(0,n):
	    num += 1
	    lst.append(num**3)
	return sum(lst)

def invert_list(lst):
	lsty=[]
	for i in lst:
		lsty.append(-i)
	return lsty

def range_of_num(start, end):
	lst=[]
	num=start
	for i in range(0,(end-start)):
		num+=1
		lst.append(num)
	return lst[:-1]

def print_list(n):
	result=[]
	i=0
	while i<n:
		i+=1
		result.append(i)
	return result

def isEvenOrOdd(num):
	if num%2==0:
		return "even"
	else:
		return "odd"

def equation(s):
	return eval(s)

def sum_five(lst):
	listy=[]
	for i in lst:
		if i>5:
			listy.append(i)
	return sum(listy)

def basic_calculator(a, o, b):
	if (o=='/' or o=='*') and b==0:
		return None
	elif o not in '/-*+':
		return None
	else:
		return eval(str(a)+o+str(b))

def eq(evaluate):
	return eval(evaluate)

def area_shape(base, height, shape):
	if shape == "triangle":
		return base * height * 0.5
	elif shape == "parallelogram":
		return base * height 

def half_quarter_eighth(n):
	lst = []
	lst.append(n*0.5)
	lst.append(n*0.25)
	lst.append(n*0.125)
	return lst

def min_max(nums):
	return [min(nums), max(nums)]

def greater_than_one(frac):
	return eval(frac)>1

def invert_list(lst):
    lsty=[]
    if len(lst)>0:
        for i in lst:
            lsty.append(-i)
    return lsty

def operate(num1, num2, operator):
	return eval(str(num1)+operator+str(num2))

def shuffle(nums, n):
    lst1=nums[:n]
    lst2=nums[n:]
    lst=[]
    y=0
    for i in lst1:
        lst.append(lst1[y])
        lst.append(lst2[y])
        y=y+1
    return lst
