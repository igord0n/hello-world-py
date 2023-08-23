cores = {'vermelho': '\033[0;31m',
         'azul': '\033[0;34m',
         'verde': '\033[0;32m',
         'roxo': '\033[0;35m',
         'limpa': '\033[m'
         }

helloWorld = "{}Hello, world colored in python.".format(cores['vermelho'])
print(helloWorld)

# Just learning how to use color directly in line.

doYouKnow = input(
    "{}Did you know that it was possible using ANSI? ".format(cores['azul']))
print(doYouKnow + ".\n" + "Actually I just learned it... Cool, isn't? ^.^")
