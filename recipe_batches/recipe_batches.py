#!/usr/bin/python

import math

# Firt Pass
# Just check if all of the values of the of the inputs are less than the available outputs
# 

def recipe_batches(recipe, ingredients):
    recipe_copy = recipe.copy()
    ing_copy = ingredients.copy()

    # Go ahead and check if any ingredients are missing
    for rec_ing in recipe_copy.keys():
      if(not rec_ing in ing_copy or ing_copy[rec_ing] < recipe_copy[rec_ing]):
        return 0

    batches = []
    for rec_ing, need in recipe_copy.items():
      batches.append(math.floor(ing_copy[rec_ing] // need))
    
    return min(batches)  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))