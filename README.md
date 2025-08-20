# `llmgcalparse`

Create Google Calendar event URLs interactively from a natural language description, leveraging LLMs with an OpenAI Chat Completions-compatible API and user edits.

## Features

- **Conversational Extraction:** Uses an LLM to extract structured event details from a free-form description.
- **Flexible Backends:** Works with any LLM with an OpenAI Chat Completions-compatible API.
- **User-in-the-loop Editing:** Edit each LLM-suggested field (title, times, description, location) for accuracy.
- **Automatic URL Generation:** Generates a ready-to-use Google Calendar event creation link.

## Usage

```bash
python -m llmgcalparse --api-key=YOUR_API_KEY --base-url=BASE_URL --model=MODEL_NAME
```

- `--api-key`: (Required) Your API key for the LLM service
- `--base-url`: (Required) Base URL of the LLM API endpoint
- `--model`: (Required) AI model to use (e.g., `gpt-4.1`)

Each step uses [get-unicode-multiline-input-with-editor](https://github.com/jifengwu2k/get-unicode-multiline-input-with-editor) to prompt you in your default text editor (like `git`), so you have full control over what is sent to Google Calendar.

```
$ python -m llmgcalparse --api-key=sk-xxxxx --base-url=https://my-llm-api/v1 --model=my-model-name

# Enter natural language description of event above. Lines starting with # will be ignored.
Project demo with Alice at 11am July 1st, 2024 via Zoom. Lasts one hour.

Model-generated event title: '''Project demo with Alice'''
[editor opens, you confirm or edit...]

Model-generated start datetime (YYYYMMDDTHHMMSS): '''20240701T110000'''
[editor lets you fix/confirm dates...]

...

Generated Google Calendar Event URL: 
https://calendar.google.com/calendar/render?action=TEMPLATE&text=Project%20demo%20with%20Alice&...
```

## Installation

```bash
pip install llmgcalparse
```

## Vision

**Harness the generative power of AI while respecting the proven workflows of programmers.**

Professional developers and power users rely on flexible, scriptable, and transparent toolchains—often centered around the Unix terminal and text editors. While modern large language models are powerful assistants, most AI tools are designed for web or desktop GUIs, making them isolated from the daily routines of experienced programmers.

**This project aims to bridge that gap.**

We envision a future where:

- **LLM-driven tools** are accessible directly from the command line and within editors, enhancing efficiency without disrupting established workflows.
- **AI-generated content** (code, prose, configuration, documentation) always lands in a place where it can be reviewed, edited, and curated by the human developer before use.
- **Automation and creativity** are augmented, not replaced, by AI: human judgment and oversight remain fundamental.
- **Command-line and scriptable tools** powered by LLMs are as composable, hackable, and reliable as their traditional counterparts.
- **Transparency, simplicity, and user control** are at the core—even as we extend what's possible with powerful generative models.

**By bringing generative AI into classic, trusted environments, we empower developers to move faster, automate more, and discover new ways to build—without sacrificing clarity or control.**

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).