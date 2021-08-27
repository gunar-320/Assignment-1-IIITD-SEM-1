#Assignment 1 : Gunar Sindhwani : Roll Number-2020199: Group-4|Section- B

#code starts from here!
bulkchoice=''
def show_menu(): #shows menu
	print("=" * 40)
	print(" " * 10 + "MY BAZAAR")
	print("=" * 40)
	print("Hello! Welcome to my Grocery Store!")
	print("Following are the products availaible in the shop:")
	print('')
	print("-" * 40)
	print("CODE | DESCRIPTION | CATEGORY | COST(Rs)")
	print("-" * 40)
	print(''' 
	 0 | Tshirt     | Apparels    | 500
	 1 | Trousers   | Apparels    | 600
	 2 | Scarf      | Apparels    | 250
	 3 | Smartphone | Electronics | 20,000
	 4 | iPad       | Electronics | 30,000
	 5 | Laptop     | Electronics | 50,000
	 6 | Eggs       | Eatables    | 5
	 7 | Chocolate  | Eatables    | 10
	 8 | Juice      | Eatables    | 100
	 9 | Milk       | Eatables    | 45''')
	print('-' * 40)
	print('')
	global bulkchoice   #added global so as to access it from global stackframe in main()
	while bulkchoice != 'y' or bulkchoice != 'Y' or bulkchoice != 'N' or bulkchoice != 'n':
		bulkchoice = input("Would you like to buy in bulk? (y or Y / n or N) :")
		print('')
		if bulkchoice=="Y" or bulkchoice=="N" or bulkchoice=='n' or bulkchoice == 'y':
			break


def get_regular_input():#takes regular input from the user if the user selected N or n
	print("-" * 40)
	print("ENTER THE ITEMS YOU WISH TO BUY")
	print('-' * 40)
	raw_input_list1 = list(map(int, input("Enter the item codes (space-seperated) :").split()))
	quantity_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(len(raw_input_list1)):
		if raw_input_list1[i] >= 0 and raw_input_list1[i] <= 9: #condition that the input values entered by the user should be in the code range of the products and arent negative.
			quantity_list[raw_input_list1[i]] += 1 #increments 1 in quantity list at a position of the code number.
		else:
			print("This Item Code is Invalid ", raw_input_list1[i], "THIS ITEM HAS BEEN SKIPPED!")


	return (quantity_list)


def get_bulk_input(): #takes bulk input from the user if the user entered Y or y in show menu()

		commodity_description = ['T-Shirt', 'Trousers', 'Scarf', 'Smartphone', 'iPad', 'Laptop', 'Eggs', 'Chocolate',
								 'Juice', 'Milk']
		# list for commodity
		commodity_cost = [500, 600, 250, 20000, 30000, 50000, 5, 10, 100, 45]
		# list for commodity pricing corresponding to the index at commodity_description
		print('-' * 40)
		print("ENTER ITEMS AND QUANTITIES")
		print('-' * 40)
		quantities_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #0-9 indexed list with each index value =0 which would be incremented later by the amount of the commodity of the code of commodity entered .
		while True:
			bulk_input_list = list(map(int, input("Enter code and quantity (leave blank to stop):").split()))
			if len(bulk_input_list) == 0:
				print("Your Order has been finalized.")
				print('')
				break
			if (bulk_input_list[0]<0 and bulk_input_list[1]<0) or ((bulk_input_list[0]>=9 or bulk_input_list[0]<0) and bulk_input_list[1]<0):
				print("Invalid Code and Quantity . Try again.")
				print('')
			elif bulk_input_list[0]>9 or bulk_input_list[0]<0:
				print("Invalid Code . Try again.")
				print('')
			elif bulk_input_list[1]<0:
				print("Invalid Quantity . Try again.")
				print('')


			else:  # main condition: prepares list
				quantities_list[bulk_input_list[0]] += bulk_input_list[1] #bulk_input_list[0] represents the code of the commodity . This step adds bulk_input_list[1] which is the quantity of the commodity to the index of the code in quantities list.
				print("You added", bulk_input_list[1], commodity_description[bulk_input_list[0]])
				print('')
		return quantities_list


