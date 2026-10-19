# Portfolio — Raghavendra Rongali

This repository contains a Streamlit-based personal portfolio/resume web app for Raghavendra Rongali. It displays a summary, skills, experience, projects, and contact information with a responsive card layout.

## Features

- Single-file Streamlit app (`app.py`) that renders a styled resume/portfolio.
- Responsive project cards rendered row-wise (2 per row).
- Custom CSS for headings, cards, and footer styling.
- Sidebar with profile image and contact links.

## Requirements

- Python 3.8+
- Packages:
	- `streamlit`
	- `Pillow`

Install requirements with:

```bash
pip install streamlit pillow
```

## Run Locally

From the repository root run:

```bash
streamlit run app.py
```

Open the printed local URL in your browser (usually `http://localhost:8501`).

## Files

- `app.py` — Main Streamlit app.
- `README.md` — This file.
- `My photo official.jpg` — Sidebar profile image (place in repo root).

## Notes

- If you update project cards or experience sections, keep text blocks as plain markdown to ensure consistent rendering.
- For layout tweaks, adjust CSS in `app.py` or change `st.columns` widths.

If you want, I can also create a `requirements.txt` and run the app locally to verify the layout.
