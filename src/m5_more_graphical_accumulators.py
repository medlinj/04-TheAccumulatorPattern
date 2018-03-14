"""
This module lets you practice one form of the ACCUMULATOR pattern,
namely, the "IN GRAPHICS" form which features:
  -- DRAWING OBJECTS via ACCUMULATING positions and/or sizes,
     as in:   x = x + pixels

Additionally, it emphasizes that you must
  ** DO A CONCRETE EXAMPLE BY HAND **
before you can implement a solution to the problem in Python. 
  
Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and JD Medlin.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math


# ----------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    #run_test_draw_squares_from_circle()
    #run_test_draw_circles_from_rectangle()
    run_test_draw_lines_from_rectangles()


def run_test_draw_squares_from_circle():
    """ Tests the   draw_squares_from_circle  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_squares_from_circle  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # TWO tests on ONE window.
    # ------------------------------------------------------------------
    title = 'Tests 1 and 2 of DRAW_SQUARES_FROM_CIRCLE: '
    title = title + ' 7 little squares from green circle, 4 big squares'
    window1 = rg.RoseWindow(650, 350, title)

    # Test 1:
    circle = rg.Circle(rg.Point(100, 100), 20)
    circle.fill_color = 'green'
    draw_squares_from_circle(7, circle, window1)

    # Test 2:
    circle = rg.Circle(rg.Point(350, 70), 50)
    draw_squares_from_circle(4, circle, window1)
    window1.close_on_mouse_click()

    # ------------------------------------------------------------------
    # A third test on ANOTHER window.
    # ------------------------------------------------------------------
    title = 'Test 3 of DRAW_SQUARES_FROM_CIRCLE: '
    title += ' 20 teeny squares from blue circle!'
    window2 = rg.RoseWindow(525, 300, title)

    # Test 3:
    circle = rg.Circle(rg.Point(50, 50), 10)
    circle.fill_color = 'blue'
    draw_squares_from_circle(20, circle, window2)

    window2.close_on_mouse_click()


def draw_squares_from_circle(n, circle, window):
    """
    What comes in:  Three arguments:
      -- A positive integer n.
      -- An rg.Circle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_squares_from_circle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Circle on the given rg.RoseWindow.
      Then draws  n  rg.Squares on the given rg.RoseWindow, such that:
        -- The first rg.Square circumscribes the given rg.Circle.
        -- Each subsequent rg.Square has its upper-left quarter
             on top of the lower-right quarter of the previous rg.Square,
             so that the squares form an overlapping sequence
             that goes down and to the right.
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type n: int
      :type circle: rg.Circle
      :type window: rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       positions of each square,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------

    circle.attach_to(window)
    for k in range(n):
        corner1 = rg.Point(circle.center.x - circle.radius + circle.radius * k, circle.center.y - circle.radius + circle.radius * (k))
        corner2 = rg.Point(circle.center.x + circle.radius + circle.radius * k, circle.center.y + circle.radius + circle.radius * (k))
        rect = rg.Rectangle(corner1, corner2)
        rect.attach_to(window)
    window.render()


def run_test_draw_circles_from_rectangle():
    """ Tests the   draw_circles_from_rectangle  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_circles_from_rectangle  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # DONE: 3. Implement this TEST function.
    #   It TESTS the  draw_circles_from_rectangle  function
    #   defined below.  Include at least **   3   ** tests, of which
    #      ***  at least TWO tests are on ONE window and
    #      ***  at least ONE test is on a DIFFERENT window.
    #
    ####################################################################
    # HINT: Consider using the same test cases as suggested by the
    #   pictures in  draw_circles_from_rectangle.pdf   in this project.
    #   Follow the same form as the example in a previous problem.
    ####################################################################
    # ------------------------------------------------------------------

    window3 = rg.RoseWindow(600, 600)

    rectangle1 = rg.Rectangle(rg.Point(75, 50), rg.Point(90, 75))
    rectangle1.fill_color = 'blue'
    rectangle1.outline_color = 'orange'
    draw_circles_from_rectangle(5, 20, rectangle1, window3)


    rectangle2 = rg.Rectangle(rg.Point(200, 300), rg.Point(450, 500))
    rectangle2.fill_color = 'brown'
    rectangle2.outline_color = 'yellow'
    draw_circles_from_rectangle(20, 10, rectangle2, window3)


    rectangle3 = rg.Rectangle(rg.Point(100, 100), rg.Point(200, 200))
    rectangle3.fill_color = 'red'
    rectangle3.outline_color = 'purple'
    draw_circles_from_rectangle(20, 10, rectangle3, window3)
    window3.close_on_mouse_click()



