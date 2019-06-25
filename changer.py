import os
import pypexels
import requests as rq
py_pexel = pypexels.PyPexels(api_key='API-Key')# Enter your API key here.
i=0
search_results = py_pexel.search(query='programmer', per_page=40)#Enter Query and Number of Images you want to fetch.

while True:
     for photo in search_results.entries:

          img_data = rq.get(photo.src.get('original')).content#Change Quality if you want to. Original is Recommended.
          #You Need To Create Image Library Manually
          with open("Images//" + str(i+1) + ".jpg", 'wb+') as f:
               f.write(img_data)
          print(i,photo.height,photo.width, photo.src.get('original'))
          i=i+1
          cmd = """osascript -e 'tell application "System Events"
          set desktopCount to count of desktops
          tell current desktop 
          set picture to "/Users/roshanchokshi/PycharmProjects/Desktop Changer/Images/{}.jpg" 
          end tell
          end tell'"""

          os.system(cmd.format(i))



