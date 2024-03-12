using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Shapes
{
    class Circle : Shape
    {
        // Global variables
        private double radius;
        private double diameter;
        private double circumference;

        // Default constructor. Also calls the default constructor of the base class (Shape).
        public Circle() : base()
        {
            // Giving circle attributes default values.
            this.radius = 5.5;
            this.diameter = 11;
            this.circumference = (diameter * Math.PI);
        }
        // Overloaded constructor. Also calls the overloaded constructor of Shape. Circle's attributes are not passed.
        public Circle(string colour, double area, double radius, double diameter, double circumference) : base(colour, area)
        {
            // Sets circle attributes with default values.
            this.radius = radius;
            this.diameter = diameter;
            this.circumference = circumference;
        }

        // Accessors.
        public double GetRadius()
        {
            return radius;
        }
        public double GetDiameter()
        {
            return diameter;
        }

        // Behaviours.

        // Public functions
        public void DisplayArea()
        {
            area = Math.PI * Math.Pow(GetRadius(), 2);

            Console.WriteLine("The area of your circle is " + area);
        }
        public void DisplayCircumference()
        {
            circumference = Math.PI * GetDiameter();

            Console.WriteLine("The circumference of your circle is " + circumference);
        }
    }
}
