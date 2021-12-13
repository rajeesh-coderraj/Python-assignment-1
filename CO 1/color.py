#create a list of colors from comma-separated color names entered by user .Display first and last colours
colors=str(input("enter the color separated by ,:"))
newcolor=colors.split(",")
print(newcolor)
print(newcolor[0],newcolor[-1])
