# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    diamond.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ssong <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/05/28 11:31:48 by ssong             #+#    #+#              #
#    Updated: 2018/05/28 11:40:55 by ssong            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class A:
	def method(self):
		print("This Method belongs to class A")
	pass

class B(A):
	def method(self):
		print("This Method belongs to class B")
	pass

class C(A):
	def method(self):
		print("This Method belongs to class C")
	pass

class D(B, C):
	pass

d = D()
d.method()
