


#--------------------------------------------
#----Boolean--------
#---------------------------------------------
# [1] in Programming You Need to Known Your If Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True 
#---------------------------------------------


name = ""
print(name.isspace()) # False

print("-" * 50) # --------------------------------------------------

x = ' '
print(x.isspace()) # True

print("-" * 50) # --------------------------------------------------


print(100 > 200) # False
print(100 > 100) # False
print(100 > 90) # True


print("-" * 50) # --------------------------------------------------

# True Values


print(bool("Salar")) # True
print(bool(27)) # True
print(bool(27.65)) # True
print(bool(True)) # True
print(bool([1,2,3,4,5])) # True


print("-" * 50) # --------------------------------------------------


# False Values

print(bool(0)) # False
print(bool("")) # False
print(bool('')) # False
print(bool([])) # False
print(bool(False)) # False
print(bool({})) # False
print(bool(())) # False
print(bool(None)) # False