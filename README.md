WasatchAnalyzeIQ
=========

Acquire data from Wasatch Photonics spectrometers for use in AnalyzeIQ


Requirements
------------

  * PyQt 4.7+
  * NumPy

Installation 
--------------------

Copy the contents of the folder into analyzeiq directory
screenshots from email go here

Setup and Rebuilding
--------------------

After modifications have been made, rebuild the wasatchdevice_inst and
wasatchdevice_check executables with the commands:

in root of  WasatchAnalyzeIQ:

python wasatchdevice_check_generate.py py2exe
python wasatchdevice_inst_generate.py py2exe

Copy the entire contents of the executable file into the directory:

To package up for installation, create a zip file with the name:
11_Wasatch.zip


Documentation
-------------

* First, run the tests with nose

    For details on how to install pyqt in a virtual environment that
    closely matches that provided by python xy 2.7.10, see the file: 
   
https://github.com/nharringtonwasatch/BoardTester/blob/master/docs/guiqwt_pythonxy_match.md
