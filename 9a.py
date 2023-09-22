# import requests
# from bs4 import BeautifulSoup
# import os

# url='https://xkcd.com/'
# r = requests.get(url)
# print(r.status_code) #optional
# print(r.content) #optional
# htmldoc = BeautifulSoup(r.content, "html.parser")
# # print(htmldoc.pritify())
# imgdiv = htmldoc.find("div", class_="box")
# imgcontent = imgdiv.find_all('img')
# imgurl = url+imgcontent[0].get("src")
# comic=requests.get(imgurl)
# imgfile=open('a899e84.jpg',"src")
# for chunk in comic.iter_content(1000):
#     imgfile.write(chunk)
# imgfile.close()
#fka
import requests
from bs4 import BeautifulSoup
import os

url = "https://xkcd.com/"

# Make a request to the XKCD website and get the response
response = requests.get(url)

# Check the status code of the response
if response.status_code == 200:
  # The request was successful, so parse the HTML
  html_doc = BeautifulSoup(response.content, "html.parser")

  # Find the `div` element with the class `box`
  img_div = html_doc.find("div", class_="box")

  # Find all `img` elements in the `div` element
  img_content = img_div.find_all("img")

  # Get the URL of the first `img` element
  img_url = 'http:' + url+ img_content[0].get('src')


  # Download the image from the URL
  image = requests.get(img_url)

  # Save the image to a file
  with open("xkcd.png", "wb") as file:
    file.write(image.content)

else:
  # The request was not successful
    print("Error: The request to the XKCD website failed.")
