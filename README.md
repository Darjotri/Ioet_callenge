# IOET_CHALLENGE EMPLOYEES OCCURRENCIES

Program to verify if two employees were at the same time frame in the office.

In my solution I use Python as the programming languagae, because is easy to use command line programs like this, I use three Python files:
main.py that is a file to call all the functionallity of the project,
utils. py that is a file to define some functions to read the file and parse the file name to use the command line,
and controller. py that contains the logic part of the project uses functions to build a dictionary using the file with employee name as a key and the lis of time frames as value,
to compare the time frames and display it as another dictionary, with the names of the two employees as key and the times that they were at the same time as value.

In this solution you can notice that every file encapsulates an espoecific functionallity that do just one thing, helping to re use this functions in another part of teh code, also the test part were made exhaustively during the construction of the code without using any library.
The format of the input file will be the same as the example proposedin the challenge email, but you can construct your own examples, if they have an extra space or similar I controlling it by deleting it in the code.
In every function that I use, I left a comment to explain the functionallity.

To execute the program:
1. Open a command line in your computer n a folder that you to use.
2. Download git repository, go to code and copy https://github.com/Darjotri/Ioet_challenge.git and then use the command "git clone <link>".
3. Once there go to the folder downloaded with the command  "cd Ioet_challenge".
4. To run the code use the following command: "python main.py <file_name>", you can use any file name, but with the format of the challenge,
I porpose the input.txt, but if you want to rename it or use another file just copy the file to the project folder and use the command with that file.

Note: A external library is used to parse the file name, just is aesthetic.
