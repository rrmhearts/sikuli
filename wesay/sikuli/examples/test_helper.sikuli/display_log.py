from __future__ import with_statement
import glob
import os
import platform
import sys
import webbrowser
import subprocess

sys.path.insert(0, '/home/vagrant/Integration-Testing-Framework/sikuli/examples/test_and_log')
from yattag import Doc

#
# Display a log that has been generated by running tests and logging with TestHelper.
#

# Default log folder: /vagrant/log on VM, ./log on HM
pf = platform.platform().lower()
if "win" in pf:
    # In sikuli, use getBundlePath(), otherwise use os.path stuff
    if "java" in pf:
        log_folder = os.path.dirname(getBundlePath()) + "/log"
    else:
        log_folder = os.path.dirname(os.path.realpath(__file__)) + "/log"
elif "lin" in pf:
    log_folder = "/vagrant/log"
else:
    print("lulz, wut os r u using?\n\n*Ahem*\n\nMy most sincere apologies, " +
          "Sir/Ma'am, but I only support Windows and Linux so far.")
    exit(1)

# Make sure the folder exists
if not os.path.exists(log_folder):
    print("Folder not found: " + log_folder + "\n")
    exit(1)

# Make sure there is one and only one .log file in the folder
glob_result_log = glob.glob(log_folder + "/*.log")
if len(glob_result_log) < 1:
    print("No .log file found in folder: " + log_folder + "\n")
    exit(1)
elif len(glob_result_log) > 1:
    print("Multiple .log files found in folder: " + log_folder + "\n")
    exit(1)
else:
    log_file = glob_result_log[0]

# Make sure there is one and only one .css file in the folder
glob_result_css = glob.glob(log_folder + "/*.css")
if len(glob_result_css) < 1:
    print("No css file found in folder: " + log_folder + "\n")
    exit(1)
elif len(glob_result_css) > 1:
    print("Multiple css files found in folder: " + log_folder + "\n")
    exit(1)
else:
    css_file = os.path.basename(glob_result_css[0])

# Build the html log
with open(log_folder + "/log.html", "w") as html_file:
    doc, tag, text = Doc().tagtext()
    doc.asis('<!DOCTYPE html>')

    with tag("html", lang="en_us"):
        with tag("head"):
            with tag("title"):
                text("Test Results")
            doc.stag("link", href=css_file, rel="stylesheet", type="text/css")
        with tag("body"):
            with tag("table"):
                with tag("thead"):
                    with tag("tr"):
			with tag("th"):
                            text("Time and Date")
                        with tag("th"):
                            text("Test name")
                        with tag("th"):
                            text("Action")
                        with tag("th"):
                            text("Expected")
                        with tag("th"):
                            text("Screenshot")
                with tag("tbody"):

                    # Add in the .log file, which should contain table rows
                    with open(log_file, "r") as f:
                        doc.asis(f.read())

    # Write the html document to the file
    html_file.write(doc.getvalue())

# Open a browser tab with the file displayed in it
new = 2  # open in a new tab if possible
url = "file://" + log_folder + "/log.html"
webbrowser.open(url, new=new)