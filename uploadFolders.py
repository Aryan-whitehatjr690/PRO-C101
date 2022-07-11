import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                localPath=os.path.join(root,fileName)
                relative_path=os.path.relpath(localPath, file_from)
                dropbox_path=os.path.join(file_to, relative_path)
                with open(localPath,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))
def main():
    access_token='sl.BLOqqnRPfYKesaqkyvN-CVzmYXWHymD2akj8kSTp2kvHMnVH6Ig31-eZ8MxosxbXsHM3WivbUF2MU3CMtih7awKrGNf0H5_GQ1lLnj6IORGjRLGd9M5NnRh6kiZb36jCk3Ah3nE'
    transferData=TransferData(access_token)
    fileFrom=input("Enter the folder path to transfer: ")
    fileTo=input("Enter the full path to upload to dropbox: ")
    transferData.upload_file(fileFrom,fileTo)
    print("File Successfuly Transfered.")
main()