Pracuj.pl Job Bot (Discord Notifier)

An automated bot written in Python that monitors new job postings on the pracuj.pl portal and sends notifications to the Discord channel. The project has been optimized for running on Raspberry Pi 4.

Features
Real-time monitoring: The bot searches defined lists of results (e.g., DevOps, IT Admin in a selected location).
Discord webhook: Instant notifications with the job title, company name, and direct link.
Database (JSON): Local system for saving posted job postings to avoid duplicate notifications.
Security: Use of `.env` files to hide sensitive data (tokens).
Automation: Configured for a `cron` schedule (e.g., checking every 12 hours).

Project structure
`praca_bot.py` – the main bot script.
`.env` – configuration file with the webhook (ignored by Git).
`requirements.txt` – a list of required Python libraries.
`wyslane_ogloszenia.json` – a local database of posted offers.

<img width="673" height="506" alt="image" src="https://github.com/user-attachments/assets/ca4e89f3-057a-4cd4-ae97-0b1b7d9493f6" />
<img width="975" height="569" alt="image" src="https://github.com/user-attachments/assets/3e855bce-5e95-4980-a621-5b1803f8e044" />


Installation and Configuration

1. Cloning the Repository
```bash
git clone [https://github.com/RadoslawDev/pracuj-bot.git](https://github.com/RadoslawDev/pracuj-bot.git)
cd pracuj-bot
