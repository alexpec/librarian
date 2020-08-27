from librarian.Media.IMedia import IMedia




class News(IMedia):
	'''
	A class used to represent a newsfeed

	...

	Properties
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
	content: str
		string representing the content of the news
	author: str
		news author (when available - otherwise the vehiacle)


	Methods
	-------
	save(io_pipeline)
		Saves the news using the specified io pipeline
	load(io_pipeline)
		Loads the news using the specified io pipeline

	'''

	def __init__(self):
		'''
		Attributes
		----------
		'''

		self.published_date = None
		self.updated_date = None
		self.vehiacle = None
		self.channel = None
		self.author = None
		self.link = None
		self.content = None

	
	@property
	def published_date(self): return self.__published_date
	@published_date.setter
	def published_date(self, data): self.__published_date = data

	@property
	def updated_date(self): return self.__published_date
	@updated_date.setter
	def updated_date(self, data): self.__published_date = data
	
	@property
    def vehiacle(self): return self.__vehiacle
    @vehiacle.setter
    def vehiacle(self, data): self.__vehiacle = data

    @property
    def channel(self): return self.__channel
    @channel.setter
    def channel(self data): set.__channel = data

    @property
    def author(self): return self.__author
    @author.setter
    def author(self, data): self.__author = data

	@property
	def link(self): return self.__link
	@link.setter
	def link(self, data): self.__link = data

	@property
	def content(self): return self.__content
	@content.setter
	def content(self, data): self.__content = data