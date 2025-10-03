import random
import pdfplumber
from docx import Document
import re

# 1. Должности IT
positions = [
    "Data Engineer",
    "Python-разработчик",
    "Java-разработчик",
    "Frontend-разработчик",
    "Backend-разработчик",
    "Fullstack-разработчик",
    "DevOps-инженер",
    "QA-инженер",
    "SDET",
    "Android-разработчик",
    "iOS-разработчик",
    "Mobile-разработчик",
    "BI-аналитик",
    "Data Scientist",
    "ML-инженер",
    "Cloud Engineer",
    "Security Engineer",
    "System Administrator",
    "Database Administrator",
    "Software Architect",
    "Game Developer",
    "UI/UX Designer",
    "Web Designer",
    "Product Owner",
    "Scrum Master",
    "Technical Support Engineer",
    "Network Engineer",
    "Embedded Developer",
    "IT Project Manager",
    "Site Reliability Engineer (SRE)"
]

# 2. Форматы работы
work_formats = [
    "Полная занятость (Full-time)",
    "Частичная занятость (Part-time)",
    "Удалённая работа (Remote)",
    "Гибрид (Hybrid)",
    "Стажировка (Internship)",
    "Контракт (Contract)",
    "Проектная работа (Project-based)",
    "Фриланс (Freelance)",
    "Временная работа (Temporary)",
    "Обучение + работа (Trainee/Apprentice)"
]

# 3. Компании
companies = [
    "TechCorp",
    "DataInc",
    "CloudSolutions",
    "AI Labs",
    "DevStudio",
    "WebFactory",
    "CyberSystems",
    "FutureTech",
    "SoftWareHouse",
    "NextGen IT"
]

# 4. Навыки и технологии
skills = [
    "Python",
    "Java",
    "SQL",
    "Docker",
    "Kubernetes",
    "AWS",
    "Linux",
    "Git",
    "REST API",
    "Spark"
]

# 5. Примеры задач
tasks = [
    "Разработка и поддержка внутреннего ПО",
    "Создание ETL-процессов и работа с данными",
    "Поддержка CI/CD и инфраструктуры",
    "Тестирование и автоматизация процессов",
    "Разработка веб-приложений",
    "Анализ и визуализация данных",
    "Моделирование и оптимизация баз данных",
    "Настройка и поддержка облачных сервисов",
    "Разработка мобильных приложений",
    "Обеспечение безопасности и мониторинга"
]

# 6. Шуточные бонусы
fun_bonuses = [
    "Бесплатно 2 пачки риса в месяц 🍚",
    "Подписка на Pornhub на год при трудоустройстве 🍿",
    "Неограниченный кофе на рабочем месте ☕",
    "Каждый день пицца на обед 🍕",
    "Ежемесячный бонус в виде носков с мемами 🧦",
    "Личный кактус на рабочем столе 🌵",
    "Кружка с вашим именем и смешной надписью 🏆",
    "Случайный день отпуска каждый месяц 🏖️",
    "VIP-доступ к офисному столу с массажем 💺",
    "Каждое утро кошка приходит на совещание 🐱"
]

# 7. Шуточное описание зарплаты
salary_descriptions = [
    "Достойная 💰",
    "Присутствует 🤑",
    "Возможно будет 🤷‍♂️",
    "Миска риса в месяц 🍚",
    "По настроению начальника 😎",
    "Оплата в монетках из шоколада 🍫",
    "За старания — пятёрка из начальника ⭐",
    "В виде бонусов — носки с мемами 🧦",
    "Зависит от количества кофе ☕"
]

