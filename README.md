# Proxmox + Ansible + Docker Compose

Автоматизированное развёртывание инфраструктуры на Proxmox LXC с использованием Ansible и Docker Compose.

## Описание

Проект демонстрирует полный цикл настройки серверной инфраструктуры:

- Создание и базовая настройка LXC-контейнера на Proxmox VE (Debian 12)
- Автоматизация через Ansible одной командой
- Развёртывание multi-container приложения через Docker Compose
- Настройка сетевой безопасности (UFW + SSH-ключи)

## Архитектура
Proxmox VE
└── LXC (Debian 12)
├── Ansible
│   ├── обновление системы
│   ├── установка Docker
│   ├── настройка UFW
│   └── SSH-ключи
└── Docker Compose
├── web  (FastAPI)
└── db   (PostgreSQL 16)
text## Стек технологий

- **Гипервизор:** Proxmox VE
- **Контейнер:** LXC (Debian 12)
- **Автоматизация:** Ansible
- **Контейнеризация:** Docker + Docker Compose
- **Backend:** FastAPI + Uvicorn
- **База данных:** PostgreSQL 16
- **Файрвол:** UFW
- **Аутентификация:** SSH-ключи

## Структура проекта
proxmox-ansible-docker/
├── ansible/
│   ├── inventory.ini
│   ├── playbook.yml
│   └── files/
│       ├── docker-compose.yml
│       ├── init.sql
│       └── app/
│           ├── main.py
│           ├── requirements.txt
│           └── Dockerfile
├── README.md
└── .gitignore
text## Требования

- Proxmox VE с созданным LXC (Debian 12)
- Ansible на управляющей машине
- Коллекция `community.general`

```bash
sudo apt update && sudo apt install -y ansible
ansible-galaxy collection install community.general
Развёртывание

Укажите IP LXC и путь к SSH-ключу в ansible/inventory.ini
Укажите разрешённый IP в переменной allowed_ip в playbook.yml
Запустите playbook:

Bashcd ansible
ansible-playbook -i inventory.ini playbook.yml
После выполнения приложение будет доступно по адресам:

http://<IP_LXC>:8000/
http://<IP_LXC>:8000/health
http://<IP_LXC>:8000/items

Возможности развития

Создание non-root пользователя и настройка sudo
Отключение парольной аутентификации SSH
Вынос секретов в Ansible Vault / .env
Добавление Nginx в качестве reverse-proxy
Мониторинг (Zabbix / Prometheus + Grafana)
CI/CD через GitHub Actions

Автор
Студент. Проект выполнен самостоятельно в рамках изучения Ansible, Docker Compose и работы с Proxmox.