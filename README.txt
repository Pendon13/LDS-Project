#############
### About ###
#############

Program by Jon Pendon
Formulas by Dr. Ara Kahyaoglu, Jaehyeok Yang, Harmit Parmar

This program may be run using web2py.exe. It will prompt a locally hosted server notifcation which is used to administrative purposes.

####################################################
### How to use the program on pythonanywhere.com ###
####################################################

1. Download the code as a ZIP file. (Code -> Download ZIP)
2. Extract the folder to a desired folder.
3. Navigate to .\web2py\applications
4. Send LDS to a compressed folder named LDS.zip
5. Navigate to pythonanywhere.com and create "Add a new web app" on your account
6.Follow the tutorial until "Upload your files" is reached (web2py application)
7. Navigate to your web app's dashboard
8. Scroll down to find the "Source Code" of the web app and click "Go to directory"
9. Navigate to /home/your-username/web2py/applications/
10. Upload the LDS.zip file created earlier
11. Click "Open Bash console here"
12. Type "unzip LDS.zip" and wait until the files are unzipped
13. Navigate to /home/your-username/web2py/
14. Upload routes.py located in the .\web2py folder

At this point the website should be working. Go to "your-username.pythonanywhere.com" to view the website.

##########################
### Editing the photos ###
##########################

1. All molecule images are located under .\web2py\applications\LDS\static\images\2d
2. The file must be saved as a png file named "FormulaInput.png"
   Formula input is what the user will put in the submission box
   I.E. N3^-.png, N3.png
3. Please make a pull request on the GitHub if you wish to add any changes
