from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.image("vorlage9-Seite1.jpg", x=-4, y=-8, w=217, h=313)

# 1 Freigeschaltet



# 2 Gegen Wiedereinschalten gesichert



# 3 Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle



# 4 Geerdet und kurzgeschlossen



# 5 Mit der Abdeckung soll erreicht werden



pdf.output("elektrische-betriebsmittel.pdf", "F")