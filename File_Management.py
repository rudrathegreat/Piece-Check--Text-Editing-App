class File_Management(object):

	def save_text(self, data_1 = None, data_2 = None, Frame = None):
	
		data_1.replace('\\', '\\\\')
		full_file_name = data_1 + data_2 + '.txt'
		text = Frame.get(1.0, END)
		
		File = open(full_file_name, 'W')
		File.write(text)
		File.close()
		
		
		