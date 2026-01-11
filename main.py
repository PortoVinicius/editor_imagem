from image_utils import ImageProcessor

def main():
    input_path = input("Caminho da imagem de entrada: ")

    processor = ImageProcessor(input_path)
    processor.resize_to_192().save_png("icon-192.png")

    print("Imagem convertida com sucesso → icon-192.png")

if __name__ == "__main__":
    main()
