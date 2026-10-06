import numpy as np 

'''
Find:
1. Total sales
2. Sales of each product
3. Sales of each day
4. Average sales of each product
5. Maximum sale
6. Minimum sale
'''
sales = np.array([
    [1000, 2000, 3000],
    [1500, 2500, 3500],
    [2000, 3000, 4000]
])

# 1 
print("Total sales:",np.sum(sales))

# 2. Sales of each product
print("Sales of each product")
each_product_sum = np.sum(sales, axis=1)

for index, each_product_sales in enumerate(each_product_sum, start=1): 
    print("",index," : ",each_product_sales)

# 3. Sales of each day
# sales_each_day = sales[:,0:3]
# ndenumerate
for day, sales_each_day in np.ndenumerate(sales) : 
    print("Day",day,": Sales",sales_each_day)
    print()


# 4. Average sales of each product
average_sales_product = np.mean(sales, axis=1, keepdims=True)
print(average_sales_product)


# max sale 
print(np.max(sales))

# minimum sales 
print(np.min(sales))