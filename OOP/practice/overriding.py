# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    overriding.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ssong <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/05/28 11:19:39 by ssong             #+#    #+#              #
#    Updated: 2018/05/28 11:30:47 by ssong            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Employee:
	def setNumberOfWorkingHours(self):
		self.numberOfWorkingHours = 40
	
	def displayNumberOfWorkingHours(self):
		print(self.numberOfWorkingHours)

#overriding same name as base class method, but will change the function
#super(). superFUNCTIONN!! will call the base class method.

class Trainee(Employee):
	def setNumberOfWorkingHours(self):
		self.numberOfWorkingHours = 45
	
	def resetNumberOfWorkingHours(self):
		super().setNumberOfWorkingHours()

employee = Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours of employee: ", end = ' ')
employee.displayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of trainee: ", end = ' ')
trainee.displayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print("Number of working hours of trainee: ", end = ' ')
trainee.displayNumberOfWorkingHours()
