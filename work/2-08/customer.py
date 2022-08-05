import product

pobj=product.productClass()

pobj.display()

pobj.mobile=2500
pobj.__laptop=50000 #here, value of laptop doesn't change bcz its private

pobj.display()
