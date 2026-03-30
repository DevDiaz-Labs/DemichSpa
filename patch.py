import re

with open("src/components/Appointment.astro", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the HTML modifications
content = content.replace(
    'class="btn btn-full">Solicitar Cita</button>',
    'class="btn-premium">Solicitar Cita</button>'
)
content = content.replace(
    'class="card-link" style="justify-content: center; font-size:1rem;">Ver en Google Maps &rarr;</a>',
    'class="map-btn">Ver en Google Maps &rarr;</a>'
)

# And now replacing the CSS block for the cards to premium styles
css_target = """  .contact-card {
    background: var(--c-bg-soft);
    padding: 2.5rem 2rem;
    border-radius: 0 0 8px 8px;
    border-top: 3px solid var(--c-primary);
    box-shadow: var(--shadow-sm);
    display: flex;
    flex-direction: column;
  }

  .contact-card h3 {
    margin-bottom: 1rem;
    font-size: 1.5rem;
  }

  .contact-card p {
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
  }

  /* Form Styles */
  .appointment-form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-bottom: 2rem;
  }

  .appointment-form input,
  .appointment-form select {
    width: 100%;
    padding: 0.8rem 1rem;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    font-family: var(--font-body);
    font-size: 0.95rem;
    outline: none;
    transition: border-color 0.2s;
  }

  .appointment-form input:focus,
  .appointment-form select:focus {
    border-color: var(--c-primary);
  }

  .btn-full {
    width: 100%;
    border-radius: 4px;
  }

  .socials p {
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: var(--c-text-main);
  }

  .social-icons {
    display: flex;
    gap: 1rem;
  }

  .social-icons a {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    background: #fff;
    border-radius: 50%;
    color: var(--c-primary);
    box-shadow: var(--shadow-md);
    transition: transform 0.2s, background 0.2s, color 0.2s;
  }

  .social-icons a:hover {
    background: var(--c-primary);
    color: #fff;
    transform: translateY(-3px);
  }

  /* Schedule Styles */
  .schedule-list {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin-top: 1rem;
  }

  .schedule-list li {
    display: flex;
    justify-content: space-between;
    padding-bottom: 0.75rem;
    border-bottom: 1px dashed #e0e0e0;
    font-size: 0.95rem;
    color: var(--c-text-main);
  }

  .schedule-list li:last-child {
    border-bottom: none;
  }

  .schedule-list li span:first-child {
    font-weight: 500;
  }

  .closed {
    color: #e53935;
    font-weight: 600;
  }

  /* Map Styles */
  .map-card {
    padding-bottom: 2.5rem;
  }

  .map-container {
    flex-grow: 1;
    min-height: 250px;
    border-radius: 8px;
    overflow: hidden;
    margin-top: 1rem;
  }

  .card-link {
    font-weight: 600;
    color: var(--c-primary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
  }

  .card-link:hover {
    color: var(--c-primary-hover);
    text-decoration: underline;
  }"""

new_css = """  .contact-card {
    background: #ffffff;
    padding: 3rem 2.5rem;
    border-radius: 20px;
    border: 1px solid rgba(0, 0, 0, 0.03);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.04), 0 2px 10px rgba(0, 0, 0, 0.02);
    display: flex;
    flex-direction: column;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
  }

  .contact-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 25px 50px rgba(212, 175, 55, 0.08), 0 5px 15px rgba(0, 0, 0, 0.03);
  }

  .contact-card h3 {
    margin-bottom: 1rem;
    font-size: 1.6rem;
    font-family: var(--font-heading);
    color: var(--c-text-main);
  }

  .contact-card p {
    font-size: 0.95rem;
    color: var(--c-text-light);
    line-height: 1.6;
    margin-bottom: 2rem;
  }

  /* Form Styles Premium */
  .appointment-form {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    margin-bottom: 2.5rem;
  }

  .appointment-form input,
  .appointment-form select {
    width: 100%;
    padding: 1rem 1.25rem;
    background-color: #f8f9fa;
    border: 1px solid transparent;
    border-radius: 12px;
    font-family: var(--font-body);
    font-size: 0.95rem;
    color: var(--c-text-main);
    outline: none;
    transition: all 0.3s ease;
  }

  .appointment-form input::placeholder {
    color: #a0a0a0;
  }

  .appointment-form input:focus,
  .appointment-form select:focus {
    background-color: #ffffff;
    border-color: rgba(212, 175, 55, 0.5);
    box-shadow: 0 0 0 4px rgba(212, 175, 55, 0.1);
  }

  .btn-premium {
    width: 100%;
    padding: 1.1rem;
    border-radius: 30px;
    font-size: 0.95rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    background: linear-gradient(135deg, var(--c-primary) 0%, #b5952f 100%);
    color: #fff;
    border: none;
    box-shadow: 0 10px 20px rgba(212, 175, 55, 0.3);
    cursor: pointer;
    transition: all 0.3s ease;
  }

  .btn-premium:hover {
    transform: translateY(-2px);
    box-shadow: 0 15px 30px rgba(212, 175, 55, 0.4);
    background: linear-gradient(135deg, #e6ca5d 0%, var(--c-primary) 100%);
  }

  /* Social Icons */
  .socials p {
    font-weight: 600;
    margin-bottom: 0.8rem;
    color: var(--c-text-main);
  }

  .social-icons {
    display: flex;
    gap: 1rem;
  }

  .social-icons a {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 44px;
    height: 44px;
    background: #ffffff;
    border-radius: 50%;
    color: var(--c-primary);
    border: 1px solid rgba(212, 175, 55, 0.15);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    transition: all 0.3s ease;
  }

  .social-icons a:hover {
    background: var(--c-primary);
    color: #ffffff;
    border-color: transparent;
    transform: translateY(-4px);
    box-shadow: 0 10px 20px rgba(212, 175, 55, 0.3);
  }

  /* Schedule Styles Premium */
  .schedule-list {
    display: flex;
    flex-direction: column;
    gap: 0.85rem;
  }

  .schedule-list li {
    display: flex;
    justify-content: space-between;
    padding-bottom: 0.85rem;
    border-bottom: 1px solid #f0f0f0;
    font-size: 0.95rem;
    color: var(--c-text-main);
  }

  .schedule-list li:last-child {
    border-bottom: none;
  }

  .schedule-list li span:first-child {
    font-weight: 600;
    color: var(--c-text-main);
  }

  .closed {
    color: #e53935;
    font-weight: 700;
  }

  /* Map Styles */
  .map-card {
    padding-bottom: 3rem;
  }

  .map-container {
    flex-grow: 1;
    min-height: 250px;
    border-radius: 12px;
    overflow: hidden;
    margin-top: 0.5rem;
    box-shadow: inset 0 2px 10px rgba(0,0,0,0.05);
  }

  .map-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.9rem 2.5rem;
    border: 2px solid var(--c-primary);
    border-radius: 50px;
    color: var(--c-primary);
    font-weight: 600;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    text-decoration: none;
    transition: all 0.3s ease;
  }

  .map-btn:hover {
    background: var(--c-primary);
    color: #fff;
    box-shadow: 0 8px 25px rgba(212, 175, 55, 0.3);
    transform: translateY(-2px);
  }"""

if css_target in content:
    content = content.replace(css_target, new_css)
    with open("src/components/Appointment.astro", "w", encoding="utf-8") as f:
        f.write(content)
    print("Success: Updated CSS.")
else:
    print("Error: CSS target not found.")
