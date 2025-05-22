from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name="I"):
        if not name:
            raise ValueError("Name cannot be empty.")
        super().__init__(orientation="portrait", unit="mm", format="A4")
        self.name = name.strip().title()

    def generate(self, output_path="shirtificate.pdf"):
        self.add_page()
        self.add_text()
        self.output(output_path)

    def header(self):
        self.set_font("helvetica", size=32)
        self.cell(0, 30, "CS50 Shirtificate", align="C")
        self.image("shirtificate.png", x=10, y=40, w=190)

    def add_text(self):
        self.set_font("helvetica", size=24)
        self.set_text_color(255, 255, 255)
        self.set_y(105)
        self.cell(0, 10, f"{self.name} took CS50", align="C")



def main():
    name = PDF(input("Name: "))
    name.generate()


if __name__ == "__main__":
    main()