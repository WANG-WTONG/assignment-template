import pygame
import requests
import io
import sys


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Image Bot')

def fetch_image_from_web(keyword):
    
    url = f"https://api.pexels.com/v1/search?query={keyword}&per_page=1"
    headers = {
        "Authorization": "92eJwZkM1xfqjeplRLL9tUaQF5m3ol7QvrMVcBnlnuRlKkeYawbuhixx"  
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data['photos']:
            image_url = data['photos'][0]['src']['medium']
            image_response = requests.get(image_url)
            return io.BytesIO(image_response.content)
        else:
            print("No images found.")
            return None
    else:
        print("Image not found.")
        return None

def main():
    running = True
    image = None

   
    keyword = input("Enter a keyword to generate an image: ").lower()
    image_data = fetch_image_from_web(keyword)

    if image_data:
        image = pygame.image.load(image_data)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        if image:
            screen.blit(image, (100, 100))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()