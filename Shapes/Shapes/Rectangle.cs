using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Shapes
{
    class Rectangle : Shape
    {
        // Global variables
        private double length;
        private double width;
        private double perimeter;

        // Default constructor of rectangle that calls the default constructor of Shape.
        public Rectangle() : base()
        {
            // Gives default values to rectangle attributes.
            this.length = 4;
            this.width = 3;
            this.perimeter = 14;

            // Default values have already been given in the shapes class.
        }

        // Overloaded constructor. Also calls the overloaded constructor of Shape. Rectangle's attributes are not passed.
        public Rectangle(string colour, double area, double length, double width, double perimeter) : base(colour, area)
        {
            this.length = length;
            this.width = width;
            this.perimeter = perimeter;
        }

        // Accessors

        public double GetLength()
        {
            return length;
        }
        public double GetWidth()
        {
            return width;
        }

        // Behaviours

        public void DisplayArea()
        {
            area = GetLength() * GetWidth();
            if (area >= 0)
            {
                Console.WriteLine("The area of your rectangle is " + area);
            }
            else
            {
                Console.WriteLine("The area of your rectangle is invalid.");
            }
        }

        public void DisplayPerimeter()
        {
            perimeter = (2 * GetLength()) + (2 * GetWidth());
            Console.WriteLine("The perimeter of your rectangle is " + perimeter);
        }
    }
}
