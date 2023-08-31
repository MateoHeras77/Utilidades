from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.lib import utils
from reportlab.platypus import SimpleDocTemplate, Image as PlatypusImage
import os

def convert_images_to_pdf(image_folder, output_pdf_name):
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        print("No se encontraron imágenes en la carpeta proporcionada.")
        return

    output_pdf_path = os.path.join(image_folder, output_pdf_name)
    doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)

    story = []
    for image_file in image_files:
        img_path = os.path.join(image_folder, image_file)
        img = Image.open(img_path)
        img_width, img_height = img.size

        platypus_img = PlatypusImage(img_path, width=doc.width, height=doc.height, kind='proportional')
        story.append(platypus_img)

    doc.build(story)
    print(f"PDF creado: {output_pdf_path}")

if __name__ == "__main__":
    input_folder = input("Ingrese la ruta de la carpeta de imágenes: ")
    output_pdf_name = input("Ingrese el nombre del archivo PDF de salida (con extensión .pdf): ")

    convert_images_to_pdf(input_folder, output_pdf_name)
