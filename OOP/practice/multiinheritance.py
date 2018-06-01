# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multiinheritance.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ssong <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/05/28 10:32:05 by ssong             #+#    #+#              #
#    Updated: 2018/05/28 10:42:23 by ssong            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class OperatingSystem:
	multitasking = True
	name = "Mac OS"

class Apple:
	website = "www.Apple.com"
	name = "Apple"

# if there is a conflicting variable with the same name
# The first inheritance gets called first with that name
class Macbook(Apple, OperatingSystem):
	def __init__(self):
		if self.multitasking is True:
			print("This is a multitasking system. Visit {} for more details".format(self.website))
			print("Name :", self.name)

macBook = Macbook()


