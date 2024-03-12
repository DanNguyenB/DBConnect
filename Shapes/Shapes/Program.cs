using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Shapes
{
    class Program
    {
        static void Main(string[] args)
        {
            string userChoice = "";

            string userColour = "";

            double userLength;
            double userWidth;
            double perimeter = 0;

            double userRadius;
            double userDiameter;
            double circumference = 0;

            double area = 0;

            bool isDone = false;

            while (isDone == false)
            {
                Console.Clear();

                Console.WriteLine("Choose a shape to perform operations on. \n1 - Rectangle  \n2 - Circle");
                userChoice = Console.ReadLine();

                switch (userChoice)
                {
                    case "1":
                        Console.WriteLine("Please enter a colour for your rectangle.");
                        userColour = Console.ReadLine();
                        Console.WriteLine("Please enter a length for your rectangle.");
                        userLength = Convert.ToDouble(Console.ReadLine());
                        Console.WriteLine("Please enter a width for your rectangle.");
                        userWidth = Convert.ToDouble(Console.ReadLine());

                        Rectangle userRectangle = new Rectangle(userColour, area, userLength, userWidth, perimeter);

                        userRectangle.DisplayColour();
                        userRectangle.DisplayArea();
                        userRectangle.DisplayPerimeter();

                        Console.ReadLine();
                        break;

                    case "2":
                        Console.WriteLine("Please enter a colour for your circle.");
                        userColour = Console.ReadLine();
                        Console.WriteLine("Please enter a radius for your circle.");
                        userRadius = Convert.ToDouble(Console.ReadLine());
                        Console.WriteLine("Please enter a diameter for your circle.");
                        userDiameter = Convert.ToDouble(Console.ReadLine());

                        Circle userCircle = new Circle(userColour, area, userRadius, userDiameter, circumference);

                        userCircle.DisplayColour();
                        userCircle.DisplayArea();
                        userCircle.DisplayCircumference();

                        Console.ReadLine();
                        break;
                }
            }
        }
    }
}
