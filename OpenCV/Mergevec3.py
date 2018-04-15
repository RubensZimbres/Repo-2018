import sys
import glob
import struct
import argparse
import traceback


def exception_response(e):
	exc_type, exc_value, exc_traceback = sys.exc_info()
	lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
	for line in lines:
		print(line)

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', dest='vec_directory')
	parser.add_argument('-o', dest='output_filename')
	args = parser.parse_args()
	return (args.vec_directory, args.output_filename)

def merge_vec_files(vec_directory, output_vec_file):

	if vec_directory.endswith('/'):
		vec_directory = vec_directory[:-1]

	files = glob.glob('{0}/*.vec'.format(vec_directory))

	if len(files) <= 0:
		print('Vec files to be mereged could not be found from directory: {0}'.format(vec_directory))
		sys.exit(1)
	if len(files) == 1:
		print('Only 1 vec file was found in directory: {0}. Cannot merge a single file.'.format(vec_directory))
		sys.exit(1)


	prev_image_size = 0
	try:
		with open(files[0], 'rb') as vecfile:
			content = b''.join((line) for line in vecfile.readlines())
			val = struct.unpack('<iihh', content[:12])
			prev_image_size = val[1]
	except IOError as e:
		print('An IO error occured while processing the file: {0}'.format(f))
		exception_response(e)


	# Get the total number of images
	total_num_images = 0
	for f in files:
		try:
			with open(f, 'rb') as vecfile:
				content = b''.join((line) for line in vecfile.readlines())
				val = struct.unpack('<iihh', content[:12])
				num_images = val[0]
				image_size = val[1]
				if image_size != prev_image_size:
					err_msg = """The image sizes in the .vec files differ. These values must be the same. \n The image size of file {0}: {1}\n
						The image size of previous files: {0}""".format(f, image_size, prev_image_size)
					sys.exit(err_msg)

				total_num_images += num_images
		except IOError as e:
			print('An IO error occured while processing the file: {0}'.format(f))
			exception_response(e)

	header = struct.pack('<iihh', total_num_images, image_size, 0, 0)
	try:
		with open(output_vec_file, 'wb') as outputfile:
			outputfile.write(header)

			for f in files:
				with open(f, 'rb') as vecfile:
					content = b''.join((line) for line in vecfile.readlines())
					outputfile.write(bytearray(content[12:]))
	except Exception as e:
		exception_response(e)


if __name__ == '__main__':
	vec_directory, output_filename = get_args()
	if not vec_directory:
		sys.exit('mergvec requires a directory of vec files. Call mergevec.py with -v /your_vec_directory')
	if not output_filename:
		sys.exit('mergevec requires an output filename. Call mergevec.py with -o your_output_filename')

	merge_vec_files(vec_directory, output_filename)
	
Source: https://github.com/wulfebw/mergevec
