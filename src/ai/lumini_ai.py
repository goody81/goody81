"""
LuminAI Module
AI-powered content analysis and insights
"""

import re
from collections import Counter


class LuminiAI:
    """AI-powered content analyzer with NLP capabilities"""
    
    def __init__(self, config=None):
        self.config = config or {}
    
    def extract_keywords(self, text, top_n=10):
        """Extract top keywords from text"""
        # Simple keyword extraction (can be enhanced with NLP libraries)
        words = re.findall(r'\b[a-z]{4,}\b', text.lower())
        
        # Filter common stop words
        stop_words = {
            'that', 'this', 'with', 'from', 'have', 'been',
            'will', 'would', 'could', 'should', 'their', 'there',
            'about', 'which', 'when', 'where', 'what', 'your',
            'more', 'some', 'into', 'than', 'them', 'these',
            'those', 'such', 'only', 'other', 'also', 'very'
        }
        
        filtered_words = [w for w in words if w not in stop_words]
        counter = Counter(filtered_words)
        
        return counter.most_common(top_n)
    
    def analyze_sentiment(self, text):
        """Basic sentiment analysis"""
        positive_words = {
            'good', 'great', 'excellent', 'amazing', 'wonderful',
            'fantastic', 'best', 'love', 'perfect', 'awesome',
            'beautiful', 'brilliant', 'success', 'happy', 'positive'
        }
        
        negative_words = {
            'bad', 'terrible', 'awful', 'worst', 'hate', 'poor',
            'disappointing', 'failed', 'failure', 'negative', 'wrong',
            'problem', 'issue', 'error', 'difficult', 'hard'
        }
        
        words = set(re.findall(r'\b[a-z]+\b', text.lower()))
        
        pos_count = len(words & positive_words)
        neg_count = len(words & negative_words)
        
        if pos_count > neg_count:
            return 'positive'
        elif neg_count > pos_count:
            return 'negative'
        else:
            return 'neutral'
    
    def categorize_content(self, text):
        """Categorize content by topic"""
        categories = {
            'technology': ['software', 'technology', 'computer', 'digital', 
                          'code', 'programming', 'development', 'data'],
            'business': ['business', 'market', 'finance', 'sales', 
                        'revenue', 'company', 'enterprise', 'management'],
            'science': ['research', 'study', 'science', 'analysis',
                       'experiment', 'theory', 'discovery', 'scientific'],
            'education': ['education', 'learning', 'student', 'teacher',
                         'course', 'school', 'university', 'training']
        }
        
        text_lower = text.lower()
        scores = {}
        
        for category, keywords in categories.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            scores[category] = score
        
        if max(scores.values()) > 0:
            return max(scores, key=scores.get)
        return 'general'
    
    def analyze(self, crawled_data):
        """Analyze crawled data with AI"""
        analyzed = []
        
        for item in crawled_data:
            text = item.get('text', '')
            
            analysis = {
                **item,
                'ai_analysis': {
                    'keywords': self.extract_keywords(text),
                    'sentiment': self.analyze_sentiment(text),
                    'category': self.categorize_content(text),
                    'word_count': len(text.split()),
                    'char_count': len(text)
                }
            }
            
            analyzed.append(analysis)
        
        return analyzed
