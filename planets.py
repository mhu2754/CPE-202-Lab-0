def weight_on_planets():
   # write your code here
   x = float(input('What do you weigh on earth? '))
   y = x * 0.38
   z = x * 2.34
   print(f'\n'
         f'On Mars you would weigh {y} pounds.\n'
         f'On Jupiter you would weigh {z} pounds.')

if __name__ == '__main__':
   weight_on_planets()