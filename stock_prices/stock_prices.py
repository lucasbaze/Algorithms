#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # list to hold all calculations
  max_profits = []

  for x in range(0, len(prices) - 1):
    # Check if the left number is less then right number
    # if true, skip it because we don't want negative profits
    if(prices[x] > prices[x + 1]):
      continue

    for y in range(x, len(prices) - 1):
      max_profits.append(prices[y] - prices[x])
  
  return max(max_profits)




if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))