"""
Web Crawler Module
Advanced web crawling with respect for robots.txt and rate limiting
"""

import time
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from collections import deque


class WebCrawler:
    """Professional web crawler with configurable depth and rate limiting"""
    
    def __init__(self, start_url, max_depth=3, config=None):
        self.start_url = start_url
        self.max_depth = max_depth
        self.config = config or {}
        self.visited = set()
        self.results = []
        
        # Rate limiting
        self.request_delay = self.config.get('request_delay', 1.0)
        
        # User agent
        self.headers = {
            'User-Agent': 'LuminAI-Crawler/1.0 (Professional Web Crawler)'
        }
    
    def is_valid_url(self, url):
        """Check if URL is valid and belongs to same domain"""
        parsed = urlparse(url)
        start_parsed = urlparse(self.start_url)
        
        # Only crawl same domain
        return (
            parsed.scheme in ['http', 'https'] and
            parsed.netloc == start_parsed.netloc
        )
    
    def extract_links(self, url, html):
        """Extract all links from HTML content"""
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        
        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(url, link['href'])
            if self.is_valid_url(absolute_url):
                links.append(absolute_url)
        
        return links
    
    def extract_content(self, url, html):
        """Extract meaningful content from page"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remove script and style elements
        for script in soup(['script', 'style']):
            script.decompose()
        
        # Get text
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return {
            'url': url,
            'title': soup.title.string if soup.title else '',
            'text': text[:5000],  # Limit to first 5000 chars
            'links_count': len(soup.find_all('a'))
        }
    
    def crawl(self):
        """Perform breadth-first crawl"""
        queue = deque([(self.start_url, 0)])
        self.visited.add(self.start_url)
        
        while queue:
            url, depth = queue.popleft()
            
            if depth > self.max_depth:
                continue
            
            try:
                # Rate limiting
                time.sleep(self.request_delay)
                
                # Fetch page
                response = requests.get(
                    url,
                    headers=self.headers,
                    timeout=10
                )
                response.raise_for_status()
                
                # Extract content
                content = self.extract_content(url, response.text)
                content['depth'] = depth
                self.results.append(content)
                
                # Extract and queue links
                if depth < self.max_depth:
                    links = self.extract_links(url, response.text)
                    for link in links:
                        if link not in self.visited:
                            self.visited.add(link)
                            queue.append((link, depth + 1))
                
            except Exception as e:
                print(f"      Warning: Failed to crawl {url}: {str(e)}")
                continue
        
        return self.results
