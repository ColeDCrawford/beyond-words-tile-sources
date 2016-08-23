import sys, getopt, os
from deepzoom import deepzoom

usage_msg = "Usage: python image_converter.py -i <input_file/dir> -o <output_dir>\n\
Dependency: deepzoom (https://github.com/openzoom/deepzoom.py)"
info_msg = "Info: No output directory specified. Default \"output\" directory will be used."
notfound_msg = "Error: No file or directory found named: "

if __name__ == "__main__":
	argv = sys.argv[1:]
	input_path = ''
	output_path = ''
	try:
		opts, args = getopt.getopt(argv,"i:o:")
	except getopt.GetoptError:
		print(usage_msg)
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-i':
			input_path = arg
		elif opt == '-o':
			output_path = arg
		else:
			print(usage_msg)

	if input_path == '':
		print(usage_msg)
		sys.exit()

	if output_path == '':
		print(info_msg)
		output_path = "output"

	creator = deepzoom.ImageCreator()

	if os.path.isdir(input_path):
		files = os.listdir(input_path)
		for file_name in files:
			input_filename = os.path.join(input_path, file_name)
			if os.path.isfile(input_filename):
				output_filename = os.path.join(output_path, file_name + '.dzi')
				print "Creating .dzi for image at " + input_filename
				creator.create(input_filename, output_filename)
				print(input_filename + "--->" + output_filename)

	elif os.path.isfile(input_path):
		input_filename = input_path
		output_filename = os.path.join(output_path, input_path + '.dzi')
		print "Creating .dzi for image at " + input_filename
		creator.create(input_filename, output_filename)
		print(input_filename + "--->" + output_filename)

	else:
		print(notfound_msg + input_path);
