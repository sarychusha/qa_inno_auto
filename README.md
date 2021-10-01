# qa_inno_auto
Итоговая аттестация по теме: Автоматизированное тестирование UI

CI:

[![Build Status](https://app.travis-ci.com/sarychusha/qa_inno_auto.svg?branch=main)](https://app.travis-ci.com/sarychusha/qa_inno_auto)

Цель: Автоматизация тестирования UI
Задачи:
 • Написание автотестов

 • Настройка и запуск тестов в CI

 • Написание тест кейсов

 • Получение отчетов по результатам тестирования

Форма работы: индивидуальная
Набор технологий:
 • Python

 • Pytest

 • Selenium

План работы:
 • Необходимо написать ui тесты на https://qacoursemoodle.innopolis.university.

 • Необходимо написать тесты на  3 раздела (авторизация, обновление личной информации и добавление нового курса). Для каждого раздела необходимо добавить позитивные и негативные тесты (количество на выбор студента)

 • Необходимо составить к тестам тестовую документацию. В тест кейсах должны быть предварительные шаги (если это необходимо), шаги, ожидаемый результат. Как и где ее хранить остается на выбор студента.

Критерии проекта:
Проект должен быть выложен на github и удовлетворять следующим критериям:
 • Необходимо настроить CI (https://travis-ci.org/). В проекте должен присутствовать файл настроек, который описывают логику взаимодействия с travis-ci.

 • Необходимо настроить линтер (программа, которая проверяет код на соответствие стандартам в соответствии с определенным набором правил), который должен запускаться локально/на стороне travis-ci.

 • К каждому тесту должны присутствовать тест кейсы

 • README.md заполнен и содержит актуальную информацию:

 • В файле README.md стоят бейджики travis (https://travis-ci.org/).

 • Доступна инструкция по установке зависимостей

 • Описано как запустить тесты

 • Есть информация о цели тестирования и краткое описание проекта

 • Для тестирования используется фреймворк pytest

 • Результатом тестирования является сгенерированный отчет. Он может быть доступен в travis-ci (https://travis-ci.org/) как артефакт, так и на локальной машине.

Установка:

- Создайте отдельную директорию на локальном компьютере
- Склонируйте этот репозиторий
- Откройте проект
- Установите все пакеты, которые указаны в файле requirements.txt
pip install -r /path/to/requirements.txt

Тестовая документация:
1. Тест-кейсы на авторизацию
Запуск в файле: tests/auth/test_auth.py
2. Тест-кейсы на регистрацию
Запуск в файле: tests/sign_up/test_sign_up.py
3. Тест-кейсы на добавление и удаление курса
Запуск в файле: tests/create_course/test_course_creation.py
4. Тест-кейсы на редактирование информации пользователя
Запуск в файле: \tests\personal_data\test_personal_data.py

Тест-кейсы лежат здесь: https://chlist.sitechco.ru/project/25806/checklist

Отчет Allure:
http://26.58.156.206:65531/index.html
