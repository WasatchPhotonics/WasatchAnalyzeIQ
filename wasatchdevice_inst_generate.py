""" wasatchdevice_generate - called by py2exe to create an executable version of
the wasatchdevice.py application. This is based heavily on:
http://ralsina.me/weblog/posts/BB955.html

See the README for instructions on how to package this output for use with
analyzeiq.
"""

from distutils.core import setup
import py2exe

setup(console=["scripts\wasatchdevice_inst.py"],
      options={"py2exe": {

                            "dll_excludes": [ "MSVCP90.dll", "MSWSOCK.dll",
                                              "mswsock.dll", "powrprof.dll",
                                              "w9xpopen.exe",
                                            ],

                            "includes": [ "sip", 
                                          "wasatchusb",
                                          "wasatchanalyzeiq",
                                        ],


                            "excludes": ["pywin", "pywin.debugger", "pywin.debugger.dbgcon",
                                         "pywin.dialogs", "pywin.dialogs.list",
                                         "Tkconstants","Tkinter","tcl", 
                                         "wx", "scipy", "matplotlib",
                                        ],
               
                            "bundle_files": 1,
 
                            "dist_dir": "11-WasatchPhotonicsStroker",
                          },


              },

       data_files = ["scripts\\emulator.inst"],
       zipfile=None
     )

