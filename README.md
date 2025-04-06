# Android APK Scanner with AI

A powerful static analysis tool that uses AI to scan Android APK files for security vulnerabilities and potential issues. The scanner decompiles APK files and analyzes the source code, manifest, and resource files using AI models.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Output Format](#output-format)
- [Supported AI Models](#supported-ai-models)
- [Security Analysis Coverage](#security-analysis-coverage)
- [Error Handling](#error-handling)
- [Performance](#performance)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)



## Features

- APK decompilation using JADX
- Multi-threaded file analysis
- Support for multiple AI models (currently supports GEMENAI)
- Comprehensive security vulnerability scanning
- HTML and Markdown report generation
- Cross-platform compatibility (Windows/Linux)
- Interactive report browsing through generated index.html


## Prerequisites

- Python 3.8 or higher
- JADX decompiler
- Required Python packages (see requirements.txt)
- Valid API key for supported AI models

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd android-scanner-ai
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

3. Set up JADX:
   - Windows: Ensure jadx.bat is in the jadx/bin directory
   - Linux: Ensure jadx is executable in the jadx/bin directory
   ```bash
   chmod +x jadx/bin/jadx
   ```

4. Configure API Keys in config.py:
   - Obtain your API key from [Google AI](https://aistudio.google.com/app/apikey) Studio and add it to the `config.py` file

5. Configure Models in config.py:
   - Set up your Gemini Model by referring to the [Gemini models](https://ai.google.dev/gemini-api/docs/models) and configure it in the `config.py` file.


## Usage

Run the scanner using the following command:

```bash
python run.py --apk-path <path_to_apk> \
              --out-dir <output_directory> \
              --target-package <package_name> \
              --model-name <AI_model> \
              --report <report_directory> \
              --threads <number_of_threads>
```

### Arguments

- `--apk-path`: Path to the APK file to analyze
- `--out-dir`: Directory where decompiled files will be saved
- `--target-package`: Package name to analyze (e.g., 'com.example.app')
- `--model-name`: AI model to use (e.g., 'GENEAI', 'OPENAI')
- `--report`: Directory where analysis reports will be saved
- `--threads`: Number of concurrent analysis threads (1-10, default: 1)

## Project Structure

```
android-scanner-ai/
├── run.py # Main entry point
├── config.py # Configuration and API keys
├── requirements.txt # Python dependencies
├── jadx/ # JADX decompiler
│ └── bin/
│ ├── jadx # Linux executable
│ └── jadx.bat # Windows executable
├── models/
│ └── genai_model.py # AI model integration
└── utils/
├── extract_apk_helpers.py # APK extraction utilities
└── html_helpers.py # Report generation utilities
```

## Configuration

Edit `config.py` to configure:

1. AI Model API Keys:
```python
api_keys = {
    "GENEAI": "your-api-key-here"
}
```

2. Available Models:
```python
Models = {
    "GENEAI": {
        "gemini-2.0-flash": "gemini-2.0-flash"
    }
}
```

3. Analysis Instructions and Rules

## Output Format

The scanner generates two types of reports for each analyzed file:

1. Markdown Report (.md):
```markdown
## Vulnerability: [Title]
**Severity**: [Low/Medium/High]
**CWE ID**: [ID]
**Description**: [Details]
**Code Example**: [Relevant Code]
**Recommendation**: [Fix Suggestions]
**References**: [Links]
```

2. HTML Report:
- Interactive web-based report
- Organized by package structure
- Linked through index.html

## Supported AI Models

Currently supported AI models:
- Google Gemini AI (GENEAI)
  - Model: gemini-2.0-flash

## Security Analysis Coverage

The scanner analyzes:

1. Java Source Files:
   - Security vulnerabilities
   - Code weaknesses
   - Best practice violations

2. AndroidManifest.xml:
   - Permission issues
   - Component exposure
   - Security configurations

3. strings.xml:
   - Hardcoded credentials
   - Sensitive data
   - Configuration issues

## Error Handling

The scanner includes robust error handling for:
- Invalid APK files
- Missing JADX executable
- AI model errors
- File system issues
- Threading problems

## Performance

- Multi-threaded analysis (up to 10 threads)
- Concurrent file processing
- Efficient report generation
- Optimized for large APKs


## Acknowledgments

- JADX decompiler
- Google Gemini AI