def draw_circles_from_rectangle(m, n, rectangle, window):
    """
    What comes in:  Four arguments:
      -- Positive integers m and n.
      -- An rg.Rectangle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_circles_from_rectangle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Rectangle on the given rg.RoseWindow.
      Then draws  m  rg.Circles on the given rg.RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the height
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately to the left of the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately to the left
             of the previous rg.Circle, so that the circles form a row
             that goes to the left.
        -- Each rg. Circle has the same fill_color as the given
             rg.Rectangle (and has no outline_color).
      Then draws  n  rg.Circles on the given RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the width
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately above the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately above the previous
             rg.Circle, so that the circles form a column that goes up.
        -- Each rg.Circle has the same outline_color as the given
             rg.Rectangle (and has no fill_color).
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type m: int
      :type n: int
      :type rectangle: rg.Rectangle
      :type window: rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       positions of each circle,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------

    rectangle.attach_to(window)

    for k in range(m):
        radius = (rectangle.corner_2.y - rectangle.corner_1.y) / 2
        center = rg.Point(rectangle.corner_1.x - radius - 2 * radius * k, rectangle.corner_1.y + radius)
        circle = rg.Circle(center, radius)
        circle.attach_to(window)
        circle.fill_color = rectangle.fill_color

    for k in range(n):
        radius = (rectangle.corner_2.x - rectangle.corner_1.x) / 2
        center = rg.Point(rectangle.corner_1.x + radius, rectangle.corner_1.y - radius - 2 * radius * k)
        circle = rg.Circle(center, radius)
        circle.attach_to(window)
        circle.outline_color = rectangle.outline_color
    window.render()


def run_test_draw_lines_from_rectangles():
    """ Tests the   draw_lines_from_rectangles  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_lines_from_rectangles  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 & 2 of DRAW_LINES_FROM_RECTANGLES:'
    title += '  5 lines, 8 lines!'
    window1 = rg.RoseWindow(900, 400, title)

    rectangle1 = rg.Rectangle(rg.Point(100, 25), rg.Point(150, 125))
    rectangle2 = rg.Rectangle(rg.Point(300, 150), rg.Point(400, 175))
    rectangle1.outline_color = 'red'
    rectangle2.outline_color = 'blue'
    draw_lines_from_rectangles(rectangle1, rectangle2, 5, window1)

    rectangle1 = rg.Rectangle(rg.Point(870, 30), rg.Point(750, 100))
    rectangle2 = rg.Rectangle(rg.Point(700, 90), rg.Point(650, 60))
    rectangle2.outline_color = 'green'
    draw_lines_from_rectangles(rectangle1, rectangle2, 8, window1)

    window1.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = 'Test 3 of DRAW_LINES_FROM_RECTANGLES:  11 lines!'
    window2 = rg.RoseWindow(700, 700, title)

    rectangle1 = rg.Rectangle(rg.Point(550, 200), rg.Point(650, 100))
    rectangle2 = rg.Rectangle(rg.Point(600, 50), rg.Point(650, 75))
    rectangle1.outline_color = 'brown'
    rectangle2.outline_color = 'cyan'
    rectangle2.outline_thickness = 10
    draw_lines_from_rectangles(rectangle1, rectangle2, 11, window2)

    window2.close_on_mouse_click()


