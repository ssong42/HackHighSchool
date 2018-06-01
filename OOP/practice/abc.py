# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    abc.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ssong <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/05/28 13:14:30 by ssong             #+#    #+#              #
#    Updated: 2018/05/28 13:21:46 by ssong            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABCMeta, abstractmethod

#Abstract Base Class

class Shape(metaclass = ABCMeta):
	@abstractmethod
	def area(self):
		return 0

class Square(Shape):
	side = 4
	def area(self):
		print("AREa of square: ", self.side * self.side)

class Rectangle(Shape):
	width = 5
	length = 10
	def area(self):
		print("AREa of rectangle: ", self.width * self.length)

square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()
