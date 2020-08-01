# famitracker2midi

This is a Python 3 script that converts Famitracker .txt output files into MIDI files.

I wrote this program so that Famitracker composers could use the program to compose for platforms other than the Famicom itself. 

Make sure [mido](https://mido.readthedocs.io/en/latest/installing.html) is installed before running this script.

##  How to convert:

Step 1: Prepare the files - https://youtu.be/Y869wolHxwk

Step 2: Export your famitracker file to TEXT and place it in the same folder as midifam.py

Step 3: Edit the code
  - go to line 90 and change the text file name to the name of your exported file
  - go to the last line and change the output midi file name
  
Step 4: Run the Code

Step 5: Enjoy



TODO:
  - use command line arguments to get the file names
  - allow effects from the effects columns
  - convert the drum channel
  - allow more user control over how the conversion works
