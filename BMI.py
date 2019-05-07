height = input('您的身高')
weight = input('您的體重')
composition = input('您的體指率')
height = int(height) 
weight = int(weight) 
composition = int(composition)

BMI = weight/(height/100*height/100)
print('您的BMI:', BMI)