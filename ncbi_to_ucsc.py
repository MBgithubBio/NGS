import sys


#argv[1]:txt file includes the NCBI code for each chromosem. you can install this file from NCBI (https://www.ncbi.nlm.nih.gov/assembly/GCF_000003025.6/)

#make dictionary the key is NCBI chromosome code and the value is chr1,chr2,chr2 code
dict_chromsomes={}
with open(sys.argv[1], 'r') as input_file:
	for items in input_file:
		items=items.strip().split('\t')
		if items[0].startswith("C"):
			chromsome=items[0]+items[1]
			dict_chromsomes[items[2]]=chromsome


#argv[2]:your input .sam file
#argv[3]:your modifeid output .sam file
with open(sys.argv[2], 'r') as input_file, open(sys.argv[3], 'w') as output_file:
    # Iterate over each line in the input file
    for line in input_file:
		if line[0]!="@":
        # Split the line into fields separated by tabs
        		fields = line.strip().split('\t')
        # Check if the second field starts with "NC_"
	        	if fields[2].startswith('NC_'):
            # Replace the "NC_" prefix with "chr"
            			fields[2] = dict_chromsomes[fields[2]]

            # Join the fields back together with tabs and write to the output file
          		 	output_file.write('\t'.join(fields) + '\n')
		else:
            # If the first field doesn't start with "NC_", write the line as-is to the output file (to inclide the header of .sam file)
            		output_file.write(line)

