from PIL import Image

class ImageProcessor:
    def __init__(self, input_path):
        self.input_path = input_path
        self.image = Image.open(input_path)

    def resize_to_512(self):
        self.image = self.image.resize((512, 512), Image.LANCZOS)
        return self

    def save_png(self, output_path):
        self.image = self.image.convert("RGBA")
        self.image.save(output_path, format="PNG")
