# 📄 AI Regulatory Monitoring System

An autonomous LangGraph agent that monitors Indian financial regulators — **RBI, SEBI, and IRDAI** — for new circulars and announcements, classifies what's genuinely new versus previously seen, and generates structured reports, triggered through a Streamlit dashboard.

## Why this exists

Compliance teams at financial institutions manually track regulator websites for new circulars, notifications, and policy changes — a slow, error-prone process where a missed update carries real regulatory risk. This pipeline automates that monitoring loop: it checks a selected regulator's site, diffs new content against what's already been seen, classifies it, and produces a report — no manual page-checking required.

## Demo

![Streamlit UI](docs/screenshot.png)

*Select a regulator (RBI / SEBI / IRDAI), enter a notification email, and start monitoring.*

## How it works

```
Streamlit UI (select regulator + email)
        │
        ▼
   Scheduler (runs daily)
        │
        ▼
   run_pipeline() in app.py
        │
        ▼
┌───────────────────────────────────────┐
│           LangGraph Agent              │
│                                         │
│  1. Fetch current regulator page       │
│  2. Compare against last-seen state    │
│     (SQLite: get_old_data / update)    │
│  3. Classify: new vs. routine content  │
│  4. Generate structured report         │
└───────────────────────────────────────┘
        │
        ▼
   Updated state persisted to DB
   Report output (+ email notification)
```

The agent maintains state across runs (`document`, `classification_data`, `old_data`, `new_data`, `report`), so each run only flags content that's genuinely changed since the last check — not the entire page every time.

## Features

- **Multi-source monitoring** — covers RBI, SEBI, and IRDAI, selectable via the UI
- **Stateful change detection** — SQLite-backed persistence means the agent only reports on *new* regulatory content, not re-flagging what it already classified
- **Daily scheduled runs** — the pipeline checks each selected source once a day
- **Streamlit dashboard** — pick a regulator, enter a notification email, and trigger monitoring with one click
- **Email notifications** — configurable receiver address for alerting on new regulatory updates

## Metrics (current)

| Metric | Value |
|---|---|
| Regulatory sources monitored | 3 (RBI, SEBI, IRDAI) |
| Check frequency | Daily |
| Storage | SQLite, local |
| LLM provider | Groq — `<MODEL_NAME>` *(update this with the exact model from `src/graph/graph.py`)* |

> Latency-per-run and classification accuracy numbers are still being collected through real runs and will be added here once available.

## Tech Stack

| Layer | Technology |
|---|---|
| Agent orchestration | LangGraph |
| LLM | Groq (`<MODEL_NAME>`) |
| Scheduling | Python scheduler (daily interval) |
| UI | Streamlit |
| Storage | SQLite |
| Notifications | Email (SMTP via `.env` config) |
| Language | Python |

## Project Structure

```
.
├── app.py              # Pipeline entrypoint — builds and invokes the LangGraph agent
├── scheduler.py         # Scheduler that runs the pipeline daily
├── streamlitUi.py        # Streamlit dashboard for selecting a regulator and starting monitoring
├── src/
│   ├── graph/
│   │   └── graph.py     # LangGraph agent definition (Create_graph)
│   └── database/
│       └── database.py  # SQLite read/write helpers for tracking old vs. new state
└── requirements.txt
```

## Getting Started

### Prerequisites
- Python 3.10+
- A Groq API key

### Installation

```bash
git clone https://github.com/shubh9165/Regulatory-Monitoring-Pipeline.git
cd Regulatory-Monitoring-Pipeline
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```
website=RBI
receiver=your-email@example.com
GROQ_API_KEY=your-groq-api-key
```

### Running

**Streamlit dashboard**
```bash
streamlit run streamlitUi.py
```
Select a regulator (RBI / SEBI / IRDAI), enter an email address, and click **Start Monitoring**.

**Single pipeline run (no UI)**
```bash
python app.py
```

## Example Output

*(To be added — paste an actual `report` output from a real run here once available. This is the single most convincing addition to this README, more than any other section.)*

```
Document: ...
Classification: ...
New Data: ...
Report: ...
```

## Roadmap

- [ ] Run the scheduler as a fully independent background process, decoupled from the Streamlit UI session, so monitoring continues even if the dashboard tab is closed
- [ ] Add a "Stop Monitoring" control and live status indicator to the UI
- [ ] Collect and publish real latency and classification-accuracy metrics
- [ ] Add more regulator sources beyond RBI/SEBI/IRDAI
- [ ] Add structured report export (PDF/CSV)
- [ ] Add basic test coverage for the classification step
- [ ] Containerize with Docker for easier deployment

## License

MIT
