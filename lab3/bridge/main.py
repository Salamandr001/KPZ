from Circle import Circle
from Square import Square
from Triangle import Triangle
from Renderer import VectorRenderer, RasterRenderer

def main():
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    circle = Circle(vector_renderer)
    square = Square(raster_renderer)
    triangle = Triangle(vector_renderer)

    circle.draw()
    square.draw()
    triangle.draw()

if __name__ == '__main__':
    main()
