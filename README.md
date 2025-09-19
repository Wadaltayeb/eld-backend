# 🚚 DRIVELEDGER — Fleet Management Backend

**DRIVELEDGER** is a full-stack fleet management system built with modern technologies to streamline vehicle tracking, driver records, and operational workflows. Designed for scalability, clarity, and performance, this backend powers a seamless experience for both admins and users.

---

## 🔧 Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| Backend      | Django 5.2.6        |
| API          | Django REST Framework |
| Deployment   | Render (Free Tier) |
| Static Files | WhiteNoise         |
| CORS         | django-cors-headers |
| Server       | Gunicorn           |

---

## 🌐 Live Backend

- **Status**: ✅ Online
- **Homepage**: Custom `home.html` with animated status and branding

---

## 🔐 Admin Access (for testing only)

> ⚠️ These credentials are for demo purposes. Change them before production.
- **Admin Panel** 
- **Username**: `admin`
- **Password**: `admin12345`

---

## 📁 API Endpoints

| Method | Endpoint                     | Description               |
|--------|------------------------------|---------------------------|
| POST   | `/api/drivers/create/`       | Create a new driver       |
| GET    | `/api/drivers/list/`         | List all drivers          |
| PUT    | `/api/drivers/update/<id>/`  | Update driver info        |
| DELETE | `/api/drivers/delete/<id>/`  | Delete a driver           |

> All endpoints are secured and CORS-enabled for frontend integration.

---

## 📦 Installation (Local)

```bash
git clone https://github.com/Wadaltayeb/eld-backend.git
cd eld-backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

🚀 Deployment (Render)

- Uses render.yaml for automatic build and deploy
- Environment variables:
  - DJANGOSETTINGSMODULE=eld_project.settings
  - SECRET_KEY=your-secret-key
  - ALLOWED_HOSTS=render.com
  - RENDER=TRUE

---

🎨 Design Philosophy

Ali’s vision for DRIVELEDGER blends technical precision with visual clarity:

- Pixel-perfect layouts
- Responsive design across all devices
- Emotionally resonant documentation
- Arabic-first storytelling with English accessibility
- Neon effects and modern animations to impress evaluators

---

🧠 Author

Ali Wadaltayeb — Full-stack project lead  
Expert in modular architecture, responsive design, and deployment workflows  
Passionate about empowering users through automation and clarity

---

📜 License

This project is licensed for educational and demonstration purposes.  
Please contact the author for production use or collaboration.

---

> 💬 “DRIVELEDGER isn’t just code — it’s a story of precision, passion, and purpose.”
`

---
