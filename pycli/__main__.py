import sys, argparse
#from pycli.Functions.print_argument import print_arg
#from Classes.classmodule import MyClass

my_parser=argparse.ArgumentParser()
my_parser.add_argument('--num1', required=True, type=int)
my_parser.add_argument('--num2', required=True, type=int)
#my_parser.add_argument('--name', required=True, type=str)


args=my_parser.parse_args()

def main():

	#my_object = MyClass(args.name)
	#prod=my_object.multiply()
	#total=my_object.sum()

	#phrase=my_object.print_argument()
	sum=args.num1+args.num2
	print ('The sum is '+sum)
	#print (total)


if __name__ == '__main__':
	main()

