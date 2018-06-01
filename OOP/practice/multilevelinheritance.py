# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multilevelinheritance.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ssong <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/05/28 10:48:32 by ssong             #+#    #+#              #
#    Updated: 2018/05/28 10:52:03 by ssong            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class MusicalInstruments:
	numberofMajorKeys = 12

class StringInstruments(MusicalInstruments):
	typeOfWood = "Tonewood"

class Guitar(StringInstruments):
	def __init__(self):
		self.numberOfStrings = 6
		print("This guitar consists fo {} strings. It is made of {} and it can play {} keys".format(self.numberOfStrings, self.typeOfWood, self.numberofMajorKeys))

guitar = Guitar()
