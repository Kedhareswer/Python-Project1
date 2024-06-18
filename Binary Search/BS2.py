// find median of a list?
>>> median([1, 3, 5])
3
>>> median([1, 3, 5, 7])
4.0


import statistics

items = [6, 1, 8, 2, 3]

statistics.median(items)
#>>> 3


statistics.median(map(float, items))
#>>> 3.0

from decimal import Decimal
statistics.median(map(Decimal, items))
#>>> Decimal('3')




#Source: https://stackoverflow.com/questions/24101524


