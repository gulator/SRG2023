from django.test import TestCase

# Create your tests here.

test = {1:'rosa',2:'pedro',3:'alma',4:'leandro'}
orden = {k: v for k, v in sorted(test.items(), key=lambda item: item[1])}
print(orden)