def print_order_details(quantities):
	print('-' * 40)
	print("ORDER DETAILS")
	print('-' * 40)
	sum=0

	commodity_description = ['T-Shirt', 'Trousers', 'Scarf', 'Smartphone', 'iPad', 'Laptop', 'Eggs', 'Chocolate','Juice','Milk']
# list for commodity
	commodity_cost = [500, 600, 250, 20000, 30000, 50000, 5, 10, 100,45]
# list for commodity pricing corresponding to the index at commodity_description
	serial_number = 1
	for i in range(len(quantities)):
		if (quantities[i]) > 0:
			print('[', serial_number, ']', commodity_description[i], 'X', quantities[i], "= Rs", commodity_cost[i], '*',
				  quantities[i], '= Rs', commodity_cost[i] * quantities[i])
			sum = sum+commodity_cost[i] * quantities[i]
			serial_number = serial_number + 1

	print('')
	print("TOTAL COST = ",sum)
	print('')


def calculate_category_wise_cost(quantities): #this function finds out the category wise cost :apparels , electronics , eatables
	print('-' * 40)
	print("CATEGORY-WISE COST")
	print('-' * 40)
	apparels_count = 0
	electronics_count = 0
	eatables_count = 0
	apparels_cost = 0
	eatables_cost = 0
	electronics_cost = 0

	commodity_cost = [500, 600, 250, 20000, 30000, 50000, 5, 10, 100, 45] #list containing the commodity cost , mentioned in the order as per menu
	apparels_cost = (quantities[0] * commodity_cost[0]) + (quantities[1] * commodity_cost[1]) + (quantities[2] * commodity_cost[2]) #apparels cost are calculated (these lie in the index 0-2 as per menu code)
	electronics_cost = (quantities[3] * commodity_cost[3] + quantities[4] * commodity_cost[4] + quantities[5] *commodity_cost[5])#electronics cost are calculated (these lie in the index 3-5 as per menu code)
	eatables_cost = quantities[6] * commodity_cost[6] + quantities[7] * commodity_cost[7] + quantities[8]*commodity_cost[8] + quantities[9] * commodity_cost[9]#eatables cost are calculated (these lie in the index 6-9 as per menu code)
#below not equal to zero conditions are added so that if any of the category cost is zero , they won't be displayed in the menu
	if apparels_cost != 0:
		print('Apparels = Rs ', apparels_cost)
	if electronics_cost != 0:
		print("Electronics = Rs ", electronics_cost)
	if eatables_cost:
		print("Eatables = Rs ", eatables_cost)
	print('')
	return (apparels_cost, electronics_cost, eatables_cost)



def get_discount(cost, discount_rate): #helper function for calculating discount , takes formal parameters as cost and discount_rate

	return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost): #calculates the discounted price of each category
	print('-'*40)
	print("DISCOUNTS")
	print('-'*40)
	apparels_discount = 0
	electronics_discount = 0
	eatables_discount = 0
	if apparels_cost >= 2000:
		apparels_discount = get_discount(apparels_cost, 0.1)

	if electronics_cost >= 25000:
		electronics_discount = get_discount(electronics_cost, 0.1)

	if eatables_cost >= 500:
		eatables_discount = get_discount(eatables_cost, 0.1)

	total_discount = apparels_discount + eatables_discount + electronics_discount
	total_cost_after_discount = (apparels_cost + electronics_cost + eatables_cost) - total_discount
	if apparels_discount != 0:
		print("[APPAREL] Rs ", apparels_cost, " - Rs ", apparels_discount, " = Rs ",
			  (apparels_cost - apparels_discount))
	if electronics_discount != 0:
		print("[ELECTRONICS] Rs ", electronics_cost, " - Rs ", electronics_discount, " = Rs ",
			  (electronics_cost - electronics_discount))
	if eatables_discount != 0:
		print("[EATABLES] Rs ", eatables_cost, " - Rs ", eatables_discount, " = Rs ",
			  (eatables_cost - eatables_discount))

	discounted_apparels_cost = apparels_cost - apparels_discount
	discounted_electronics_cost = electronics_cost - electronics_discount
	discounted_eatables_cost = eatables_cost - eatables_discount
	print('')
	print("TOTAL DISCOUNT = Rs ", total_discount)
	print("TOTAL COST = Rs ", total_cost_after_discount)
	return (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost)


