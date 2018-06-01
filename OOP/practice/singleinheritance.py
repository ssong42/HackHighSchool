# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    singleinheritance.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ssong <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/05/28 10:17:55 by ssong             #+#    #+#              #
#    Updated: 2018/05/28 10:30:48 by ssong            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# BASE CLASS
class Apple:
	manufacturer = "Apple Inc."
	website = "www.apple.com/contact"

	def contactDetails(self):
		print("To contact us log on to",self.website)
	
# DERIVED CLASS
class Macbook(Apple):
	def __init__(self):
		self.yearOfManufacture = 2017
	
	def manufacturerDetails(self):
		print("This Macbook was manufactured in the year {} by {}".format(self.yearOfManufacture, self.manufacturer))
	
macBook = Macbook()
macBook.manufacturerDetails()
macBook.contactDetails()
