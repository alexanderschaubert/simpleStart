import os
import shutil

folder_track = "C:\\Users\\alexander.schaubert\\Desktop\\test"
folder_dest = "C:\\Users\\alexander.schaubert\\Desktop\\test1"

class SimpleClass():
    def executeMethode(self, folder_track, folder_dest):
     for filename in os.listdir(folder_track):
      file = folder_track + "\\" +filename
      new_path = folder_dest + "\\" +filename
      shutil.move(file, new_path)


simplesClass = SimpleClass()
simplesClass.executeMethode(folder_track, folder_dest)