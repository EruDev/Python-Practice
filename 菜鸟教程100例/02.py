"""
题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
"""
while True:

	profit = int(input('请输入利润:'))

	if profit < 100000:
		bonus = 0.1 * profit
	elif profit >= 100000 and profit < 200000:
		bonus = 100000*0.1 + 0.075*(profit-100000)
	elif profit >= 200000 and profit < 400000:
		bonus = 100000*0.1 + 100000*0.075 + (profit-200000)*0.05
	elif profit >= 400000 and profit < 600000:
		bonus = 100000*0.1 + 100000*0.075 + 200000*0.05 + (profit-400000)*0.03
	elif profit >= 600000 and profit < 1000000:
		bonus = 100000*0.1 + 100000*0.075 + 200000*0.05 + 200000*0.03 + (profit-600000)*0.015
	elif profit >= 1000000:
		bonus = 100000*0.1 + 100000*0.075 + 200000*0.05 + 200000*0.03 + 400000*0.015 + (profit-1000000)*0.01
	else:
		print('输入有误')

	print(bonus)


