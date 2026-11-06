# ARIA - Automated Research Intelligence Assistant

**🚀 Transform months of research into minutes of insight**

English | [中文](./README_zh.md)

ARIA is an automated research assistant framework for scientific data analysis, visualization, and report generation.

## Project Structure

```
aria/
├── .claude/commands/           # Claude AI command files
│   ├── academic/               # Academic workflow commands
│   ├── git/                    # Git operation commands
│   └── python/                 # Python environment commands
├── data/
│   ├── raw/                   # Original data
│   ├── processed/              # Preprocessed data
│   └── output/                 # Experiment outputs
│       ├── models/             # Trained models
│       ├── results/            # Experimental results
│       ├── figures/            # Visualization charts
│       └── logs/               # Execution logs
├── docs/                       # Project documentation
├── src/                        # Source code
├── scripts/                    # Execution scripts
├── GETTING_STARTED.md          # Quick start guide
├── INSTALL.md                  # Installation guide
└── README.md                   # This file
```

## Workflow

### 1. Data Preparation

For an approved SQLite source, start with metadata inspection:

```sh
python scripts/onboard_sqlite.py path/to/subscriptions.sqlite subscriptions workspace.json
```

The command creates a new portable workspace JSON with a logical source ID,
connection guidance, and a dated inventory of declared tables, columns and keys.
It lists views and virtual/shadow tables by name and type. Application rows and
the local database path stay out of the record. Review join cardinality, business
definitions, and permitted uses with the source owner before planning a study.
For a refresh, write a new file, review the difference and increment the source
record version when adopting a change. Protect the file using OS permissions
for every account or tool that can open it. Read-only mode applies to this inspector.

- Place raw data in the `data/raw/` folder
- Manually create `docs/01-basic-information.md` to describe project background, objectives, and data overview

### 2. Data Analysis

- **Raw Data Analysis**: Use `@raw-data-analysis.md` command to analyze raw data, generating `docs/02-raw-data-analysis.md`
- **Data Preprocessing**: Use `@preprocess.md` command to design preprocessing plan (`docs/03-preprocess-plan.md`), execute preprocessing, analyze processed data (`docs/04-processed-data-analysis.md`)

### 3. Research Design

- **Research Plan**: Use `@research-plan.md` command to develop research plan including feature engineering, model selection, evaluation metrics, generating `docs/05-research-plan.md`

### 4. Code Implementation

- **Code Development**: Use `@code-implementation.md` command to implement research plan, creating necessary Python modules
- Generate `docs/06-implementation-docs.md` (implementation documentation) and `docs/07-execution-instructions.md` (execution guide)
- Code quality check: Use mypy and ruff to ensure code quality

### 5. Experiment Execution

- **Run Experiments**: Use `@run-experiments.md` command to execute experiment scripts
- Outputs saved to corresponding subfolders in `output/` directory

### 6. Results Analysis

- **Results Analysis**: Use `@experiment-analysis.md` command to analyze experiment outputs
- Generate individual analyses in `docs/08-experiment-results/` directory
- Generate `docs/09-experiment-report.md` comprehensive experiment report

### 7. Paper Writing

- **Academic Paper**: Use `@research-report.md` command to generate high-impact journal format paper
- Generate `docs/10-manuscript.md` (main text), `docs/10-manuscript-supplement.md` (supplementary materials), `docs/10-cover-letter.md` (cover letter)

### 8. Model Deployment (Optional)

- **Gradio Interface**: If models are trained, use `@gradio-app.md` command to create model inference interface
- Generate `docs/11-model-deployment-guide.md` deployment guide

## Claude AI Commands

### Academic Commands

All academic command files are located in `.claude/commands/academic/` directory:

- `@raw-data-analysis.md` - Analyze raw data
- `@preprocess.md` - Data preprocessing
- `@research-plan.md` - Research plan design
- `@code-implementation.md` - Code implementation
- `@run-experiments.md` - Experiment execution
- `@experiment-analysis.md` - Results analysis
- `@research-report.md` - Academic paper generation
- `@gradio-app.md` - Model deployment interface
- `@convert2docs.md` - Convert markdown to DOCX (optional)

