# BrainLift CLI

[![PyPI version](https://badge.fury.io/py/brainlift.svg)](https://badge.fury.io/py/brainlift)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful command-line interface for the BrainLift knowledge management system. This CLI tool allows you to interact with the BrainLift serverless backend to manage, search, and generate structured knowledge content.

## 🚀 Installation

### Install from PyPI

```bash
pip install brainlift
```

### Install from Source

```bash
git clone https://github.com/trilogy-group/-brainlift-cli.git
cd -brainlift-cli
pip install -e .
```

## ⚙️ Configuration

After installation, configure the CLI with your API key:

```bash
blm configure
```

This interactive command will prompt you for your API key. The BrainLift function URL is pre-configured to the production endpoint by default.

Alternatively, you can provide the API key directly:

```bash
blm configure --api-key your-api-key
```

If you need to use a different function URL (for development or testing), you can specify it:

```bash
blm configure --api-key your-api-key --function-url https://your-custom-function-url.lambda-url.region.on.aws/
```

Configuration is stored in `~/.brain-lift/config` and can be updated at any time by running the configure command again.

## 🛠️ Commands

### Configure

```bash
# Interactive configuration (prompts for API key)
blm configure

# Direct configuration with API key
blm configure --api-key <key>

# Optional: Specify custom function URL (for development/testing)
blm configure --api-key <key> --function-url <custom-url>
```

### List Content

```bash
# List all products
blm list

# List topics in a product
blm list --product <product>

# List sections in a topic
blm list --product <product> --topic <topic>
```

### Search Content

```bash
# Search for content
blm search "your search query"

# Search within a specific product
blm search "your search query" --product <product>

# Limit search results
blm search "your search query" --limit 5
```

### Get Content

```bash
# Get content by path
blm get --product <product> --topic <topic>

# Get specific section
blm get --product <product> --topic <topic> --section <section>

# Get content in JSON format
blm get --product <product> --topic <topic> --format json
```

### Import Content

```bash
# Import content from a markdown file
blm import <file.md> --product <product> --topic <topic>
```

### Update Content

```bash
# Update content from a file
blm update --product <product> --topic <topic> --file <file.md>

# Update with direct content input
blm update --product <product> --topic <topic> --content "Your content here"
```

### Delete Content

```bash
# Delete a topic
blm delete --product <product> --topic <topic>

# Delete a specific section
blm delete --product <product> --topic <topic> --section <section>
```

### Generate Content

```bash
# Generate structured content from a file and save it to the system
blm generate --product <product> --topic <topic> --file <file.md>

# Generate from direct content input
blm generate --product <product> --topic <topic> --content "Your content here"

# Specify template version
blm generate --product <product> --topic <topic> --file <file.md> -v v3
```

## 📖 Content Generation Guidelines

When using the `generate` command, the system follows these principles:

1. **Factual Accuracy** ✨
   - Prioritizes factual accuracy over filling every template section
   - All content must be derived from the source material
   - Empty sections are preferred over fabricated information

2. **DOK Structure** 📊
   - **DOK1**: Raw facts directly from the source material
   - **DOK2**: Foundational knowledge and summaries based on facts
   - **DOK3**: Insights and patterns derived from the content (only when genuinely present)
   - **DOK4**: High-level perspectives and strategic viewpoints (only when supported by content)

3. **Experts Section** 👨‍🏫
   - Only includes people or sources explicitly mentioned in the original content
   - If no experts are mentioned, this section remains empty or is omitted
   - Never invents expert names or credentials

4. **Purpose Section** 🎨
   - Clearly defines the core objective or focus of the material
   - Captures the essence of what the content is about
   - Based on explicit statements in the content

5. **Template Flexibility** 🔍
   - Respects what's actually in the content rather than forcing information into categories
   - Adapts to the natural structure of the source material
   - Maintains integrity of the original information

## 🔎 Verbose Mode

Add the `--verbose` flag to get more detailed output:

```bash
# Informational logging
blm --verbose INFO list

# Debug-level logging with detailed API interactions
blm --verbose DEBUG generate --product <product> --topic <topic> --file <file.md>
```

## 👷 Development

This CLI is designed as a thin wrapper around the BrainLift serverless backend, following a clean separation of concerns:

### Client-Side Responsibilities

1. **Command-line Interface**: Parsing arguments and providing a user-friendly experience
2. **File I/O**: Reading from and writing to local files
3. **API Communication**: Making HTTP requests to the serverless backend
4. **Output Formatting**: Presenting results in a readable format

### Server-Side Responsibilities

1. **Business Logic**: All algorithmic processing of content
2. **Storage Operations**: Saving and retrieving content from S3
3. **Vector Indexing**: Managing the vector database for semantic search
4. **Content Generation**: Using AI to transform raw content into structured knowledge

### Architecture

The CLI follows a modular design with these key components:

- **CLI Module**: Command parsing and execution logic
- **Client Module**: API communication and authentication
- **Configuration**: Managing API endpoints and credentials

## 👏 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
