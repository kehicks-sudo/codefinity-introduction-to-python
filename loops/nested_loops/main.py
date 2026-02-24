produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk",]
groceries = produce + dairy
for section in groceries:
    print(section)
    for item in section:
        print(item)
        
        