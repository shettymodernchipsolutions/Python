"""
***How to Install Python IDE:?
STEP 1) Select Version of Python to Install
The installation procedure involves downloading the official Python .exe installer and running it on your system.
The version you need depends on what you want to do in Python.
STEP 2) Download Python Executable Installer
Open your web browser and navigate to the Downloads for Windows section of the official Python website.
Search for your desired version of Python. At the time of publishing this article, the latest Python 3 release is version 3.7.3, while the latest Python 2 release is version 2.7.16.
Select a link to download either the Windows x86-64 executable installer or Windows x86 executable installer. The download is approximately 25MB.
STEP 3) Run Executable Installer
1. Run the Python Installer once downloaded.
2. Make sure you select the Install launcher for all users and Add Python 3.7 to PATH checkboxes. The latter places the interpreter in the execution path. For older versions of Python that do not support the Add Python to Path checkbox, see Step 6.
3. Select Install Now – the recommended installation options.
4. The next dialog will prompt you to select whether to Disable path length limit. Choosing this option will allow Python to bypass the 260-character MAX_PATH limit. Effectively, it will enable Python to use long path names.
STEP 4) Verify Python Was Installed On Windows
Navigate to the directory in which Python was installed on the system.
In our case, it is C:\Users\Username\AppData\Local\Programs\Python\Python37 since we have installed the latest version.
Double-click python.exe.
STEP 5) Verify Pip Was Installed
If you opted to install an older version of Python, it is possible that it did not come with Pip preinstalled. Pip is a powerful package management system for Python software packages. Thus, make sure that you have it installed.
We recommend using Pip for most Python packages, especially when working in virtual environments.
To verify whether Pip was installed:
Open the Start menu and type "cmd."
Select the Command Prompt application.
Enter pip -V in the console. If Pip was installed successfully
Pip has not been installed yet if you get the following output:
'pip' is not recognized as an internal or external command,
Operable program or batch file.
Step 6) Add Python Path to Environment Variables (Optional)
We recommend you go through this step if your version of the Python installer does not include the Add Python to PATH checkbox or if you have not selected that option.
Setting up the Python path to system variables alleviates the need for using full paths. It instructs Windows to look through all the PATH folders for “python” and find the install folder that contains the python.exe file.
1. Open the Start menu and start the Run app.
2. Type sysdm.cpl and click OK. This opens the System Properties window.
3. Navigate to the Advanced tab and select Environment Variables.
4. Under System Variables, find and select the Path variable.
5. Click Edit.
6. Select the Variable value field. Add the path to the python.exe file preceded with a semicolon (;).
For example, in the image below, we have added ";C:\Python34."
7. Click OK and close all windows.
By setting this up, you can execute Python scripts like this: Python script.py
Instead of this: C:/Python34/Python script.py
Step 7) Install virtualnv (Optional)
You have Python, and you have Pip to manage packages. Now, you need one last software package - virtualnv. Virtualnv enables you to create isolated local virtual environments for your Python projects.
**Why use virtualnv?
Python software packages are installed system-wide by default. Consequently, whenever a single project-specific package is changed, it changes for all your Python projects. You would want to avoid this, and having separate virtual environments for each project is the easiest solution.
**To install virtualnv:
1. Open the Start menu and type "cmd."
2. Select the Command Prompt application.
3. Type the following pip command in the console:
C:\Users\Username> pip install virtualenv
**VERIFYING:
To try to verify installation,
1. Navigate to the directory C:\Users\Pattis\AppData\Local\Programs\Python\Python39
(or to whatever directory Python was installed: see the pop-up window for Installing step 1).
Double-click the icon/file python.exe
2.A pop-up window with the title C:\Users\Pattis\AppData\Local\Programs\Python\Python39\python.exe appears, and inside the window
on the first line is the text Python 3.9.6 ...
(notice that it should also say 64 bit). Inside the window, at the bottom left, is the prompt >>>:
type exit() to this prompt and press enter to terminate Python.
"""


'''
INSTALLATION OF PYCHARM:?
Step 1.
Download PyCharm from the JetBrains website. You will have the option of using the Professional version or the Community version. This guide installs the Community edition.
 Note: It is also a good idea to confirm that Python is installed.
Step 2.
After running the installer, select the installation location.
The most common location is in our Program Files directory, but this can be changed to an alternative location if needed, but this is usually unnecessary
Step 3.
Next, we will be prompted to select our installation options.
These include the option to add a desktop shortcut, updating your path to include PyCharm launcher along with any associating file types, and a context menu. You can see below the choices I have selected for my installation.
Feel free to choose what is best for your development style.
Step 4.
The next step is to choose your start menu folder location, for a quick reference from your desktop start page.
Step 5.
Now, we wait for PyCharm to install.
If you wish to see additional details of the installation, you can select show details.
Step 6.
Finally, reboot the computer at the end of the PyCharm installation process.
---------------------------------------------*****---------------------------------------------------------------------
**How Do I Configure PyCharm?
Step 1.
When we open PyCharm the first time, we will initially be prompted with featured plugins we can download to emulate a Vim editor, R language support, or an AWS Toolkit. A more detailed plugin list is available in settings.
Feel free to install and enable the ones that best suit your needs.
Step 2.
From the main screen, we can create a new project, open an existing one
or select one from our versioning control system of choice, like GIT.
We can also see the configuration options in the bottom right corner
and ask for help which can be useful in moving forward.
Step 3.
When creating a new project, we will be asked a few questions like where would we like to place our project folder and any related files which need to be saved.
Or, whether we would like a main.py created by default
and other Python interpreter options unique to our environment.
If you did not install Python before installing PyCharm, you will get a warning
-------------------------------------------****-----------------------------------------------------------------------------------'''




