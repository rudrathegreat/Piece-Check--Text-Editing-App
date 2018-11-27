
class File(object):  # This writes the text into a blank file or a used one and closes

    def save_file(self, widget_text=None, filepath=None):
        print("File Create: " + filepath)
        filepath = filepath.replace('\\', '\\\\')
        file1 = open(filepath, "w")
        file1.write(widget_text)
        file1.close()
        print("File Created: " + filepath)
