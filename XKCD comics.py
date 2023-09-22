import requests as req
import os, bs4

# Make Directory to store image
os.makedirs('xkcd', exist_ok=True)

# Start the counter from 1
n = 1

while True:
  # Create the URL for the comic number
  url = 'https://xkcd.com/{}'.format(n)

  # Request the url from the web
  res = req.get(url)

  # Check if the response is successful
  if res.status_code == 200:
    # The request was successful, so parse the HTML
    soup = bs4.BeautifulSoup(res.text)

    # Find the Element that contain the image tag
    comicElem = soup.select('#comic img')

    # If the image tag is found
    if comicElem:
      # Get the URL of the image
      comicUrl = 'http:' + comicElem[0].get('src')

      # Download the image from the URL
      res = req.get(comicUrl)

      # Save the file in the directory
      imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
      for chunk in res.iter_content(1):
        # Writing the binary image file
        imageFile.write(chunk)
      # Closing the binary image file
      imageFile.close()

      # Increment the counter
      n += 1
    else:
      # The image tag was not found, so break the loop
      break
  else:
    # The request was not successful, so break the loop
    break

print('Successfully downloaded all the images')
