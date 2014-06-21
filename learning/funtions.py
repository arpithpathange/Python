def add(a,b):
    return a+b

def TopOrBottom(width): 
# width is total width  of returned line
 
    return '%s%s%s' % ('+',('=' * (width-2)),'+') 


print TopOrBottom(10)
print add(1,2)
print TopOrBottom(10)