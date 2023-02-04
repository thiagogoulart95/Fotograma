from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
import os

def add_image(image_path, pdf_canvas, x, y):
    pdf_canvas.drawImage(image_path, x, y, width=200, height=200)

folder_path = "imagens"
images = [f for f in os.listdir(folder_path) if f.endswith(
    ".jpg") or f.endswith(".png")]

pdf_file = "fotograma.pdf"
pdf_canvas = canvas.Canvas(pdf_file, pagesize=landscape(letter))
pdf_canvas.setTitle("Fotograma")

x = 50
y = 400
for i in range(0, len(images)):
    add_image(os.path.join(folder_path, images[i]), pdf_canvas, x, y)
    x += 250
    if x >= 700:
        x = 50
        y -= 250
        if y < 50:
            y = 400
            pdf_canvas.showPage()
pdf_canvas.save()
