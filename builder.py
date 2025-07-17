from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def build_pdf(data):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("template.html")
    html_out = template.render(data=data)

    with open("resume.html", "w", encoding='utf-8') as f:
        f.write(html_out)

    HTML("resume.html").write_pdf("resume.pdf", stylesheets=["style.css"])
