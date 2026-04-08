# EventMaster Pro

Professional event budget planner built with Streamlit and a custom web interface.

The application is designed for planners who need fast quote assembly, clean financial visibility, and polished client-facing output.

## Live Application

https://orcamento-eventos-pro.streamlit.app/

## Documentation

- Beginner-friendly bilingual code guide (PT-BR / EN): [GUIA_DO_CODIGO_PT_EN.md](GUIA_DO_CODIGO_PT_EN.md)

## Key Capabilities

- Centralized event setup (client/event name and event type)
- Service-based quote builder with editable line items
- Flat-rate and installment calculations with monthly interest
- Real-time total and remaining balance against available budget
- PDF proposal export for sharing with clients
- Session persistence in browser localStorage for quick continuity
- Responsive premium UI for desktop and mobile

## Technology Stack

### Backend / App Host

- Python 3
- Streamlit 1.56.0

### Frontend Layer (embedded in Streamlit)

- HTML5 + CSS3
- JavaScript (Vanilla)
- Tailwind CSS (CDN)
- Font Awesome 6 (icons)
- Google Fonts

### Document Generation

- jsPDF
- jsPDF-AutoTable

### Runtime / Data

- Browser localStorage for session and quote state
- Unsplash assets for curated visual media

### Python Dependencies

- streamlit

## Project Structure

- `app_noiva.py`: Main production app (Streamlit + embedded HTML/CSS/JS)
- `EventMaster.py`: Alternate app entry/module in repository
- `app_noiva_backup.py`: Backup snapshot for recovery/reference
- `requirements.txt`: Python dependencies

## Running Locally

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Start Streamlit.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app_noiva.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

## Recent Improvements

- Refined hero section with a cleaner, proportional single-image layout
- Removed distracting visual overlays for a more premium composition
- Improved responsive behavior to prevent stretched visuals on wide screens
- Upgraded visual consistency across cards, buttons, and modal sections
- Updated dependency pinning to Streamlit 1.56.0

## License

This project is distributed for portfolio and product demonstration purposes.
