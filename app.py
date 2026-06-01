import streamlit as st

# Set page configuration
st.set_page_config(page_title="Instant Portfolio Builder", page_icon="🚀", layout="centered")

st.title("🚀 Instant Portfolio Builder")
st.write("Fill in your details below to instantly generate and download your personal portfolio website.")

st.divider()

# --- INPUT SECTION ---
st.header("1. Enter Your Details")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Full Name", "John Doe")
    email = st.text_input("Email Address", "john.doe@example.com")
with col2:
    role = st.text_input("Job Title / Role", "Software Developer")
    github = st.text_input("GitHub/LinkedIn URL", "https://github.com/")

bio = st.text_area("About Me (Bio)", "I am a passionate developer who loves building cool things with code.")
skills = st.text_area("Skills (Comma-separated)", "Python, JavaScript, HTML, CSS, React")

st.subheader("Projects")
st.write("Format: `Project Name | Description` (one project per line)")
projects_input = st.text_area("Your Projects", "Portfolio Builder | A python app to generate websites\nE-commerce Site | A full-stack online store")

# --- PROCESS DATA ---
# Convert skills string to a list
skills_list = [skill.strip() for skill in skills.split(',') if skill.strip()]

# Convert projects string to a list of dictionaries
projects_list = []
for line in projects_input.split('\n'):
    if '|' in line:
        p_name, p_desc = line.split('|', 1)
        projects_list.append({"name": p_name.strip(), "desc": p_desc.strip()})
    elif line.strip():
        projects_list.append({"name": line.strip(), "desc": ""})

# --- HTML/CSS TEMPLATE ---
def generate_html():
    # Format skills into HTML spans
    skills_html = "".join([f"<span class='skill-tag'>{skill}</span>" for skill in skills_list])
    
    # Format projects into HTML cards
    projects_html = "".join([
        f"<div class='project-card'><h3>{p['name']}</h3><p>{p['desc']}</p></div>" 
        for p in projects_list
    ])

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{name} | {role}</title>
        <style>
            :root {{
                --primary: #2563eb;
                --bg: #f8fafc;
                --text: #1e293b;
            }}
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background-color: var(--bg);
                color: var(--text);
                line-height: 1.6;
            }}
            .container {{
                max-width: 800px;
                margin: 0 auto;
                padding: 2rem;
            }}
            header {{
                text-align: center;
                padding: 4rem 0;
                background: white;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                border-radius: 0 0 20px 20px;
                margin-bottom: 2rem;
            }}
            h1 {{ margin: 0; font-size: 2.5rem; color: var(--primary); }}
            h2 {{ color: var(--text); font-weight: 400; }}
            .section-title {{
                border-bottom: 2px solid var(--primary);
                display: inline-block;
                padding-bottom: 0.5rem;
                margin-top: 2rem;
            }}
            .skill-tag {{
                display: inline-block;
                background: var(--primary);
                color: white;
                padding: 0.5rem 1rem;
                border-radius: 999px;
                margin: 0.25rem;
                font-size: 0.9rem;
            }}
            .project-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1rem;
                margin-top: 1rem;
            }}
            .project-card {{
                background: white;
                padding: 1.5rem;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                border-top: 4px solid var(--primary);
            }}
            .project-card h3 {{ margin-top: 0; }}
            .contact {{ text-align: center; margin-top: 4rem; padding-bottom: 2rem; }}
            a {{ color: var(--primary); text-decoration: none; font-weight: bold; }}
            a:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        <header>
            <div class="container">
                <h1>{name}</h1>
                <h2>{role}</h2>
                <p>{bio}</p>
            </div>
        </header>

        <div class="container">
            <h2 class="section-title">Technical Skills</h2>
            <div>{skills_html}</div>

            <h2 class="section-title">Projects</h2>
            <div class="project-grid">
                {projects_html}
            </div>

            <div class="contact">
                <h2>Let's Connect!</h2>
                <p>Email: <a href="mailto:{email}">{email}</a></p>
                <p>Links: <a href="{github}" target="_blank">My Profile</a></p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

# Generate the HTML string based on current inputs
final_html = generate_html()

st.divider()

# --- PREVIEW & DOWNLOAD SECTION ---
st.header("2. Preview & Download")

# Use an expander to show the raw HTML code if the user wants to see it
with st.expander("👀 View Raw HTML Code"):
    st.code(final_html, language='html')

# Render the download button
st.download_button(
    label="⬇️ Download My Portfolio (index.html)",
    data=final_html,
    file_name="index.html",
    mime="text/html",
    use_container_width=True
)

st.success("Click the button above to download your standalone `index.html` file. You can open it in any web browser or host it on GitHub Pages, Netlify, or Vercel for free!")