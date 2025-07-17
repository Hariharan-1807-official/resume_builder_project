from jinja2 import Environment, FileSystemLoader
from builder import build_pdf


def collect_entries(section_name):
    entries = []
    while True:
        print(f"\nEnter {section_name} details:")
        title = input("  Title: ")
        place = input("  Organization/Institution: ")
        start = input("  Start Year: ")
        end = input("  End Year (or 'Present'): ")
        description = input("  Description: ")
        entries.append({
            'title': title,
            'place': place,
            'start': start,
            'end': end,
            'description': description
        })
        more = input("Add another? (y/n): ").strip().lower()
        if more != 'y':
            break
    return entries


def main():
    print("📝 Welcome to Resume Builder\n")

    name = input("Full Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    linkedin = input("LinkedIn: ")
    github = input("GitHub: ")

    summary = input("Summary/About You: ")

    skills = input("Skills (comma separated): ").split(',')

    education = collect_entries("Education")

    has_experience = input(
        "Do you have work experience? (y/n): ").strip().lower()
    experience = collect_entries("Experience") if has_experience == 'y' else []

    has_internship = input("Do you have internships? (y/n): ").strip().lower()
    internships = collect_entries(
        "Internship") if has_internship == 'y' else []

    has_projects = input("Do you have projects? (y/n): ").strip().lower()
    projects = collect_entries("Project") if has_projects == 'y' else []

    languages = input("Languages Known (comma separated): ").split(',')

    data = {
        'name': name,
        'email': email,
        'phone': phone,
        'linkedin': linkedin,
        'github': github,
        'summary': summary,
        'skills': [s.strip() for s in skills],
        'education': education,
        'experience': experience,
        'internships': internships,
        'projects': projects,
        'languages': [l.strip() for l in languages]
    }

    build_pdf(data)
    print("\n✅ Resume generated as 'resume.pdf'")


if __name__ == "__main__":
    main()
