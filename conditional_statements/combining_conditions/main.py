# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct = (discounted == True) or (lowStock == True)
promotion = (discounted == False) and not(lowStock == True)
print ("Is the item eligible for promotion?", promotion)