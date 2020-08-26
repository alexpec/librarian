




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
	save(filename, io_pipeline)
		Saves the news using the specified io pipeline
	load(filename, io_pipeline)
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
		self.published_date = None
		self.updated_date = None
		self.vehiacle = None
		self.channel = None
		self.link = None
		self.summary = None
		self.news = None
		self.author = None
