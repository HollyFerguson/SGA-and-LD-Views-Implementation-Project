#-------------------------------------------------------------------------------
# Name:        file_type.py
# Purpose:     Determine the XML schema data that was just passed as program input
#
# Author:      Holly Tina Ferguson hfergus2@nd.edu
#
# Created:     06/10/2015
# Copyright:   (c) Holly Tina Ferguson 2015
# Licence:     The University of Notre Dame
#-------------------------------------------------------------------------------

# #!/usr/bin/python
from lxml import etree
import sys
import os


class file_type():
    # Input parameters
    tree = None
    # May change as additional file options get entered into the mix
    namespaces = {'gb': "http://www.gbxml.org/schema"}


    def schema_type(self, inputfile):
        """
        Check file extensions to determine schema type
        """
        fileType = None
        struct = None

        fileExtension = inputfile.split(".")[-1]
        #print "ext: ", fileExtension

        if fileExtension == "ifcxml":
            fileType = "ifcxml"
        elif fileExtension == "gbxml":
            fileType = "gbxml"
        elif fileExtension == "citygml?":
            fileType = "citygml"
        elif fileExtension == "xml":
            # File is an xml but may still be a gbxml since those extensions are just xml
            # Open/parse the file to check if it is still a gbxml or unhandled type at this time
            self.tree = etree.parse(inputfile)
            struct = self.tree
            gbxmls = self.tree.xpath("/gb:gbXML", namespaces=self.namespaces)
            if not gbxmls:
                fileType = None
            else:
                fileType = "gbxml"
        else:
            fileType = "not yet handled"

        Company, Product, Platform = self.souce_application_data(struct, fileType)
        #print "SourceDetials: ", Company, Product, Platform

        return fileType, Company, Product, Platform

    def souce_application_data(self, struct, this_file_type):
        """
        Check gbxml for source OS, Company, and Generating Application
        """
        Company = ""
        Product = ""
        Platform = ""

        #surfaces = struct.xpath("/gb:gbXML/gb:Campus/gb:Surface", namespaces=self.namespaces)
        #for surface in surfaces:
        #    cad = str(surface.xpath("./gb:CADObjectId", namespaces=self.namespaces)[0].text)
        #    print "cad: ", cad

        if this_file_type == "gbxml":
            DocumentHistory = struct.xpath("/gb:gbXML/gb:DocumentHistory/gb:ProgramInfo", namespaces=self.namespaces)
            for item in DocumentHistory:
                Company = str(item.xpath("./gb:CompanyName", namespaces=self.namespaces)[0].text)
                Product = str(item.xpath("./gb:ProductName", namespaces=self.namespaces)[0].text)
                Platform = str(item.xpath("./gb:Platform", namespaces=self.namespaces)[0].text)

        return Company, Product, Platform
