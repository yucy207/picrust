#!/usr/bin/env python
# File created on 22 Feb 2012
from __future__ import division

__author__ = "Greg Caporaso"
__copyright__ = "Copyright 2011, The PICRUST project"
__credits__ = ["Greg Caporaso"]
__license__ = "GPL"
__version__ = "1.4.0-dev"
__maintainer__ = "Greg Caporaso"
__email__ = "gregcaporaso@gmail.com"
__status__ = "Development"
 


from cogent.util.option_parsing import parse_command_line_parameters, make_option
from biom.parse import parse_biom_table
from picrust.predict_metagenomes import predict_metagenomes
from picrust.format import format_biom_table
from picrust.util import make_output_dir_for_file

script_info = {}
script_info['brief_description'] = ""
script_info['script_description'] = ""
script_info['script_usage'] = [("","Predict metagenomes from genomes.biom and otus.biom.","%prog -g genomes.biom -i otus.biom -o predicted_metagenomes.biom")]
script_info['output_description']= ""
script_info['required_options'] = [
 make_option('-i','--input_otu_table',type='existing_filepath',help='the input otu table in biom format'),
 make_option('-g','--input_genome_table',type="existing_filepath",help='the input genome filepath in biom format'),
 make_option('-o','--output_metagenome_table',type="new_filepath",help='the output file for the predicted metagenome'),
 make_option('-f','--format_tab_delimited',action="store_true",default=False,help='output the predicted metagenome table in tab-delimited format [default: %default]')
]
script_info['optional_options'] = []
script_info['version'] = __version__


def main():
    option_parser, opts, args =\
       parse_command_line_parameters(**script_info)
    otu_table = parse_biom_table(open(opts.input_otu_table,'U'))
    genome_table = parse_biom_table(open(opts.input_genome_table,'U'))
    predicted_metagenomes = predict_metagenomes(otu_table,genome_table)

    make_output_dir_for_file(opts.output_metagenome_table)
    if(opts.format_tab_delimited):
        open(opts.output_metagenome_table,'w').write(predicted_metagenomes.delimitedSelf())
    else:
        open(opts.output_metagenome_table,'w').write(format_biom_table(predicted_metagenomes))

if __name__ == "__main__":
    main()
