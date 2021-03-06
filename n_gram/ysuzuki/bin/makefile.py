#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,os
import math,re,datetime

class Makefile:
    def __init__(self,start_date,end_date,commandstr,funcname,dependencies):
        # make datelist
        self.datelist = list()
        start_date = datetime.datetime.strptime(start_date,"%Y%m%d")
        end_date = datetime.datetime.strptime(end_date,"%Y%m%d")
        days = (end_date - start_date).days
        for i in range(days+1):
            date = start_date + datetime.timedelta(days=i)
            datestr = date.strftime("%Y%m%d")
            self.datelist.append(datestr)

        # setting other attributes
        self.commandstr = commandstr
        #self.outputfilepath = "../works/" + funcname + "/"
        self.donelogfilepath = "../works/log/" + funcname + "/"
        self.makefilename = "makefile/" + funcname
        self.dependencies = dependencies


    def make(self):
        sys.stdout = open(self.makefilename,"w")

        ### header ###
        donelogfilelist = list()
        for date in self.datelist:
            donelogfile = self.donelogfilepath + date + ".done"
            donelogfilelist.append(donelogfile)

        print "all:{}".format(" ".join(donelogfilelist))

        ### main ###
        for date in self.datelist:
            print ""
            ## target(output):dependencies
            #outputfile = self.outputfilepath + date + ".output"
            donelogfile = self.donelogfilepath + date + ".done"
            if isinstance(self.dependencies,list):
                depstr = " ".join(self.dependencies)
                print "{}:{}".format(donelogfile,depstr)
            else:
                print "{}:{}".format(donelogfile,self.dependencies)
        
            ## \t command
            print "\t{} {}".format(self.commandstr,date)

        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    start_date = raw_input("start_date >")
    end_date = raw_input("end_date >")
    commandstr = raw_input("commandstr >")
    funcname = raw_input("funcname >")
    length_dependencies = int(raw_input("length_dependencies >"))
    if length_dependencies > 0:
        dependencies = list()
        for i in range(length_dependencies):
            dependencies.append(raw_input("dependency >"))
    elif length_dependencies == 0:
        dependencies = ""
    print "\n###makefile###\n"
    
    mf = Makefile(start_date,end_date,commandstr,funcname,dependencies)
    mf.make()
