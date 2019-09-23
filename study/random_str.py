import random, string  # 调用random、string模块
# src_digits = string.digits              #string_数字
# src_uppercase = string.ascii_uppercase  #string_大写字母
# src_lowercase = string.ascii_lowercase  #string_小写字母
def random_str(n):
    ran_str = ''.join(random.sample(string.ascii_uppercase + string.digits, n))
    return ran_str
def random_vin():
    # 内容的权值
	content_map = {
	    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
	    'F': 6, 'G': 7, 'H': 8, 'I': 0, 'J': 1, 'K': 2, 'L': 3,
	    'M': 4, 'N': 5, 'O': 0, 'P': 7, 'Q': 8, 'R': 9, 'S': 2, 'T': 3,
	    'U': 4, 'V': 5, 'W': 6, 'X': 7, 'Y': 8, 'Z': 9, "0": 0, "1": 1,
	    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
	}
	# 位置的全值
	location_map = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
	vin = ''.join(random.sample('0123456789ABCDEFGHJKLMPRSTUVWXYZ', 17))
	num = 0
	for i in range(len(vin)):
	    num = num + content_map[vin[i]] * location_map[i]
	vin9 = num % 11
	if vin9 == 10:
	    vin9 = "X"
	list1 = list(vin)
	list1[8] = str(vin9)
	vin = ''.join(list1)
	return vin
def random_mobile():
    arr=['131','130','132','133','134','135','136']
    num1=random.choice(arr)
    arr1=['0','1','2','3','4','5','6','7','8','9']
    num2=''.join(random.choice('0123456789') for i in range(8))
    mobile=num1+num2
    return mobile

if __name__ == '__main__':
    print(random_vin())
