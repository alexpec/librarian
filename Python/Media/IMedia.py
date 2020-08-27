




class IMedia(object):
    '''
	A class used to represent a newsfeed

	...

	Properties
	----------
    extraction_date: timestae
        timedate of when the data entered our system
	vehiacle: str
		string of the name of newsfeed vehiacle
	channel: str
		string of which channels the news came from (rss, printed, etc)
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
        pass

    
    def __NotImplementedYet(self, attr_name):
        raise NotImplementedError("%s was not implemented in interface class" %attr_name)


    @property
    def vehiacle(self): self.__NotImplementedYet('vehiacle')
    @vehiacle.setter
    def vehiacle(self, data): self.__NotImplementedYet('vehiacle')

    @property
    def channel(self): self.__NotImplementedYet('channel')
    @channel.setter
    def channel(self data): self.__NotImplementedYet('channel')

    @property
    def author(self): self.__NotImplementedYet('author')
    @author.setter
    def author(self, data): self.__NotImplementedYet('author')

    def save(io_pipeline):
        self.__NotImplementedYet('author')

    def load(io_pipeline):
        self.__NotImplementedYet('author')
    
    

    


    