def draw_lines_from_rectangles(rectangle1, rectangle2, n, window):
    """
    What comes in:  Four arguments:
      -- Two rg.Rectangles.
      -- A positive integer n.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_lines_from_rectangles.pdf   in this project
      for pictures that may help you better understand
      the following specification:

      First draws the given rg.Rectangles on the given rg.RoseWindow.
      Then draws  n  rg.Lines on the given rg.RoseWindow, such that:
        -- The 1st rg.Line goes from the center of one of the
             1st rg.Rectangle to the center of the 2nd rg.Rectangle.
        -- The 2nd rg.Line goes from the lower-left corner of the
              1st rg.Rectangle and is parallel to the 1st rg.Line,
              with the same length and direction as the 1st rg.Line.
        -- Subsequent rg.Lines are shifted from the previous rg.Line in
              the same way that the 2nd rg.Line is shifted from the 1st.
        -- Each of the rg.Lines has thickness 5.
        -- The colors of the rg.Lines alternate, as follows:
             - The 1st, 3rd, 5th, ... rg.Line has color R1_color
             - The 2nd, 4th, 6th, ... rg.Line has color R2_color
            where
             - R1_color is the outline color of the 1st rg.Rectangle
             - R2_color is the outline color of the 2nd rg.Rectangle
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type rectangle1: rg.Rectangle
      :type rectangle2: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
      """
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       endpoints for each line,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------

    rectangle1.attach_to(window)
    rectangle2.attach_to(window)

    # for k in range(n):
    #     if rectangle1.corner_2.y > rectangle1.corner_1.y:
    #         p1_y = (rectangle1.corner_2.y - rectangle1.corner_1.y) / 2
    #     else:
    #         p1_y = (rectangle1.corner_1.y - rectangle1.corner_2.y) / 2
    #     if rectangle1.corner_2.x > rectangle1.corner_1.x:
    #         p1_x = (rectangle1.corner_2.x - rectangle1.corner_1.x) / 2
    #     else:
    #         p1_x = (rectangle1.corner_1.x - rectangle1.corner_2.x) / 2
    #
    #     point1 = rg.Point(rectangle1.corner_1.x + p1_x - p1_x * k, rectangle1.corner_2.y - p1_y + p1_y * k)
    #
    #     if rectangle2.corner_2.y > rectangle2.corner_1.y:
    #         p2_y = (rectangle2.corner_2.y - rectangle2.corner_1.y) / 2
    #     else:
    #         p2_y = (rectangle2.corner_1.y - rectangle2.corner_2.y) / 2
    #     if rectangle2.corner_2.x > rectangle2.corner_1.x:
    #         p2_x = (rectangle2.corner_2.x - rectangle2.corner_1.x) / 2
    #     else:
    #         p2_x = (rectangle2.corner_1.x - rectangle2.corner_2.x) / 2
    #
    #     point2 = rg.Point(rectangle2.corner_2.x + p2_x - p1_x * k, rectangle2.corner_2.y + p2_y + p1_y * k)
    #
    #     line = rg.Line(point1, point2)
    #     line.thickness = 5
    #     if k % 2 == 0:
    #         line.color = rectangle1.outline_color
    #     else:
    #         line.color = rectangle2.outline_color
    #     line.attach_to(window)

    # for k in range(n):
    #     p1_y = ((rectangle1.get_height)/2)
    #     p1_x = ((rectangle1.corner_2.x - rectangle1.corner_1.x)/2)
    #     point1 = rg.Point(rectangle1.corner_2.x - p1_x * (k + 1), rectangle1.corner_1.y + p1_y * (k + 1))
    #     p2_x = ((rectangle2.corner_2.x - rectangle2.corner_1.x)/2)
    #     p2_y = ((rectangle2.corner_2.y - rectangle2.corner_1.y)/2)
    #     point2 = rg.Point(rectangle2.corner_1.x - p2_x + p1_x * k, rectangle2.corner_1.y + p2_y + p1_y * k)
    #     line = rg.Line(point1, point2)
    #     line.thickness = 5
    #     if k % 2 == 0:
    #         line.color = rectangle1.outline_color
    #     else:
    #         line.color = rectangle2.outline_color
    #     line.attach_to(window)
    #
    # window.render()

    rectangle1.attach_to(window)
    rectangle2.attach_to(window)

    x_left = rectangle1.get_center().x
    y_left = rectangle1.get_center().y
    x_right = rectangle2.get_center().x
    y_right = rectangle2.get_center().y

    point_1 = rg.Point(x_left, y_left)
    point_2 = rg.Point(x_right, y_right)

    for k in range(n):
        line = rg.Line(point_1, point_2)
        x_left = x_left - rectangle1.get_width()/2
        y_left = y_left + rectangle1.get_height()/2
        x_right = x_right - rectangle1.get_width()/2
        y_right = y_right + rectangle1.get_height()/2
        point_1 = rg.Point(x_left, y_left)
        point_2 = rg.Point(x_right, y_right)
        line.thickness = 5
        if k % 2 == 0:
            line.color = rectangle1.outline_color
        else:
            line.color = rectangle2.outline_color
        line.attach_to(window)
    window.render()
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
