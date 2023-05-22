from PIL import Image, ImageFilter

cat = Image.open("cat.png")

w, h = cat.size
print("Original image size: %sx%s" % (w, h))

# 缩放到50%并另存为:
cat.thumbnail((w // 2, h // 2))
print("Resize image to: %sx%s" % (w // 2, h // 2))
# 模糊效果

cat.filter(ImageFilter.BLUR)

cat.save("small-cat.png", "png")
