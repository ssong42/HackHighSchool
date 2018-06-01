# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    accessSpecifiers.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ssong <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/05/28 10:53:26 by ssong             #+#    #+#              #
#    Updated: 2018/05/28 11:12:07 by ssong            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Public => memberName
# Protected => _memberName
#	use only within this class and derived class and nowhere else
# Private => __memberName
#	use only within that class and nowhere else
# 	the double underscore stores the attribute like this
#		_Class__nameofattribute
#Just Naming convention and nothing else

class Car:
	numberOfWheels = 4
	_color = "Black"
	__year = 2017 	# _Car__year

class BMW(Car):
	def __init__(self):
		print("Protected attribute color: ", self._color)

car = Car()
print("Public attribute numberofWheels: ", car.numberOfWheels)
bmw = BMW()
print("Private attribute __year: ", car.__year)
