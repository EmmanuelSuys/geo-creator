filename = "example.geo"

with open(filename, "w") as file:
    file.write("// This is a comment\n")
    
    # Create points
    p1 = Point(1, 0, 0, 0, 0.1, "Define first point")
    p2 = Point(2, 1, 0, 0, 0.1, "Define second point")
    
    # Create lines
    l1 = Line(1, 1, 2, "Connect the two points")
    
    # Create surfaces
    s1 = Surface(1, 1, comment="Define the surface")
    
    # Write to file
    file.write(str(p1))
    file.write(str(p2))
    file.write(str(l1))
    file.write(str(s1))
