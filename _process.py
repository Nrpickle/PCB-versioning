'''
Written by Nick McComb (www.nickmccomb.net) June 2018 to organize old files into something usable.


'''


import os
import sys
from collections import defaultdict, OrderedDict
import random

#constants:
fixed_header = "### "
below_fixed_header = "#### "

def format_output(d, index=0):
    global output_string
    global table_of_contents_string
    for k, v in sorted(d.iteritems()):
        if isinstance(v, dict):
            if index == 0:
                print "Project: " + str(k)
                output_string += "# " + str(k) + "\n"
                table_of_contents_string += "* [{}](#{})\n".format(k, k.replace(" ","-").lower())
            if index == 1:
                print "PCB: " + str(k)
                output_string += "## " + str(k) + "\n"
                table_of_contents_string += "  * [{}](#{})\n".format(k, k.replace(" ","-").lower())
            format_output(v, index+1)
        else:
            #print "{0} : {1}".format(k, v)
            random_id_no = random.randint(1, 100000)
            output_string += "<a name=\"{}\"></span>\n".format(random_id_no) + "### Version " + str(k) + "\n"
            output_string += str(v) + "\n"
            output_string += "------------- \n"
            
            #table_of_contents_string += "    * [Version {}](#{})\n".format(k, k.replace(" ","-")) #this doesn't work because they're not unique
            table_of_contents_string += "    * [Version {}](#{})\n".format(k, random_id_no) #this doesn't work because they're not unique


            
walk_dir = "_raw_files"
output_file_name = "README.md"


def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n-1, type))

#Variables that hold output data
output_data = nested_dict(3, str)

print('walk_dir = ' + walk_dir)

output_file = open(output_file_name, "w")
output_string = ""
table_of_contents_string = ""

for root, directories, filenames in os.walk(walk_dir):
    for filename in filenames: 
        target_filename =  os.path.join(root,filename)
        target_filename_list = target_filename.split('\\')
        project_name = str(target_filename_list[1])
        PCB_name = str(target_filename_list[2])
        PCB_version = str(target_filename_list[3].split(' ')[1])
        
        print "Processing Project: " + project_name + "\tPCB: " + PCB_name + "\tVersion: " + PCB_version
        
        #actually read from the target file:
        #print target_filename
        issue_file = open(target_filename,"r")
        
        issue_string = ""

        #Iterate through the file
        for x in issue_file:
            x = x.rstrip()
            if not x: continue
            #check for appropriate headers
            if x[:3] == "___": #then we're probably looking at a fixed header
                #print "Fixed header: ",
                issue_string += "\n" +  fixed_header
                is_fixed_header = True
            elif x[:2] == "__" or x[:1] == "_":
                #print "header: ",
                issue_string += "\n" + below_fixed_header
            else: #We want to add a bullet point
                issue_string += "- "

            x =  x.replace("_", "")
            x = x.lstrip()
            x = x.capitalize()
            #print x
            
            issue_string += x
            issue_string += "\n"
        
        #print "Issues: " + str(" to be filled in later")
        output_data[project_name][PCB_name][PCB_version] = issue_string
        issue_file.close()
        #print ""
        


format_output(output_data)

intro_string = "This github repo parses my internal shorthand for recording issues with my PCBs and generates markdown to make it \"pretty\". Reference [www.nickmccomb.net/pcb](http://www.nickmccomb.net/pcb) for more documentation on the PCBs themselves. \n\n Note that the \"fixed\" notation used in these messages reffers to something being fixed in the next version, and is moved to that category when the next version is being designed.\n"

output_file.write(intro_string)
output_file.write("# Table of Contents \n" + table_of_contents_string + "\n")
output_file.write(output_string)

output_file.close()



