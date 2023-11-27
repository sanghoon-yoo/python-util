from PIL import Image

# 이미지 열기
image = Image.open('C:/Users/sanghoon.yoo/Downloads/2.png')

# 이미지의 특정 픽셀 색상 추출
pixel_color = image.getpixel((1, 1))

# RGB 값을 추출
r, g, b = pixel_color
print(f'RGB: {r}, {g}, {b}')

# RGB 값을 HEX 코드로 변환
hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
print(f'HEX: {hex_color}')
