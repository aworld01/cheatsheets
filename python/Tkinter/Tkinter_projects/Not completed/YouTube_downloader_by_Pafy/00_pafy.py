"""pip install pafy"""
import pafy

url = "https://www.youtube.com/watch?v=f2YZf8IygXQ"
data = pafy.new(url)

"""
print(data) #to get below

Title: 
Author:
ID:
Duration:
Rating:
Views:
thumbnail:



print(data.title) #to get title
print(data.author) #to get author name
print(data.duration) #to get duration
print(data.rating) #to fetch rating
print(data.views) #to fetch views
print(data.likes) #to see likes
print(data.dislikes) #to see dislikes
print(data.thumb) #to get url of thumbnail url
print(data.audiostreams) #to list of audio streams
print(data.videostreams) #to list of video streams
print(data.username) #to fetch username
print(data.viewcount) #to fetch viewcount
print(data.streams) #a list of regular streams (streams containing both audio and video)
example:-
    normal = data.streams[0]
    print(normal.download(".")) #to download file


s = data.getbest() #to fetch best video
print(s.extension) #to fetch extension
print(s.get_filesize()) #to fetch filesize
print(s.mediatype) #to fetch filetype
print(s.resolution) #to fetch resolution
print(s.download(".")) #to download file
"""
normal = data.streams[0]
print(normal.download(".")) #to download file



# streams = data.allstreams #to get all streams
# for i in streams:
#     # print(i)
#     # size = i.get_filesize() #to get file size (in Byte)
#     # MegaByte = size / (1024*1024) #to convert into MB
#     # quality = i.quality
#     # extension = i.extension
#     mtype = i.mediatype
#     # print()
#     # print(size)
#     # print(MegaByte)
#     # print(quality)
#     # print(extension)
#     print(mtype)


#vid2- 29:10 / 46:30
