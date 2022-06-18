from pytube import YouTube

url=input('Enter your youtube video url: ')
b=YouTube(url)
print(b.title)
print('please wait for a moment your download is in progress')
b=b.streams.get_highest_resolution()
b.download()
print("your download was successful")
