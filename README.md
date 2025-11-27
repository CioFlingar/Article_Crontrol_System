# 📰 Article Control System

A **sleek, modern, and scalable** Article Control System built with **Django**, featuring dynamic, no-reload interactions using **HTMX** and **Alpine.js**, robust user authentication with **Django Allauth**, and a responsive, polished UI styled with **TailwindCSS**. Ideal for blogs, news platforms, or CMS projects.

----------

## 🎯 Why This Project?

This project is a production-ready solution for managing articles, prioritizing **performance**, **user experience**, and **developer productivity**. With modern tools, SEO optimization, and a clean codebase, it’s perfect for developers building content-driven platforms.

----------

## 🚀 Features

-   🔐 **Secure Authentication**: Register, login, logout, and social login with **Django Allauth**.
-   📧 **Email Confirmation**: Verify new users via email for added security.
-   📝 **Full CRUD Operations**: Create, read, update, and delete articles effortlessly.
-   🔎 **Live Search**: Instant, no-reload search powered by **HTMX**.
-   📄 **Paginated Listings**: Smooth browsing with pagination.
-   🌐 **SEO-Friendly URLs**: Slug-based URLs for better search rankings.
-   📱 **Responsive Design**: Mobile-first UI with **TailwindCSS**.
-   🛠️ **Admin Dashboard**: Intuitive backend management with **Django Admin**.
-   ⚡ **Interactive UI**: Dynamic frontend powered by **Alpine.js**.
-   ✅ **Test Suite**: Comprehensive unit tests for reliability.

----------

## ⚙️ Tech Stack

Layer

Technology

**Backend**

Django (Python)

**Frontend**

TailwindCSS, HTMX, Alpine.js

**Auth**

Django Allauth (with social login and email verification)

**Database**

PostgreSQL (via Docker)

**Dev Tools**

Django Admin, VS Code/PyCharm, Git, GitHub, Poetry, Docker

----------

## 📸 Screenshots

| 🏠 Home Page | 📖 Article Detail | 🛠️ Admin Panel |
| --- | --- | --- |
| ![Home](screenshots/home.png) | ![Detail](screenshots/detail.png) | ![Admin](screenshots/admin.png) |
----------

## 📋 Prerequisites

Before setting up the project, ensure you have the following installed:

-   Docker
-   Docker Compose
-   pipx

----------

## 📦 Installation & Setup

Follow these steps to set up the project locally using **Poetry** and **Docker**:

1.  **Create a project directory**
    
    ```bash
    mkdir article-management-system
    cd article-management-system
    
    ```
    
2.  **Open the directory in VS Code or PyCharm**
    
    -   For VS Code:
        
        ```bash
        code .
        
        ```
        
    -   For PyCharm: Open PyCharm, select `File > Open`, and choose the `article-management-system` folder.
        
3.  **Open the terminal in the IDE**
    
    -   Press `Ctrl + J` (or `Ctrl + ~` in VS Code) to open the terminal.
4.  **Install Poetry using pipx**
    
    ```bash
    pipx install poetry
    
    ```
    
5.  **Activate the Poetry virtual environment**
    
    ```bash
    poetry env activate
    
    ```
    
6.  **Set the Python interpreter in your IDE**
    
    -   Press `Ctrl + Shift + P` to open the command palette.
    -   Search for **Python: Select Interpreter** and select it.
    -   Choose the Poetry interpreter matching the activated environment (e.g., `~/.cache/pypoetry/virtualenvs/...`).
7.  **Clone the project**
    
    ```bash
    git clone https://github.com/CioFlingar/Article_Crontrol_System.git .
    
    ```
    
8.  **Create a** `.env.docker` **file**
    
    In the project root, create a file named `.env.docker` with the following content:
    
    ```env
    SECRET_KEY="any-key"
    DATABASE_URL=postgresql://postgres:postgres@db:5432/django_pj
    POSTGRES_DB=django_pj
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    RESEND_API_KEY="your-resend-api-key-from-resend"
    RESEND_EMAIL=onboarding@resend.dev
    
    ```
    
    -   Replace `your-resend-api-key-from-resend` with your actual Resend API key from Resend.
9.  **Build and run the Docker containers**
    
    ```bash
    docker compose up --build
    
    ```
    
    -   This builds and starts the Django application and PostgreSQL database containers.
    -   Once running, visit `http://127.0.0.1:8005` in your browser 🚀.
10.  **Create a superuser**
    
    ```bash
    docker compose exec web poetry run python manage.py createsuperuser
    
    ```
    
    -   Follow the prompts to set up the admin superuser.
11.  **Run tests**
    
    ```bash
    docker compose exec web poetry run python manage.py test
    
    ```
    

----------

## 📁 Project Structure

```plaintext
article-management-system/
├── articles/              # Core app: models, views, URLs, templates
├── static/                # CSS, JS, and static assets
├── templates/             # Base and shared HTML templates
├── media/                 # User-uploaded files
├── article_management/    # Django project settings and configuration
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
├── .env.docker            # Docker environment variables
├── docker-compose.yml     # Docker Compose configuration
└── README.md

```
----------

## 🧪 Running Tests

Run the test suite inside the Docker container:

```bash
docker compose exec web poetry run python manage.py test

```

----------

## 🤝 Contributing

We welcome contributions! To get started:

1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/your-feature`).
3.  Commit your changes (`git commit -m "Add your feature"`).
4.  Push to the branch (`git push origin feature/your-feature`).
5.  Open a pull request.

See our Contributing Guidelines for more details.

----------

## 📜 License

This project is licensed under Me(😉).

----------

## 👨‍💻 Author

**Walid Hasan**  
📩 Email: [eng.walidhasan@gmail.com](mailto:eng.walidhasan@gmail.com)  
🌐 GitHub: CioFlinGar  
🔗 LinkedIn: [walid-hasan-](linkedin.com/in/walid-hasan-)

----------

## 🌟 Show Your Support

If you find this project helpful, please give it a ⭐ on GitHub! Your support motivates further development and helps others discover the project.

----------

## 📢 What's Next?

-   🔔 User notifications for actions (e.g., new comments).
-   📊 Article view analytics integration.
-   🌍 Multi-language support.
-   🔗 REST API for third-party integrations.

Star the repo and stay tuned for updates! 🚀

