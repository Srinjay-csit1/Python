r=float(input("Enter radius="))
def areaCircle(r):
    area=3.14*(r*r)
    return area
def periCircle(r): 
    peri=3.14*2*r   
    return peri
print("area of the circle=",areaCircle(r))
print("Perimeter of the circle=",periCircle(r))