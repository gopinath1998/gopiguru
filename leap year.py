num=int(input("enter year value"))

if num%4==0:

	if num%100==0:

		if num%400==0:

			print"not a leap year"

		else:

			print"leap year"

	else:

		print"leap year"

else:

	print"leap year"