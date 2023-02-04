from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def add_image(image_path, pdf_canvas, x, y):
    pdf_canvas.drawImage(image_path, x, y, width=100, height=100)

folder_path = "imagens"
images = [f for f in os.listdir(folder_path) if f.endswith(".jpg") or f.endswith(".png")]

pdf_file = "fotograma.pdf"
pdf_canvas = canvas.Canvas(pdf_file, pagesize=letter)
pdf_canvas.setTitle("Fotograma")

x = 50
y = 600
for i in range(0, len(images)):
    image = images[i].rsplit(".", 1)[0]
    add_image(os.path.join(folder_path, images[i]), pdf_canvas, x, y)
    pdf_canvas.drawString(x, y - 20, image)
    x += 150
    if x >= 500:
        x = 50
        y -= 200
        if y < 50:
            y = 600
            pdf_canvas.showPage()
pdf_canvas.save()
