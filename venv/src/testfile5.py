from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

pdf = SimpleDocTemplate("tutorial27.pdf")
flow_obj = []
styles = getSampleStyleSheet()
im_data1 = Image("logo.png", 50, 50)
im_data2 = Image("logo.png", 50, 50)
t = Table([[im_data1]])
flow_obj.append(t)
pdf.build(flow_obj)
