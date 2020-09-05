




class BasicFile(object):
    '''
	A class used to save or load a file.

	...
	
	Methods
	-------
	save()
		Saves the news using the specified io pipeline
	load()
		Loads the news using the specified io pipeline
    set_filename()
        Sets the filename that will be used

	'''

	def __init__(self, filename):
		'''
		Attributes
		----------
		'''
        if filename == None:
            raise RuntimeError('Filename must not be null')


        self.__filename = filename
        self.__filehandler = None

    @property
    def filename(self): return self.__filename
    @filename.setter
    def filename(self, data): 
        raise AttributeError('Filename is not supposed to be assigned after initialization')

    def _verify_handler(self):
        handler = self.__filehandler
        if handler not None:
            raise RuntimeError('Handler already opened. Calls close() method.')
        else:
            return True


	def save(self):
        if self._verify_handler():
            self.__filehandler = open(self.filename, 'w')
            return self.__filehandler
    
    def load(self):
        if self._verify_handler():
            self.__filehandler = open(self.filename, 'r')
            return self.__filehandler

    def close(self):
        try:
            self.__filehandler.close()
        except:
            raise RuntimeError('File handler unespected error!')

        self.__filehandler = None