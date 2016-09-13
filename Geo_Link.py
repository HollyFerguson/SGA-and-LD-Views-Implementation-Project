#-------------------------------------------------------------------------------
# Name:        Geo_Link.py
# Purpose:     Start program to process geometry data for hard-coding and vocabs
#
# Author:      Holly Tina Ferguson hfergus2@nd.edu
#
# Created:     06/10/2015
# Copyright:   (c) Holly Tina Ferguson 2015
# Licence:     The University of Notre Dame
#-------------------------------------------------------------------------------

# #!/usr/bin/python
import sys
import getopt
import os
from os import path
from file_type import file_type
from term_mapping import term_mapping
from UBO_structure import UBO_structure
from filled_UBO_graph import filled_UBO_graph
from OGCtemplate import OGCtemplate
from OGCtemplate2 import OGCtemplate2
from OGCqueryNfill import OGCqueryNfill
from QueryCurrentVocab import QueryCurrentVocab
from testing import SchemaTest


class Geo_Link():
    # Input parameters
    inputfile = ""


    def run(self):
        """
        Main run function
        """
        self.process_schemas()

        return None


    def process_schemas(self):
        """
        Main Processing Function
        """

        # Only GBXML is filled at this time
        vocab_dict = { "gbxml":'SmartVocabs/gbxmlVocab.ttl', "ifcxml":'SmartVocabs/ifcxmlVocab.ttl', "citygml":'SmartVocabs/citygmlVocab.ttl' }

        # Send file type and return respective term mapping between it and the UBO
        # Also find the source app that created this particular gbXML (use to lift to ontology later)
        step1a = file_type()
        this_file_type, Company, Product, Platform = step1a.schema_type(self.inputfile)
        #print "this_file_type: ", this_file_type, Company, Product, Platform

        # Retrieve the UBO empty structure to fill with the values from the input file
        step2 = UBO_structure()
        UBOgraphStructure = step2.pull_graph_structure()


        ##################################################
        # First Phase of Project Translating To OGC Format

         # Send file type and return respective term mapping between it and the UBO
        step3 = term_mapping()
        mapDict = step3.get_mapping(this_file_type)
        #print "mapDict: ", mapDict

        """
        # Use mapping and the UBO structure to fill the UBO with geometry data
        step3 = filled_UBO_graph()
        UBO_filled, base = step3.fill_graph(this_file_type, mapDict, UBOgraphStructure, self.inputfile)

        # Setup ISO/OGC GeoSPARQL File Template...from: http://www.opengeospatial.org/standards/geosparql
        # Also uses the OGC simple feature documentation (both pdfs in sample_files folder)
        # States that the file type is RDF/XML encoded geometry data, in GeoSPARQL format)
        step4 = OGCtemplate2()
        OGC_RDF_header, OGC_file_parts = step4.createOGCtemplate2(base)
        #step4 = OGCtemplate()
        #OGC_RDF_header, OGC_file_parts = step4.createOGCtemplate(base)

        # Query UBO for data based on map, process coordinates into OGC format, use answers to fill OGC RDF file for output
        step5 = OGCqueryNfill()
        stuff = step5.processUBOforOGC(UBO_filled, base, OGC_RDF_header, OGC_file_parts)

        # Use UBO_filled to answer queries for data within to create respective ISO/OGC GeoSPARQL File
        """
        ##################################################

        ##################################################
        # Second Phase of Project Using Smart Vocabularies

        # Get the associated vocabualry
        current_vocab = vocab_dict[this_file_type]
        print "current_vocab ", current_vocab

        # Commented out to work on adding IFC type
        stepb = QueryCurrentVocab()
        answer = stepb.query_current_vocab(current_vocab, self.inputfile, UBOgraphStructure, this_file_type)

        ##################################################

        ##################################################

        # Testing tags in schema types:
        mytest = SchemaTest()
        #mytest.testing(current_vocab, self.inputfile, this_file_type)
        # Nothing to return since just printing tags to check handling

        return 0



