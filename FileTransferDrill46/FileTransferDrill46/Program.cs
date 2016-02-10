using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FileTransferDrill46
{
    class Program
    {
        static void Main(string[] args)
        {
            string dirName = @"C:\\Users\\Madison\\Desktop\\Folder A";
            string dirNew = @"C:\\Users\\Madison\\Desktop\\Folder B";
            DateTime currentTime = DateTime.Now;
            DateTime prevTime = currentTime.AddHours(-24);

            Console.WriteLine(currentTime);
            OpenFile.copyFile(dirName, prevTime, dirNew);

            Console.WriteLine("Press anykey to continue...");
            Console.ReadLine();
        }
    }
}
