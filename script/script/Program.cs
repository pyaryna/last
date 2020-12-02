using System;
using System.IO;
using System.Linq;

namespace script
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Subprocess started");

            var alphabet = "abcdefghijklmnopqrstuvwxyz0123456789{}:.,()-";
            var path = @".\result.txt";
            string text;

            using (var file = new StreamReader(path))
            {
                Console.WriteLine("Subprocess read the file");
                text = file.ReadToEnd();
            }

            Console.WriteLine("Subprocess count entries of each letter in all file");

            using (var file = new StreamWriter(path, true))
            {
                file.WriteLine("\nSubproces result");
                foreach (var letter in alphabet)
                {
                    var amount = text.ToCharArray().Count(l => l == letter);
                    if (amount > 0)
                    {
                        file.WriteLine($"Letter - {letter}\tamount - {amount}");
                    }
                }
                file.WriteLine("");
            }           

            Console.WriteLine("Press enter to stop subproces");
            Console.ReadKey();
        }
    }
}
