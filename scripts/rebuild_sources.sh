#!/bin/bash
#
# run supporting pyuic, pyrcc files to generate resource files and qt
# designer conversions. Run this from the home project directory like:
# WasatchAnalyzeIQ $ ./scripts/rebuild_sources.sh

pyuic4 \
    wasatchanalyzeiq/ui/AnalyzeIQLayout.ui \
    -o wasatchanalyzeiq/ui/AnalyzeIQLayout.py

pyrcc4 \
    wasatchanalyzeiq/ui/wasatchanalyzeiq_resources.qrc \
    -o wasatchanalyzeiq/ui/wasatchanalyzeiq_resources_rc.py
    
