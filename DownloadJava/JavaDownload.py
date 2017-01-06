#!/usr/bin/env python3

# Author: Dipankar Achinta (@tweeting_dipa) [2017]

##############################################################
# Module Import Section.
# Make all the necessary imports here.
##############################################################

# The below two (2) modules take care of Regular Expressions and
# OS level functions in the Python Programming Language.
import re, os

# Get the configuration options for the 
# appropriate `JAVA` package to be downloaded.
import BuildConfig.JavaConfig, BuildConfig.IOConfig

# Currently making use of `URLLIB`.
# Need to make the port to make use of `URLLIB3`.
# Need to plan the code in such a way that it
# doesn't break when making the module upgrade
# to `URLLIB3`.
try:
	from urllib.request import Request, urlopen
except ImportError:
	# This is bound to fail in `PYTHON3` (As no module named `URLLIB2`).
	# Still keeping this as a placeholder.
	# This section needs to be modified when
	# upgrading to `URLLIB3` specification.
	from urllib2 import Request, urlopen

##############################################################
# The section below contains the utility functions,
# that help out in the process for downloading the latest
# `JAVA` "*.tar.gz" package for `JAVA` driven applications.
##############################################################

# Utility Function - 0
def get_link(target_url, link_pattern):
	"""
	Helper function to extract links, necessary
	to locate the correct `JAVA` package. This function
	parses the URL response to extract and follow the links,
	that lead to the "*.tar.gz" JDK/SERVER-JRE/JRE package.
	"""
	request_object  = Request(target_url)
	response_object = urlopen(request_object)
	content_body    = response_object.read().decode('UTF-8')
	response_object.close()
	
	# The below returns either the matched string within
	# the content of the response, or it would return `NONE`
	# meaning it couldn't locate the pattern.
	match_result    = re.search(link_pattern, content_body)
	return match_result

# Utility Function - 1
def download_tar_binary(tar_file_name, tar_request_object):
	"""
	Get the "*.tar.gz" package from the Oracle Download page for
	the intended `JAVA` package. The chore of this utility function
	is to just download the `TAR` package and save it to a file on-disk.
	"""
	# Get the URL response from the supplied link.
	binary_response   = urlopen(tar_request_object)

	# Start the "*.tar.gz" (compressed) binary download.
	with open(tar_file_name, 'wb') as tar_file:
		while True:
			# Read the "*.tar.gz" response in chunks
			tar_chunk = binary_response.read(BuildConfig.IOConfig.CHUNK)
			if not tar_chunk:
				break
			# Write the response chunk to the "target on-disk file".
			tar_file.write(tar_chunk)

# Gateway (or Entry Point) Function - A
def download_java():
	"""
	Perform the latest `JAVA` package download by first extracting the "*.tar.gz" link from
	the returned URI response for the Standard Oracle Download Page and then downloading
	the package for local/shared installation. 
	"""
	# Make the match test for the intended pattern within the URI returned resource.
	match_result        = get_link(BuildConfig.JavaConfig.DOWNLOADS_URL, BuildConfig.JavaConfig.DOWNLOAD_PATTERN)

	# Pretty Self Explanatory.
	# Check the match for `PATTERN::NOT::FOUND`.
	if match_result is None:
		# Enable logging here and abort.
		# We need to update the URI configurations.
		pass

	# Get the `TAR::DOWNLOADS` page to download the "*.tar.gz" link.
	DOWNLOAD_TAR_URL    = BuildConfig.JavaConfig.BASE_URL + match_result.group(0)

	# Make the match test for the intended pattern within the URI returned resource.
	match_result        = get_link(DOWNLOAD_TAR_URL, BuildConfig.JavaConfig.DOWNLOAD_TAR_PATTERN)

	# Again check the match for `PATTERN::NOT::FOUND`.
	if match_result is None:
		# Enable logging here and abort.
		# We need to update the URI configurations.
		pass

	# Prepare the request to download the file.
	# Also, add the necessary headers and cookie information to
	# accept the Oracle Agreement and make the download
	# link available.
	tar_request_object  = Request(match_result.group(0))
	tar_request_object.add_header('Cookie', 'gpw_e24=http://www.oracle.com/;oraclelicense=accept-securebackup-cookie')
	tar_file_name       = os.path.basename(match_result.group(0))

	# Invoke the Download action.
	# Pass in the file-name to use as the download base file and
	# the `REQUEST` object to initiate the request.
	download_tar_binary(tar_file_name, tar_request_object)