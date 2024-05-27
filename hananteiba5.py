bin_num = list(input("please input binary number:"))
d=0
for i in range(len(bin_num)):
    digital = bin_num.pop()
    if digital == '1' :
        d=d+pow(2,i)


print("the decimal value of the bin_num is",d)