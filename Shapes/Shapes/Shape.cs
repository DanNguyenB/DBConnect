using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Shapes
{
    class Shape
    {
        // Global variables.
        protected string colour;

        // Area is declared here once as protected so the circle and rectangle class can use it -- even if their areas are calculated individually.
        protected double area;

        // Default constructor.
        public Shape()
        {
            colour = "Red";
            area = 15.0;
        }

        // Overloaded constructor.
        public Shape(string colour, double area)
        {
            this.colour = colour;
            this.area = area;
        }

        // Accessors.
        public string GetColour()
        {
            return colour;
        }
        public double GetArea()
        {
            return area;
        }

        public void DisplayColour()
        {
            Console.WriteLine("Colour: " + colour);
        }
    }
}
