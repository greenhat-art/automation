
import os
from dropbox.files import WriteMode



class TransferData:

    def upload_file(self, file_from, file_to):
        

        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_to)
             



    file_from = input("Enter the homework file's path: ")
    file_to = input("Enter the full path of the  homework  directory: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved to the homework directory")

