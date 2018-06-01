# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    initmethod.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ssong <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/05/27 10:49:23 by ssong             #+#    #+#              #
#    Updated: 2018/05/27 10:58:41 by ssong            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Employee:
    def __init__(self, name):
        self.name = name

    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee("Mark")
employee2 = Employee("Mathew")
employee.displayEmployeeDetails()
employee2.displayEmployeeDetails()
