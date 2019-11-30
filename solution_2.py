try:
    g=int('abc')
    
except ValueError as e:
    print('value error',e)
try:
    g='43'+34
except TypeError as e:
    print('Type error',e)
try:
     obj='hello'
     obj.remove()
except AttributeError as e:
    print('Attribute error',e)
