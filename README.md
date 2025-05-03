# 🌍 Tri-Aid+  
**Rapid Disaster Mapping & AI-Powered Assessment Platform**  
*Accelerating crisis response with crowdsourced data and AI insights within 48 hours.*  

---

## 📌 Table of Contents  
- [Problem Statement](#-problem)  
- [Solution](#-solution)  
- [Features](#-features)  
- [Tech Stack](#-tech-stack)  
- [Demo](#-demo)  
- [Installation](#-installation)  
- [Repo Structure](#-repo-structure)  
- [AI Pipeline](#-ai-pipeline)  
- [Contributors](#-contributors)  
- [License](#-license)  

---

## 🚨 Problem  
Disaster response is often slowed by:  
- Fragmented data from multiple sources  
- Manual verification bottlenecks  
- Delayed situational awareness (reports take weeks)  

---

## 🎯 Solution  
Tri-Aid+ combines **crowdsourcing + AI** to:  
1. **Pre-map** critical infrastructure (schools, hospitals)  
2. **Collect real-time data** via SMS, photos, voice, and social media  
3. **Generate AI-summarized reports** within 48 hours  

---

## ✨ Features  
### Pre-Disaster (Alpha Team)  
- 🗺️ Baseline mapping of vulnerable locations  
- 🔍 Open-data integration (government/NGO datasets)  

### Post-Disaster (Bravo Team)  
- 📱 Multi-input data collection (SMS/voice/image)  
- ✅ Crowd-verified damage tagging  
- 🤖 AI-generated situation reports  

### Shared Tools  
- 📊 Dynamic Map Dashboard (Mapbox)  
- 📜 PDF/Markdown report exporter  

---

## 🛠️ Tech Stack  
| Layer        | Technologies Used                  |
|--------------|------------------------------------|
| **Frontend** | React, TailwindCSS, Mapbox GL JS   |
| **Backend**  | FastAPI, PostgreSQL, Redis         |
| **AI**       | LangChain, OpenAI GPT, FAISS (RAG) |
| **Ops**      | Docker, GitHub Actions             |

---

## 🎥 Demo  
**Live Demo:** [demo.tri-aid.tech](https://demo.tri-aid.tech)  
**Test Credentials:**  

Email: volunteer@demo.tri-aid.tech
Password: Demo123!


---


---

## ⚙️ Installation  
### Local Development  
```bash
# Clone repo
git clone https://github.com/your-org/tri-aid-plus.git
cd tri-aid-plus

# Set up environment
cp .env.example .env
docker-compose up --build
```

Access:

    Frontend: http://localhost:5173

    Backend API: http://localhost:8000/docs

📂 Repo Structure

tri-aid-plus/
├── frontend/          # React app (Map UI, forms)
├── backend/           # FastAPI (REST endpoints)
├── ai-engine/         # RAG pipeline & report generation
├── docker/            # Container configs
└── docs/              # Architecture diagrams

🤖 AI Pipeline

    Data Ingestion

        SMS/Twilio → Whisper (voice-to-text)

        Social media → snscrape

    Processing

        LangChain for document chunking

        FAISS vector store for similarity search

    Output

        GPT-4-turbo generates summaries

        PDF export via LaTeX templates

👥 Contributors
Role	Team Member
AI/Backend Lead	@yourusername
Frontend Developer	@teammate1
Data Engineer	@teammate2
📜 License

MIT License - See LICENSE
🌟 Why It Matters

    "Tri-Aid+ turns chaos into actionable intelligence—because every hour counts when lives are at stake."


### Key Improvements:  
1. **Scannable** - Emoji headers and tables help judges quickly find key info.  
2. **Actionable** - Clear installation steps and demo credentials.  
3. **Technical Depth** - Explicitly calls out RAG/FAISS for AI judges.  
4. **Human Touch** - Ends with a mission-driven quote for emotional impact.
