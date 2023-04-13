# geo-creator
A Python library for creating geometry in the Gmsh .geo format.

## Installation
To use geo-creator, you must first install Gmsh on your system. You can download Gmsh from the official website: https://gmsh.info/.
Once Gmsh is installed, you can install Gmsh Geometry Creator using pip:
pip install geo-creator

## Usage

To use geo-creator in your Python project, import the `geo-creator` module:

```python
import geo-creator

# Create a Point at (0, 0, 0)
p = geo-creator.Point(0, 0, 0)

# Create a Line connecting two Points
p1 = geo-creator.Point(0, 0, 0)
p2 = geo-creator.Point(1, 1, 1)
l = geo-creator.Line(p1, p2)

# Create a Surface enclosing a set of Lines
s = geo-creator.Surface([l])

For more examples and documentation, see the documentation website.

## Contributing
Contributions to Gmsh Geometry Creator are welcome! To contribute, fork the repository, make your changes, and submit a pull request. Please see the contributing guidelines for more information.

## License
Geo-creator is released under the MIT License.