def get_tax(cost, tax): #helper function for calculating tax with formal parameters as cost and tax

	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost): #calculates tax of each category seperately
	print("-" * 40)
	print("TAX")
	print("-" * 40)
	apparels_tax = get_tax(apparels_cost, 0.1)
	electronics_tax = get_tax(electronics_cost, 0.15)
	eatables_tax = get_tax(eatables_cost, 0.05)
	if apparels_cost>0:
		print('[APPAREL] Rs', apparels_cost, '* 0.10 = Rs.', apparels_tax)
	if electronics_cost>0:
		print('[ELECTRONICS] Rs', electronics_cost, '* 0.15 = Rs.', electronics_tax)
	if eatables_cost>0:
		print('[EATABLES] Rs', eatables_cost, '* 0.05 = Rs.', eatables_tax)
	total_tax = apparels_tax + eatables_tax + electronics_tax
	total_cost_including_tax = (apparels_cost + eatables_cost + electronics_cost) + total_tax
	print('')
	print("TOTAL TAX = Rs", total_tax)
	print("TOTAL COST = Rs", total_cost_including_tax)
	print('')
	return (total_cost_including_tax, total_tax)


def apply_coupon_code(total_cost):
	print('-' * 40)
	print("COUPON CODE")
	print('-' * 40)
	coupon_code = input("Enter coupon code(else leave blank) :")
	while True:
		if coupon_code == "HELLE25": #this if else is dedicated for HELLE25 coupon code

			if total_cost >= 25000:
				total_coupon_discount = min(5000, 0.25 * total_cost)
				print("[HELLE25] min(5000,Rs",total_cost,"*0.25) = Rs ",total_coupon_discount)
				print('')
				break    #we are exiting away from the loop only when the input value i.e Total cost >25000 and the code used is HELLE25
			else:        #else in all the case when HELLE25 is applied and total cost is less than 25000 , it will prompt the user to enter the code again
				print("Code Invalid:Total Cost less than 25k Rs.")
				total_coupon_discount = 0

		if coupon_code == "CHILL50": #this if else is dedicatd for CHILL50 coupon code

			if total_cost >= 50000:
				total_coupon_discount = min(10000, 0.5 * total_cost)
				print("[CHILL50] min(10000,Rs", total_cost, "*0.5) = Rs ", total_coupon_discount)
				print('')
				break  #we are exiting from the loop only when the input value is Greater than 50000 and the code used is CHILL50
			else:      # else in all the case when CHILL50 is applied and the total cost is less than 50000 , it will promopt the user to enter the code again
				print("Code Invalid:Total Cost less than 50000")
				total_coupon_discount = 0

		if coupon_code == "": #this condition is for the case when user enters empty string that is if user leaves empty space
			print("No Coupon Code Applied")
			total_coupon_discount = 0
			break #we are exiting the loop as soon as the user enters empty string , in simple terms when the user presses ENTER key , we exit from the loop

		else:
			print("Invalid Coupon Code. Try Again.")  #for all the other cases when the input is not valid the user is promopted to enter the correct code
			coupon_code = input("ENTER COUPON CODE :") #until the user doesnt enter empty character or the correct Coupon Code with the right Total amount

	total_cost_after_discount = total_cost - total_coupon_discount
	print("TOTAL COUPON DISCOUNT = Rs ", total_coupon_discount)
	print("TOTAL COST = Rs. ", total_cost_after_discount)
	print('')
	print("Thank you for visiting!")
	return (total_cost_after_discount, total_coupon_discount)

def main(): #the main function for the shopping
	show_menu()

	if bulkchoice == "y" or bulkchoice == 'Y':
		calc1= get_bulk_input()
	elif bulkchoice == 'n' or bulkchoice =='N':
		calc1=get_regular_input()

	print_order_details(calc1)
	calc2=calculate_category_wise_cost(calc1)
	calc3=calculate_discounted_prices(*calc2)
	calc4=calculate_tax(*calc3)
	calc5=apply_coupon_code(calc4[0])


if __name__ == '__main__':
	main()
