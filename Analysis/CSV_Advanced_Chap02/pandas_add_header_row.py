#!/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Data']

data_frame = pd.read_csv(input_file, header=None, names=header_list)

data_frame.to_csv(output_file, index=False)