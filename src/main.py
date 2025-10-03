#!/usr/bin/env python3
"""
LuminAI Integrated Web Crawler & AI Platform
Main application entry point
"""

import sys
import argparse
from crawler.web_crawler import WebCrawler
from ai.lumini_ai import LuminiAI
from utils.config import Config


def main():
    """Main application entry point"""
    parser = argparse.ArgumentParser(
        description='LuminAI - Integrated Web Crawler & AI Platform'
    )
    parser.add_argument(
        '--url',
        type=str,
        help='Starting URL for web crawling'
    )
    parser.add_argument(
        '--depth',
        type=int,
        default=3,
        help='Maximum crawl depth (default: 3)'
    )
    parser.add_argument(
        '--ai-analyze',
        action='store_true',
        help='Enable AI analysis of crawled content'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='output.json',
        help='Output file for results'
    )
    
    args = parser.parse_args()
    
    # Load configuration
    config = Config()
    
    print("=" * 60)
    print("LuminAI - Integrated Web Crawler & AI Platform")
    print("=" * 60)
    
    if not args.url:
        print("\nError: Please provide a starting URL with --url")
        parser.print_help()
        sys.exit(1)
    
    # Initialize crawler
    print(f"\n[1/3] Initializing Web Crawler...")
    crawler = WebCrawler(
        start_url=args.url,
        max_depth=args.depth,
        config=config
    )
    
    # Crawl websites
    print(f"[2/3] Crawling from: {args.url}")
    crawled_data = crawler.crawl()
    print(f"      Successfully crawled {len(crawled_data)} pages")
    
    # AI Analysis
    if args.ai_analyze:
        print(f"[3/3] Running AI Analysis...")
        ai = LuminiAI(config=config)
        analyzed_data = ai.analyze(crawled_data)
        print(f"      AI analysis complete")
    else:
        analyzed_data = crawled_data
        print(f"[3/3] Skipping AI analysis")
    
    # Save results
    import json
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(analyzed_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Results saved to: {args.output}")
    print("=" * 60)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
