#!/usr/bin/env python3
"""
Simple test to verify the application components work
"""

import sys
sys.path.insert(0, 'src')

from crawler.web_crawler import WebCrawler
from ai.lumini_ai import LuminiAI
from utils.config import Config

def test_config():
    """Test configuration module"""
    config = Config()
    assert config.get('request_delay') is not None
    print("✓ Config module works")

def test_lumini_ai():
    """Test AI analysis module"""
    ai = LuminiAI()
    
    # Test keyword extraction
    text = "Python programming language is great for software development"
    keywords = ai.extract_keywords(text)
    assert len(keywords) > 0
    print(f"✓ AI keyword extraction works: {keywords[:3]}")
    
    # Test sentiment analysis
    positive_text = "This is excellent and amazing software"
    sentiment = ai.analyze_sentiment(positive_text)
    assert sentiment in ['positive', 'negative', 'neutral']
    print(f"✓ AI sentiment analysis works: {sentiment}")
    
    # Test categorization
    tech_text = "software development programming computer technology"
    category = ai.categorize_content(tech_text)
    assert category is not None
    print(f"✓ AI categorization works: {category}")

def test_crawler_structure():
    """Test crawler module structure"""
    # Test instantiation
    crawler = WebCrawler('https://example.com', max_depth=1)
    assert crawler.start_url == 'https://example.com'
    assert crawler.max_depth == 1
    print("✓ Crawler module structure works")
    
    # Test URL validation
    assert crawler.is_valid_url('https://example.com/page')
    assert not crawler.is_valid_url('https://different.com/page')
    print("✓ Crawler URL validation works")

def test_integration():
    """Test module integration"""
    config = Config()
    
    # Mock crawl data
    mock_data = [{
        'url': 'https://example.com',
        'title': 'Example',
        'text': 'This is great software for technology development',
        'links_count': 5,
        'depth': 0
    }]
    
    # Test AI analysis
    ai = LuminiAI(config=config)
    results = ai.analyze(mock_data)
    
    assert len(results) == 1
    assert 'ai_analysis' in results[0]
    assert 'keywords' in results[0]['ai_analysis']
    assert 'sentiment' in results[0]['ai_analysis']
    assert 'category' in results[0]['ai_analysis']
    
    print("✓ Module integration works")
    print(f"  - Keywords: {results[0]['ai_analysis']['keywords'][:3]}")
    print(f"  - Sentiment: {results[0]['ai_analysis']['sentiment']}")
    print(f"  - Category: {results[0]['ai_analysis']['category']}")

if __name__ == '__main__':
    print("=" * 60)
    print("Running LuminAI Component Tests")
    print("=" * 60)
    print()
    
    try:
        test_config()
        test_lumini_ai()
        test_crawler_structure()
        test_integration()
        
        print()
        print("=" * 60)
        print("✅ All tests passed!")
        print("=" * 60)
        sys.exit(0)
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
