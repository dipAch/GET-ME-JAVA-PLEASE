TOMCAT = 'tomcat'

class DownloadManager(object):
	'''
	Class blueprint for creating download agents for the build. These instances/agents will
	handle the entire dependency downloads and target software download for the automated
	build. To make the downloads more time efficient, we are using the `THREADING` module
	that the Python Standard Library provides. This allows us for concurrent downloads
	simultaneously, which when done sequentially takes a lot of time.

	The initialize method, takes as parameter(s): TARGET_BUILD    = [TOMCAT <DEFAULT> | APACHE]
	                                              TARGET_FUNCTION = WORKER_FUNCTION_TO_EXECUTE
	'''
	def __init__(self, target_build=TOMCAT, target_function):
		self.build_target  = target_build
		self.thread_target = target_function

	def begin():
		pass

	def retry():
		pass
	