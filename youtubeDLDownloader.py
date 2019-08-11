fair# ydl_test1_M.py
# To upgrade youtube-dl, run following command:
# sudo pip install --upgrade youtube-dl

# This is a script which I play one or more times a day to download newest podcasts from channels which 
# interest me.  Used to archive podcasts,  in case channels are removed in the future.
# 
# TODO:  Add header info
# TODO:  Separate into class objects
# TODO:  Output downloaded podcast info into separate file to quickly identify daily downloads.


from __future__ import unicode_literals
from youtube_dl.utils import DateRange
import youtube_dl
import json
import os
import os.path

def my_hook(d):
    if d['status'] == 'downloading':
        print(" -- Downloading: {} ".format(os.path.basename(d['filename'])), end='\r')
    if d['status'] == 'finished':
        print("Downloaded: {} ".format(os.path.basename(d['filename'])), end='\n')
		
# Less than date will be downloaded (Currently commented out -- see below)
daterange = DateRange('20170101')        

# File where all downloaded podcast IDs are kept to prevent duplicate downloads  Change to reflect your subdir structure & filename
download_archive   = r"Z:\LR_Extras\!!!_Misc_Downloaded_Podcasts_Scripts\downloaded_files.txt"   

# Output format template -- see youtube-dl notes on github.  Change to reflect your subdir structure
outtmpl            = r"Z:\LR_Extras\!!!_Misc_Downloaded_Podcasts\%(uploader)s\%(playlist_title)s\%(upload_date)s_%(title)s-[%(id)s].%(ext)s" 

ydl_opts = {
    'verbose'           : False, 
    'format'            : '18',  # MP4 output format
    'ignoreerrors'      : True,
    'restrictfilenames' : True,
    'sleep_interval'    : 1,
    'max_sleep_interval': 3,
#   'writethumbnail'    : True,  # writes JPG to output subdir
#   'writedescription'  : True,  # writes description file to output subdir
    'download_archive'  : download_archive,
    
    'outtmpl'           : outtmpl, 
#   'daterange'         : daterange, 

    'playliststart'     : 1,
    'playlistend'       : 20,    # Downloads the latest 20 podcasts/channel
    'playlist-reverse'  : True, 
#   'writesubtitles'    : True,  # writes subtitle, if available, to output subdir
#   'writeautomaticsub' : True,
    'progress_hooks'    : [my_hook]
}


# URL list to download -- can be multiple youtube channels or podcasts, depending on URL -- example of each below.
links = [
  "https://www.youtube.com/watch?v=Z5NzDLvVBdA",           # Single podcast -- specific podcast on channel (Project Veritas)
  "https://www.youtube.com/user/veritasvisuals/videos",    # Latest 20 podcasts on channel (Project Veritas)
    ]  
  
for link in links:                          
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
           ydl.download([link])
        except:
            print('Error in processing')
            pass

