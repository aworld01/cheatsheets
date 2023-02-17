from PIL import Image

imported = "ohmsLaw.jpg"
export = "compressed1.jpg"
q_per = 30

def compressed(path, output, per):
    picture = Image.open(path)
    picture.save(output, "JPEG", optimize=True, quality=per)

compressed(imported, export, q_per)
