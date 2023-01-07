print("wieght for female")
weightf = float(input("What is your weight: "))
heightf = float(input("what is you hieght: "))
agef = float(input("How old are you: "))
bmrf= 655.1 + 4.35 * weightf + 4.7 * heightf - 4.7 * agef
print("The result of your BMR is", bmrf)
bmr= print("number of bars you need is" ,bmrf/214)



print("wieght for male")
weightm = float(input("What is your weight: "))
heightm = float(input("what is you hieght: "))
agem = float(input("How old are you: "))
bmrm= 66 + 6.2 * weightm + 12.7 * heightm - 6.76 * agem
print("The result of your BMR is", bmrm)
bmrm= print("number of bars you need is" ,bmrm/214)