from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch


def create_resume(
        name,
        email,
        phone,
        linkedin,
        github,
        summary,
        skills="",
        education="",
        projects="",
        certifications="",
        output_file="ATS_Resume.pdf"
):
    

    doc = SimpleDocTemplate(
        output_file,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title = styles["Title"]
    title.alignment = TA_CENTER
    title.fontSize = 22
    title.leading = 26
    title.textColor = HexColor("#0B5394")

    heading = styles["Heading2"]
    heading.textColor = HexColor("#0B5394")

    normal = styles["BodyText"]
    normal.leading = 18

    story = []

    # =====================
    # NAME
    # =====================

    story.append(Paragraph(f"<b>{name}</b>", title))
    story.append(
        Paragraph(
            f"{email} | {phone}<br/>{linkedin} | {github}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%"))
    story.append(Spacer(1, 12))

    # =====================
    # SUMMARY
    # =====================

    story.append(Paragraph("Professional Summary", heading))
    story.append(Paragraph(summary, normal))
    story.append(Spacer(1, 12))

    # =====================
    # SKILLS
    # =====================

    if skills.strip():
        story.append(Paragraph("Technical Skills", heading))

        skill_text = "<br/>".join(
            [f"• {x.strip()}" for x in skills.split(",") if x.strip()]
        )

        story.append(Paragraph(skill_text, normal))
        story.append(Spacer(1, 12))

    # =====================
    # EDUCATION
    # =====================

    if education.strip():
        story.append(Paragraph("Education", heading))
        story.append(Paragraph(education, normal))
        story.append(Spacer(1, 12))

    # =====================
    # PROJECTS
    # =====================

    if projects.strip():
        story.append(Paragraph("Projects", heading))

        for p in projects.split("\n"):
            if p.strip():
                story.append(Paragraph(f"• {p}", normal))

        story.append(Spacer(1, 12))

    # =====================
    # CERTIFICATIONS
    # =====================

    if certifications.strip():
        story.append(Paragraph("Certifications", heading))

        for c in certifications.split("\n"):
            if c.strip():
                story.append(Paragraph(f"• {c}", normal))

        story.append(Spacer(1, 12))

    doc.build(story)

    return output_file