'''
An array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

def maxProfit(prices):
	profit = 0
	buy = float('inf')
	for i in range(len(prices)):
		if prices[i] < buy:
			buy = prices[i]		#iterate to get the lowest val
		else:
			profit = max(profit, prices[i] - buy)
	return profit


if __name__ == "__main__":
	prices= [7,1,5,3,6,4]
	result = maxProfit(prices)
	print(prices)
	print("Maximum profit = " +str(result))

