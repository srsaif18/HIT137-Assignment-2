"""
Group Members: 
1. Nahid Hasan Sangram
2. Mou Rani Biswas  
3. Md Saifur Rahman
4. Mohammed Rifatul Alam

Our Thought Process:
1. Use turtle graphics to create visual patterns
2. Implement recursive function to transform edges according to specified rules
3. For each edge: divide into 3 segments, replace middle with inverted triangle
4. Handle different starting polygons (triangle, square, pentagon, etc.)
5. Control recursion depth to create varying complexity
6. Set up turtle graphics window with proper configuration
7. Add user input validation

Prompts Used:
1. "Create recursive geometric pattern with turtle graphics using polygon edges"
2. "Implement Koch snowflake-like algorithm but with inward pointing triangles"
3. "Divide edge into 3 segments and replace middle with equilateral triangle pointing inward"
"""

import turtle
import math

def draw_edge(t, length, depth):
    """
    Recursive function to draw a single edge with pattern.
    
    Args:
        t: Turtle object
        length: Length of the edge
        depth: Recursion depth
    """
    if depth == 0:
        # Base case: draw straight line
        t.forward(length)
    else:
        # Divide edge into 3 segments
        segment_length = length / 3
        
        # Draw first segment
        draw_edge(t, segment_length, depth - 1)
        
        # Turn left 60 degrees for the inward-pointing triangle
        t.left(60)
        draw_edge(t, segment_length, depth - 1)
        
        # Turn right 120 degrees for the other side of triangle
        t.right(120)
        draw_edge(t, segment_length, depth - 1)
        
        # Turn left 60 degrees to return to original direction
        t.left(60)
        
        # Draw last segment
        draw_edge(t, segment_length, depth - 1)

def draw_polygon_pattern(sides, side_length, depth):
    """
    Draw a polygon with the recursive pattern applied to each side.
    
    Args:
        sides: Number of sides of the polygon
        side_length: Length of each side
        depth: Recursion depth
    """
    # Set up turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.penup()
    
    # Position turtle to center the drawing
    # Calculate starting position based on polygon geometry
    if sides % 2 == 0:
        # Even number of sides
        angle_offset = 90
    else:
        # Odd number of sides
        angle_offset = 90 - (180 / sides)
    
    # Calculate radius of circumscribed circle
    radius = side_length / (2 * math.sin(math.pi / sides))
    
    # Move to starting position
    t.goto(radius * math.cos(math.radians(angle_offset)), 
           radius * math.sin(math.radians(angle_offset)))
    t.setheading(angle_offset + 180)
    t.pendown()
    
    # Calculate interior angle of polygon
    interior_angle = 180 * (sides - 2) / sides
    
    # Draw each side with pattern
    for _ in range(sides):
        draw_edge(t, side_length, depth)
        t.right(180 - interior_angle)
    
    # Hide turtle after drawing
    t.hideturtle()

def get_user_input():
    """Get and validate user input."""
    while True:
        try:
            sides = int(input("Enter the number of sides (3-12): "))
            if 3 <= sides <= 12:
                break
            else:
                print("Please enter a number between 3 and 12.")
        except ValueError:
            print("Please enter a valid integer.")
    
    while True:
        try:
            side_length = float(input("Enter the side length (50-500 pixels): "))
            if 50 <= side_length <= 500:
                break
            else:
                print("Please enter a length between 50 and 500 pixels.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            depth = int(input("Enter the recursion depth (0-5): "))
            if 0 <= depth <= 5:
                break
            else:
                print("Please enter a depth between 0 and 5.")
        except ValueError:
            print("Please enter a valid integer.")
    
    return sides, side_length, depth

def visualize_examples():
    """Show examples of different patterns."""
    print("\n" + "="*60)
    print("PATTERN EXAMPLES")
    print("="*60)
    print("Depth 0: Straight line (no modification)")
    print("Depth 1: Line becomes: ——\\⁄—— (indentation pointing inward)")
    print("Depth 2: Each of the 4 segments from depth 1 gets its own indentation")
    print("Depth 3: Further refinement of each segment")
    print("="*60)
    print("\nCommon starting shapes:")
    print("- 3 sides: Triangle")
    print("- 4 sides: Square")
    print("- 5 sides: Pentagon")
    print("- 6 sides: Hexagon")
    print("- 8 sides: Octagon")
    print("="*60)

def main():
    """Main function to run the pattern generator."""
    print("="*60)
    print("GEOMETRIC PATTERN GENERATOR")
    print("="*60)
    
    # Show examples
    visualize_examples()
    
    # Get user input
    print("\nEnter your pattern parameters:")
    sides, side_length, depth = get_user_input()
    
    # Set up screen
    screen = turtle.Screen()
    screen.title(f"Geometric Pattern: {sides}-sided Polygon, Depth {depth}")
    screen.bgcolor("white")
    screen.setup(width=800, height=800)
    
    # Display pattern info
    info_turtle = turtle.Turtle()
    info_turtle.hideturtle()
    info_turtle.penup()
    info_turtle.goto(0, -350)
    info_turtle.color("blue")
    info_turtle.write(f"Polygon: {sides} sides | Side Length: {side_length} | Recursion Depth: {depth}", 
                     align="center", font=("Arial", 12, "bold"))
    
    # Draw the pattern
    try:
        draw_polygon_pattern(sides, side_length, depth)
        print("\nPattern generation complete!")
        print("Close the turtle window to exit.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your input values and try again.")
    
    # Keep window open
    turtle.mainloop()

def draw_sample_patterns():
    """Function to demonstrate different patterns (for testing)."""
    # Example 1: Square with depth 2
    screen = turtle.Screen()
    screen.title("Sample Patterns")
    screen.bgcolor("white")
    
    # Pattern 1: Triangle, depth 3
    print("\nDrawing sample pattern: Triangle, depth 3")
    draw_polygon_pattern(3, 200, 3)
    
    # Clear screen for next pattern
    input("\nPress Enter to see next pattern...")
    screen.clear()
    
    # Pattern 2: Square, depth 2
    print("Drawing sample pattern: Square, depth 2")
    draw_polygon_pattern(4, 200, 2)
    
    # Clear screen for next pattern
    input("\nPress Enter to see next pattern...")
    screen.clear()
    
    # Pattern 3: Hexagon, depth 1
    print("Drawing sample pattern: Hexagon, depth 1")
    draw_polygon_pattern(6, 150, 1)
    
    turtle.mainloop()

if __name__ == "__main__":
    # Uncomment the next line to run sample patterns instead of user input
    # draw_sample_patterns()
    
    # Run main program with user input
    main()