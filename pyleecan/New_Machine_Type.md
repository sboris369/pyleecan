##      Adding a New Machine Type to Pyleecan
This is the process I discoverd thru trial and error, of adding a new machine type to Pyleecan.

If your new to Pyleecan, be sure to watch this video.  
> Pyleecan webinar Contribution - Github projects, Object Oriented Programming.  
  <https://www.youtube.com/watch?v=fseQEwEZdiA>   >
It goes thru the process of getting your repository set up.

After you have your repository set up, make sure you uninstall Pyleecan from
your Python site-packages.  
The reason for this is, if you try to run some of the scripts
in say the Generator folder (like I did)  
Python will give ModuleNotFound Error.   
> ModuleNotFoundError: No module named 'pyleecan.Generator.ClassGenerator'



