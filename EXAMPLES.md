# LuminAI Usage Examples

## Quick Examples

### Example 1: Basic Web Crawl

```bash
export PYTHONPATH=$PWD/src
python src/main.py --url https://example.com --depth 2
```

This will crawl `example.com` and all pages 2 levels deep, saving results to `output.json`.

### Example 2: Deep Crawl with AI Analysis

```bash
export PYTHONPATH=$PWD/src
python src/main.py --url https://news.ycombinator.com --depth 3 --ai-analyze --output hn_analysis.json
```

This will:
- Crawl Hacker News 3 levels deep
- Perform AI analysis on all content
- Save enriched results to `hn_analysis.json`

### Example 3: Using Docker

```bash
# Build the image
docker build -t luminai:latest .

# Run a crawl
docker run -v $(pwd)/output:/app/output luminai:latest \
  --url https://example.com \
  --depth 2 \
  --output /app/output/results.json
```

### Example 4: Using Environment Variables

```bash
export CRAWL_DELAY=2.0
export MAX_PAGES=500
export PYTHONPATH=$PWD/src

python src/main.py --url https://example.com --depth 3 --ai-analyze
```

## Advanced Configuration

### Custom Crawler Configuration

Edit the configuration in code or use environment variables:

```bash
# Slower, more polite crawling
export CRAWL_DELAY=3.0

# Higher page limit
export MAX_PAGES=1000

# Enable AI by default
export AI_ENABLED=true
```

### Analyzing Output

The JSON output includes:

```json
[
  {
    "url": "https://example.com/page",
    "title": "Page Title",
    "text": "Extracted content...",
    "links_count": 42,
    "depth": 1,
    "ai_analysis": {
      "keywords": [
        ["keyword1", 15],
        ["keyword2", 10]
      ],
      "sentiment": "positive",
      "category": "technology",
      "word_count": 1250,
      "char_count": 7500
    }
  }
]
```

## Business Use Cases

### 1. Competitive Intelligence

Monitor competitor websites for changes:

```bash
# Crawl competitor site
python src/main.py --url https://competitor.com --depth 3 --ai-analyze --output competitor_$(date +%Y%m%d).json

# Compare with previous crawls to detect changes
```

### 2. Market Research

Aggregate industry content:

```bash
# Crawl multiple sources
for site in techcrunch.com wired.com arstechnica.com; do
  python src/main.py --url https://$site --depth 2 --ai-analyze --output ${site}_analysis.json
done
```

### 3. SEO Analysis

Analyze website structure:

```bash
# Crawl your own site
python src/main.py --url https://mysite.com --depth 5 --ai-analyze --output seo_audit.json

# Analyze keywords, sentiment, and structure
```

### 4. Content Discovery

Find related content:

```bash
# Crawl starting from a specific topic page
python src/main.py --url https://example.com/ai-topics --depth 4 --ai-analyze
```

## Integration Examples

### Python Integration

```python
import sys
sys.path.insert(0, 'src')

from crawler.web_crawler import WebCrawler
from ai.lumini_ai import LuminiAI
from utils.config import Config

# Initialize
config = Config()
crawler = WebCrawler('https://example.com', max_depth=2, config=config)

# Crawl
data = crawler.crawl()

# Analyze
ai = LuminiAI(config=config)
results = ai.analyze(data)

# Process results
for item in results:
    print(f"URL: {item['url']}")
    print(f"Category: {item['ai_analysis']['category']}")
    print(f"Sentiment: {item['ai_analysis']['sentiment']}")
    print()
```

### REST API Wrapper

You can wrap this in a Flask/FastAPI service:

```python
from flask import Flask, request, jsonify
from crawler.web_crawler import WebCrawler
from ai.lumini_ai import LuminiAI

app = Flask(__name__)

@app.route('/crawl', methods=['POST'])
def crawl_endpoint():
    data = request.json
    url = data.get('url')
    depth = data.get('depth', 2)
    
    crawler = WebCrawler(url, max_depth=depth)
    results = crawler.crawl()
    
    if data.get('ai_analyze'):
        ai = LuminiAI()
        results = ai.analyze(results)
    
    return jsonify(results)
```

## Performance Tips

1. **Rate Limiting**: Increase `CRAWL_DELAY` for slower, more polite crawling
2. **Depth Control**: Use lower depth values for faster results
3. **Domain Filtering**: The crawler only follows links on the same domain
4. **Resource Management**: Monitor memory usage for large crawls

## Troubleshooting

### Issue: "Certificate verification failed"

```bash
# For testing only - not recommended for production
export PYTHONHTTPSVERIFY=0
```

### Issue: "Too many requests / 429 error"

Increase the crawl delay:

```bash
export CRAWL_DELAY=5.0
```

### Issue: "Memory usage too high"

Reduce the maximum depth or add pagination:

```bash
python src/main.py --url https://example.com --depth 1
```

## Next Steps

- Enhance AI analysis with machine learning models
- Add database integration for storing results
- Implement distributed crawling for large-scale projects
- Add support for authenticated crawling
- Create web UI for easy management

---

For more information, see the main [README.md](README.md) or contact via GitHub issues.
