




class News(object):
	'''
	A class used to represent a newsfeed

	...

	Attributes
	----------
	published_date: timedate
		timedate of the publication date
	updated_date: timedate
		timedate of the update date (when available)
	vehiacle: str
		string of the name of newsfeed vehiacle
	channel: str
		string of which channels the news came from (rss, printed, etc)
	link: str
		string representing the link (when available)
	summary: str
		string representing the introductory text (when available)
	news: str
		string containing the full text
	author: str
		news author (when available - otherwise the vehiacle)


	Methods
	-------
	save(io_pipeline)
		Saves the news using the specified io pipeline
	load(io_pipeline)
		Loads the news using the specified io pipeline

	'''

	published_date = None
	updated_date = None
	vehiacle = None
	channel = None
	link = None
	summary = None
	news = None
	author = None


	def __init__(self):
		'''
		Parameters
		----------
		
		'''

		self.published_date = None
		self.updated_date = None
		self.vehiacle = None
		self.channel = None
		self.link = None
		self.summary = None
		self.news = None
		self.author = None


	def save(self, io_pipeline):
		'''
		Saves the class into a pipeline (database, file, rest get method, etc)


		Parameters
		----------
		io_pipeline: IPipeline
			The pipeline which will be used to save the data in the class
		'''
		pass
