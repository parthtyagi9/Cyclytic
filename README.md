# Cyclytic – AI-Powered Period and Wellness Tracker

Cyclytic is an iOS-native application that helps users understand and manage menstrual health through intelligent analytics, personalized recommendations, and privacy-first design. It combines modern iOS development with AI-driven insights to provide accurate tracking, adaptive predictions, and holistic wellness features.

---

## Overview

Cyclytic integrates predictive machine learning models and Gemini AI to deliver personalized cycle forecasts, contextual explanations for symptoms, and wellness guidance based on user behavior. The app focuses on secure health tracking, combining simplicity with powerful backend intelligence.

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-------------|----------|
| Frontend | Swift + SwiftUI | Native iOS interface with declarative UI and smooth animations |
| Backend | FastAPI (Python) | REST API handling data, AI logic, and ML integration |
| Database | Firebase Firestore | Real-time data storage for cycle logs, moods, and preferences |
| Authentication | Firebase Auth | Secure sign-in using Apple and Google |
| AI & ML | Gemini API + TensorFlow | AI-generated insights and predictive cycle analytics |
| Notifications | APNs + Firebase Cloud Messaging | Smart reminders for period, ovulation, and wellness events |
| Hosting | Render | FastAPI deployment with continuous integration |
| Analytics | Firebase Analytics | User engagement, behavior, and retention tracking |
| Version Control | GitHub | Source control, collaboration, and CI/CD setup |

---

## Core Features

### Cycle Tracking
- Log period start/end, symptoms, and moods
- Predict next period, ovulation, and fertile window
- Display visual analytics with interactive SwiftUI charts

### AI-Powered Insights
- Personalized health insights using Gemini API
- Predictive analytics powered by TensorFlow models
- Adaptive learning from user data to refine predictions

### Holistic Wellness
- AI-generated daily self-care routines and mindfulness recommendations
- Ayurvedic-based cycle phase advice
- Built-in journaling and reflections section

### Privacy & Security
- End-to-end encryption for sensitive health data
- Optional local-only data mode (Private Mode)
- Compliance with Apple HealthKit standards

### Smart Notifications
- Personalized notifications for cycle events and wellness prompts
- Timing adapts dynamically to user behavior patterns

---

## Architecture Overview

[ SwiftUI Frontend ]
↓ (HTTPS)
[ FastAPI Backend ]
↓
[ Firebase Firestore + Auth ]
↓
[ Gemini API + TensorFlow Engine ]
↑
[ APNs + Firebase Cloud Messaging ]


---

Author

Parth Tyagi
Full-Stack SWE | iOS & AI Engineer
Toronto, Canada
GitHub: https://github.com/parthtyagi9
LinkedIn: https://www.linkedin.com/in/parth-tyagi45/
Portfolio: https://www.parthtyagi.com

MIT License
Free to use, modify, and distribute with attribution.
