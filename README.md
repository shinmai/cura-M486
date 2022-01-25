# Marlin M486 - Cancel Object support for Cura  
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This is a Cura G-code Post Processing script to insert Marlin's `M486` G-codes for each object in a multi-object print, and for "non meshes" like prime towers, etc.

To install, copy the **MarlinCancelObject.py** file to you user script directory. On Windows this is **%AppData%\\cura**\\*CURA VERSION NUMBER*\\scripts. Cura needs to be restarted if it's already running. Afterwards, in **Extensions > Post Processing > Modify G-Code** select the **Add a script** button and from the menu that opens choose **Marlin M486 - Cancel Object support**.  
There are no settings or options, the script automagically assigns an ID for all objects and inserts the G-code commands into the sliced file at the correct positions.

This script is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
