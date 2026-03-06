# Books API (Initial Setup) 🚀

This project marks the beginning of my journey into Backend Development. Currently, I have focused on building a solid foundation: establishing the project structure, containerization, and a fully automated CI/CD pipeline.

### ✅ What is implemented:
* **Asynchronous API Framework:** Built with **FastAPI** to ensure high performance.
* **Cloud-Ready Configuration:** Implemented dynamic port handling using Python's `os` module, allowing seamless deployment to platforms like Render.
* **Deployment Workflow:** Successfully integrated with GitHub for automated deployment.
* **Docker Support:** The project includes a `Dockerfile` for environment consistency.

### 🛠 Tech Stack:
* **Language:** Python 3.x
* **Framework:** FastAPI
* **Server:** Uvicorn
* **Infrastructure:** Docker & Render

### 📈 Current Status & Next Steps:
The infrastructure is ready. My next milestone is to replace the static responses with a real database.
1. Integrate **SQLAlchemy** for ORM.
2. Connect a **PostgreSQL** database.
3. Implement full **CRUD** logic for book management.

### ⚙️ How to run locally:
```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