### Python Environment Commands

Python command files are located in `.claude/commands/python/` directory:

- `@setup-environment.md` - Automated environment setup
  - Checks and installs Git, Python 3.12+, and UV package manager
  - Sets up project dependencies with `uv sync`
  - Includes Tsinghua mirror fallback for network issues
  - Provides complete environment verification

### Git Commands

Git command files are located in `.claude/commands/git/` directory:

- `@git-commit.md` - Intelligent Git commits
  - Automatically creates structured commit messages
  - When there are many modified files, automatically commits in batches (max 10 files per commit)
  - Generates meaningful commit descriptions based on code changes

## Example Projects

Complete example projects demonstrating ARIA workflow across different research tasks:

- 🏠 [**aria-example-buston**](https://github.com/Biaoo/aria-example-buston) - Boston housing price prediction (regression) | [OpenML Dataset](https://www.openml.org/d/531)
- 💎 [**aria-example-diamonds**](https://github.com/Biaoo/aria-example-diamonds) - Diamond price prediction (regression) | [OpenML Dataset](https://www.openml.org/d/42225)
- 🐛 [**aria-example-kc1**](https://github.com/Biaoo/aria-example-kc1) - Software defect prediction (classification) | [OpenML Dataset](https://www.openml.org/d/1067)
- 🧩 [**aria-example-sat11**](https://github.com/Biaoo/aria-example-sat11) - SAT solver performance prediction (regression) | [OpenML Dataset](https://www.openml.org/d/41980)

All datasets are from [OpenML](https://www.openml.org/), an open machine learning platform. Each project includes complete documentation, production-ready code, trained models, and academic manuscripts.

## Quick Start

**New to ARIA? Start here: [Getting Started Guide](./GETTING_STARTED.md)** 📖

The complete guide covers:

- Installing Git and AI code editor (Cursor/VSCode/Lingma IDE)
- Automated environment setup with `@setup-environment.md`
- Step-by-step workflow from data to paper
- Troubleshooting and best practices

### For Experienced Users

1. **Setup Environment**: Use `@setup-environment.md` to configure Python and dependencies
2. **Prepare Data**: Place raw data in `data/raw/`
3. **Create Project Description**: Write `docs/01-basic-information.md`
4. **Execute Workflow**: Use Claude AI to execute academic commands in sequence
5. **Version Control**: Use `@git-commit.md` for intelligent commits

📚 **Full Documentation**: See [GETTING_STARTED.md](./GETTING_STARTED.md) and [INSTALL.md](./INSTALL.md)

## Dependency Management

Using UV for Python dependency management:

```bash
uv add <package-name>  # Add new dependency
uv sync                # Synchronize dependencies
```

## Code Quality

- Type checking: `mypy src/`
- Code style: `ruff check src/`
- Code formatting: `ruff format src/`

## Features

- 📊 **Data-Driven**: Complete workflow from raw data to academic paper
- 🤖 **AI-Assisted**: Claude AI commands automate each research phase
- 📝 **Academic Standards**: Generate Nature/Science standard papers
- 🎯 **Quality Assurance**: Integrated code quality checking tools
- 🚀 **Model Deployment**: Support for Gradio interface rapid deployment
- 📦 **Version Control**: Intelligent Git commit management

## License

This project is dual-licensed:

- **GNU AGPL-3.0** - for open source use (personal, research, education, open source projects)
- **Commercial License** - for proprietary/commercial use (contact for licensing)

See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit Issues and Pull Requests.

## Contact

For questions, suggestions, or collaboration opportunities:

- **GitHub Issues**: [Create an issue](https://github.com/Biaoo/aria/issues)
- **Email**: [biao00luo@gmail.com](mailto:biao00luo@gmail.com)
- **Project**: [ARIA on GitHub](https://github.com/Biaoo/aria)

### Join Our Community

<div align="center">
  <img src="assets/wechat-qr-20251021.png" alt="WeChat Group QR Code" width="200"/>
  <p>Scan to join WeChat discussion group</p>
</div>
