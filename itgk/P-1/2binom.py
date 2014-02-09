from math import factorial

lis = []

while True:

    def main():
    	num()
		
    def num():
        n = int(input('Enter n: '))
        k = int(input('Enter k: '))
        nte = float(input('If there is an exponent, type it in! If not, type 1: '))
        if nte is 0:
            nte == 1
        elif nte > 0:
            nte == nte
        elif nte < 0:
            nte == nte
        calc(n, k, nte)
        
    def calc(n, k, nte):
        if k < 0:
            print('0')
        elif k > n:
            print('0')
        elif n >= k >= 0:
            binom = (factorial(n) / (factorial(k) * factorial(n-k))) ** nte
            print_result(binom)

    def print_result(binom):
        if binom > 1:
            print('The answer is: ', format(binom, '.0f'))
        elif binom == 1:
            print('The answer is: ', format(binom, '.0f'))
        else:
            print('The answer is: ', format(binom, '.4f'))
        lis.append(binom)

    main()

    endProg = input('Do you wish to calculate again or exit? (Exit with "e") ')
    if endProg == "e":
        break

print(lis)




       
