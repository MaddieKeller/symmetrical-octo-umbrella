using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FileTransferDrill46
{
    class OpenFile
    {
          public static List<string> getFiles(string dirPath)
        {
            List<string> dirs = new List<string>(Directory.EnumerateFiles(dirPath));
            
            foreach (string dir in dirs)
            {
                Console.WriteLine(dir);
            }
            Console.WriteLine("There were {0} files found.", dirs.Count);
            return dirs;
        }

        public static void copyFile(string dirPath, DateTime ageToCheck, string newPath)
        {
            //enumerate through the files in the dirPath and get all ones newer than ageToCheck
            DirectoryInfo dirsInfo = new DirectoryInfo(dirPath);
            var dirs = from dir in dirsInfo.EnumerateFiles()
                       where dir.LastWriteTime > ageToCheck
                       select dir;

            //add folder if doesn't already exist
            if (!System.IO.Directory.Exists(newPath))
            {
                System.IO.Directory.CreateDirectory(newPath);
            }

            int count = 0;
            string newFile = null;

            foreach(var d in dirs)
            {
                Console.WriteLine("{0} was last accessed on {1}.", d.Name, d.LastWriteTime);
                newFile = System.IO.Path.Combine(newPath, d.Name);

                System.IO.File.Copy(d.FullName, newFile, true);

                count++;
            }
            Console.WriteLine("There are {0} new files", count);
        }

    }
}
