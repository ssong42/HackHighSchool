# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    staticmethodandinstancemethod.py                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ssong <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/05/27 10:42:25 by ssong             #+#    #+#              #
#    Updated: 2018/05/27 10:48:15 by ssong            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Employee:
    def employeeDetails(self):
        self.name = "Ben"

    @staticmethod
    def welcomeMessage():
        print("Welcome to our organization!")

employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()
