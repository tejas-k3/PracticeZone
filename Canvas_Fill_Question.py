# Problem statement is as below :-
# Mimic the filling of shape in a Mspaint like application.
# grid/canvas - M X N
# borderColor - integer - 99 (shape already drawn with this colour)
# x and y - coordinates where we will start colouring (fall inside the shape)
# fillCololur - integger - 50 (colour we will use to colour the pixels in the shape)
# The colouring algorithm should colour uniformly in all directions.

"""
Explanation :

So I took example of expanding outwards and realised we're going to paint neighbouring cells
RECURSIVELY! And that's where we are making use of fill(x, y) method which first checks if
cell is valid ie it's within shape/canvas boundry and NOT painted already !

I missed the NOT painted already condition initially leading to infinite recursion. A bad bug indeed :)

Approach is we go outwards from our current cell and mark it's valid neighbours with filler
color till we hit the boundary where our algorithm stops. And as it's happening in all directions
It will continue to fill regardless of shape being regular OR irregular.

I have made use of ChatGPT to generate the driver code & print_canvas method which is a helper
method to envision the canvas after and before the filColor Algorithm.

I/P & O/P
Original Canvas:
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 1 0 1
1 1 1 1 1

Filling at coordinates: (2, 2)

Canvas after filling:
1 1 1 1 1
1 2 2 2 1
1 2 2 2 1
1 2 1 2 1
1 1 1 1 1

"""

def fillColorInCanvas(canvas, bordor_color_number, starting_coordinations, filler_color_number):
    # As we missed out on discussing IF shape will always encapsulate whole area in all direction,
    # we are also checking if the coordinate to be painted is bounded by canvas!
    def coordinate_is_valid_to_color(x, y):
        return  0 <= x < len(canvas) and 0 <= y < len(canvas[0]) and canvas[x][y] != bordor_color_number and canvas[x][y] != filler_color_number 
    
    start_x, start_y = starting_coordinations

    def fill(x, y):
        # It's boundary of canvas or shape or already colored
        if not coordinate_is_valid_to_color(x, y):
            return
        canvas[x][y] = filler_color_number
        fill(x - 1, y - 1) # top left
        fill(x - 1, y) # top
        fill(x - 1, y + 1) # top right
        fill(x, y - 1) # left
        fill(x, y + 1) # right
        fill(x + 1, y) # bottom
        fill(x + 1, y - 1) # bottom left
        fill(x + 1, y + 1) # bottom right

    fill(start_x, start_y)

def print_canvas(canvas):
    for row in canvas:
        print(" ".join(map(str, row)))

# Driver function for your code
if __name__ == "__main__":
    # Example canvas represented as a 2D grid with an irregular boundary
    canvas = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ]

    # Starting coordinates for the fill operation
    start_coordinates = (2, 2)

    # Colors
    filler_color = 2
    boundary_color = 1

    # Display the original canvas
    print("Original Canvas:")
    print_canvas(canvas)
    print("\nFilling at coordinates:", start_coordinates)

    # Call the fill function
    fillColorInCanvas(canvas, boundary_color, start_coordinates, filler_color)

    # Display the canvas after the fill operation
    print("\nCanvas after filling:")
    print_canvas(canvas)