def return_vacancies() -> list:
    """
    Возвращает list с тремя сгенерированными вакансиями.

    :return: список вакансий
    """

    vacancies = []

    for _ in range(3):
        skills_text = ", ".join(random.sample(skills, 3))
        tasks_text = "\n".join(f"- {t}" for t in random.sample(tasks, 4))
        text = f"""
🏢 Компания: <b>{random.choice(companies)}</b>
💼 Должность: {random.choice(positions)}
🕒 Формат работы: {random.choice(work_formats)}
🛠 Навыки: <i>{skills_text}</i>
📌 Будущие задачи:
{tasks_text}
💰 Зарплата: {random.choice(salary_descriptions)}
🎁 Бонус: {random.choice(fun_bonuses)}

Откликнуться: <a href="https://t.me/ZlayaMarmeladka">связаться в telegram</a>
"""
        vacancies.append(text)

    return vacancies

def extract_text_from_pdf(file_path: str) -> str:
    """
    Парсит PDF файл и возвращает его содержимое.

    :param file_path: путь до файла
    :return: str текст файла
    """

    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_text_from_docx(file_path: str) -> str:
    """
    Парсит DOCX файл и возвращает его содержимое.

    :param file_path: путь до файла
    :return: str текст файла
    """

    doc = Document(file_path)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip()])
    return text.strip()

programming_languages = [
    "Python", "Java", "C++", "C#", "Go", "JavaScript", "TypeScript", "Ruby",
    "PHP", "Swift", "Kotlin", "Rust", "Scala", "Perl", "R", "MATLAB",
    "SQL", "PL/SQL", "Bash", "Shell", "Dart", "Objective-C", "Groovy"
]

web_technologies = [
    "HTML", "CSS", "Sass", "Less", "React", "Vue.js", "Angular", "Django",
    "Flask", "FastAPI", "Spring", "Node.js", "Express", "Next.js",
    "Nuxt.js", "GraphQL", "REST API", "SOAP", "Bootstrap", "jQuery"
]

databases = [
    "PostgreSQL", "MySQL", "MongoDB", "Redis", "SQLite", "Oracle", "MS SQL Server",
    "Cassandra", "Elasticsearch", "MariaDB", "Firebase", "DynamoDB", "Neo4j"
]

devops_skills = [
    "Docker", "Kubernetes", "Terraform", "Ansible", "Jenkins", "GitLab CI",
    "CircleCI", "Travis CI", "AWS", "Azure", "GCP", "Helm", "Prometheus",
    "Grafana", "Linux", "Ubuntu", "Debian", "CentOS", "CI/CD", "Git", "SVN"
]

data_skills = [
    "Pandas", "NumPy", "SciPy", "Scikit-learn", "TensorFlow", "Keras",
    "PyTorch", "LightGBM", "XGBoost", "OpenCV", "Matplotlib", "Seaborn",
    "Plotly", "Power BI", "Tableau", "ETL", "Airflow", "Kafka", "Spark",
    "Hadoop", "BigQuery", "Data Engineering", "Data Analysis", "Machine Learning",
    "Deep Learning", "NLP", "Computer Vision", "SQL", "NoSQL"
]

soft_skills = [
    "Agile", "Scrum", "Kanban", "TDD", "BDD", "Problem Solving", "Teamwork",
    "Communication", "Time Management", "Leadership", "Critical Thinking",
    "Mentoring", "Planning", "Project Management", "Adaptability"
]

mobile_ui_skills = [
    "Android", "iOS", "React Native", "Flutter", "Unity", "Unreal Engine",
    "Figma", "Sketch", "Adobe XD", "UI/UX Design", "Responsive Design"
]

security_skills = [
    "Cybersecurity", "Penetration Testing", "OWASP", "Network Security",
    "Firewalls", "VPN", "TLS/SSL", "Cryptography", "Linux Security"
]

all_skills = (
    programming_languages +
    web_technologies +
    databases +
    devops_skills +
    data_skills +
    soft_skills +
    mobile_ui_skills +
    security_skills
)

def extract_skills(text: str) -> list[str]:
    """
    Возвращает список ключевых навыков, найденных в тексте.

    :param text: текст, в котором нужно найти ключевые навыки
    :return: список строк (ключевых навыков)
    """

    key_skills = []

    for skill in all_skills:
        if re.search(rf"\b{re.escape(skill)}\b", text, re.IGNORECASE):
            key_skills.append(skill)
    return key_skills