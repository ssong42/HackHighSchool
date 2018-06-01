# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    overloading.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ssong <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/05/28 13:08:42 by ssong             #+#    #+#              #
#    Updated: 2018/05/28 13:14:24 by ssong            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Square:
	def __init__(self, side):
		self.side = side
	
# special method for add function
	def __add__(squareOne, squareTwo):
		return ((4 * squareOne.side) + (4 * squareTwo.side))	

squareOne = Square(5)
squareTwo = Square(10)
print("Sum of sides of both the squares = ", squareOne + squareTwo)

