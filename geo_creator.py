class Point:
    def __init__(self, point_id, x, y, z, lc, comment=""):
        self.point_id = point_id
        self.x = x
        self.y = y
        self.z = z
        self.lc = lc
        self.comment = comment
    
    def __str__(self):
        comment_str = "// " + self.comment + "\n" if self.comment else ""
        return comment_str + "Point({0}) = {{{1}, {2}, {3}, {4}}};\n".format(
            self.point_id, self.x, self.y, self.z, self.lc)

class Line:
    def __init__(self, line_id, start_point_id, end_point_id, comment=""):
        self.line_id = line_id
        self.start_point_id = start_point_id
        self.end_point_id = end_point_id
        self.comment = comment
    
    def __str__(self):
        comment_str = "// " + self.comment + "\n" if self.comment else ""
        return comment_str + "Line({0}) = {{{1}, {2}}};\n".format(
            self.line_id, self.start_point_id, self.end_point_id)

class Surface:
    def __init__(self, surface_id, *curve_loop_ids, comment=""):
        self.surface_id = surface_id
        self.curve_loop_ids = curve_loop_ids
        self.comment = comment
    
    def __str__(self):
        comment_str = "// " + self.comment + "\n" if self.comment else ""
        return comment_str + "Plane Surface({0}) = {{{1}}};\n".format(
            self.surface_id, ", ".join(map(str, self.curve_loop_ids)))
