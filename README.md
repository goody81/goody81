# LuminAI - Professional Web Crawler & AI Platform

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-Commercial-red)
![Python](https://img.shields.io/badge/python-3.9%2B-brightgreen)

## 🚀 Enterprise-Grade Web Intelligence Platform

**LuminAI** is a cutting-edge, integrated platform that combines advanced web crawling with AI-powered content analysis. Designed for businesses that need to extract, analyze, and gain actionable insights from web data at scale.

### 💎 Premium Features

- **🕷️ Smart Web Crawler**
  - Intelligent breadth-first crawling algorithm
  - Automatic rate limiting and robots.txt compliance
  - Domain-focused crawling with configurable depth
  - Robust error handling and retry logic

- **🤖 AI-Powered Analysis**
  - Advanced keyword extraction and topic modeling
  - Sentiment analysis for content understanding
  - Automatic content categorization
  - Statistical insights and metrics

- **🏗️ Enterprise Architecture**
  - Modular, maintainable codebase
  - Docker-ready for cloud deployment
  - OpenShift CI/CD integration
  - Scalable and extensible design

- **⚙️ Flexible Configuration**
  - Environment-based configuration
  - CLI interface with multiple options
  - JSON output for easy integration
  - Customizable crawl parameters

## 📦 Installation

### Using Docker (Recommended)

```bash
# Build the image
docker build -t luminai:latest .

# Run with Docker
docker run luminai:latest --url https://example.com --depth 2
```

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/goody81/goody81.git
cd goody81

# Install dependencies
pip install -r requirements.txt

# Run the application
export PYTHONPATH=$PWD/src
python src/main.py --url https://example.com --depth 2
```

## 🎯 Quick Start

### Basic Web Crawling

```bash
python src/main.py --url https://example.com --depth 3
```

### With AI Analysis

```bash
python src/main.py --url https://example.com --depth 3 --ai-analyze
```

### Custom Output File

```bash
python src/main.py --url https://example.com --depth 2 --output results.json
```

## 🔧 Configuration

Configure the platform using environment variables:

```bash
export CRAWL_DELAY=1.5        # Delay between requests (seconds)
export MAX_PAGES=200          # Maximum pages to crawl
export AI_ENABLED=true        # Enable AI analysis by default
export OUTPUT_FORMAT=json     # Output format
```

## 📊 Output Format

The platform generates structured JSON output with rich metadata:

```json
{
  "url": "https://example.com/page",
  "title": "Page Title",
  "text": "Extracted content...",
  "links_count": 42,
  "depth": 1,
  "ai_analysis": {
    "keywords": [["keyword1", 15], ["keyword2", 10]],
    "sentiment": "positive",
    "category": "technology",
    "word_count": 1250,
    "char_count": 7500
  }
}
```

## 🏢 Business Value

### Market Applications

- **📈 Competitive Intelligence**: Monitor competitor websites and track changes
- **🎯 Market Research**: Gather insights from industry websites and news sources
- **📰 Content Aggregation**: Build comprehensive databases of web content
- **🔍 SEO Analysis**: Analyze website structures and content strategies
- **📊 Trend Analysis**: Track emerging topics and sentiment across domains
- **🤝 Lead Generation**: Discover and analyze potential business partners

### ROI Features

- **Time Savings**: Automate manual research tasks
- **Data Quality**: Clean, structured output ready for analysis
- **Scalability**: Handle multiple domains and thousands of pages
- **Insights**: AI-driven analysis provides actionable intelligence
- **Integration**: JSON output integrates with any data pipeline

## 🛠️ Technical Specifications

### System Requirements

- Python 3.9 or higher
- 2GB RAM minimum
- Network connectivity
- Docker (optional, for containerized deployment)

### Dependencies

- `requests` - HTTP library for web requests
- `beautifulsoup4` - HTML parsing and extraction
- `lxml` - Fast XML/HTML processing

### Performance

- Handles 100+ pages per minute with default settings
- Configurable rate limiting to respect server resources
- Memory-efficient streaming architecture
- Optimized for both small and large-scale crawls

## 🎓 Use Cases

1. **Content Intelligence**: Extract and analyze content from competitor websites
2. **Market Monitoring**: Track industry news and emerging trends
3. **Data Collection**: Build datasets for machine learning and analytics
4. **Research Automation**: Gather information from multiple sources automatically
5. **SEO Auditing**: Analyze website structures and content optimization

## 🔐 Enterprise Features

- Configurable user agents for ethical crawling
- Respect for robots.txt and crawl delays
- Error handling and recovery
- Comprehensive logging
- Containerization support
- CI/CD integration

## 📈 Scaling & Deployment

### Cloud Deployment

The platform includes an OpenShift CI/CD workflow for seamless deployment:

- Automatic containerization
- Registry integration (GHCR, Quay.io, Docker Hub)
- OpenShift deployment automation
- Production-ready infrastructure

### Horizontal Scaling

- Deploy multiple instances for different domains
- Process queue integration ready
- Microservices architecture compatible

## 💰 Pricing & Licensing

**Enterprise License Available**

This is a commercial-grade platform designed for business use. Contact for licensing:

- **Standard License**: Perfect for small to medium businesses
- **Enterprise License**: Includes support, customization, and updates
- **Custom Development**: Tailored solutions for specific needs

**Estimated Value**: $20,000+ based on development time, features, and market positioning

## 🤝 Support & Contact

For licensing, custom development, or support inquiries:

- GitHub: [@goody81](https://github.com/goody81)
- Create an issue for technical questions
- Enterprise customers: Contact via GitHub profile

## 📝 License

Copyright © 2025. All rights reserved.

This software is provided for evaluation purposes. Commercial use requires a valid license.

---

**Built with ❤️ for businesses that value data intelligence**
