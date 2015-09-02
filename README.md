WasatchAnalyzeIQ
=========

Acquire data from Wasatch Photonics spectrometers for use in AnalyzeIQ

![wasatch analyzeiq screenshot](/docs/wasatch_photonics_analyzeiq_popup.png "wasatch analyzeiq screenshot")

Requirements
------------

  * PyQt 4.7+
  * NumPy

Installation 
--------------------

The instructions are for the default installation location of C:\Analyze IQ V2\.
You may have to change the prefix to match your instllation.

Create the following folder:
<analyzieq>\Common\Instrument\11-WasatchPhotonicsStroker

Copy the entire contents of the build directory:

WasatchAnalyzeIQ\11-WasatchPhotonicsStroker

into the folder:

<analyzieq>\Common\Instrument\11-WasatchPhotonicsStroker


Setup and Rebuilding
--------------------

After modifications have been made, rebuild the wasatchdevice_inst and
wasatchdevice_check executables with the commands:

python wasatchdevice_check_generate.py py2exe
python wasatchdevice_inst_generate.py py2exe

Copy the entire contents of the build directory:

WasatchAnalyzeIQ\11-WasatchPhotonicsStroker

into the folder:

<analyzieq>\Common\Instrument\11-WasatchPhotonicsStroker

To package up for redistribution, create a zip file with the name:
11-WasatchPhotonicsStroker.zip


Documentation
-------------

* First, run the tests with nose

    For details on how to install pyqt in a virtual environment that
    closely matches that provided by python xy 2.7.10, see the file: 
   
https://github.com/nharringtonwasatch/BoardTester/blob/master/docs/guiqwt_pythonxy_match.md
