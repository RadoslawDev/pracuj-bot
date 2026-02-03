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

Installation and Configuration

1. Cloning the Repository
```bash
git clone [https://github.com/RadoslawDev/pracuj-bot.git](https://github.com/RadoslawDev/pracuj-bot.git)
cd pracuj-bot
