import collections
import json
from pprint import pprint


def parse_json(path):
    with open(path, 'r', encoding='utf-8') as j:
        json_data = json.load(j)
        words = []
        for news in json_data['rss']['channel']['items']:
            for word in news['description'].split():
                if len(word) > 6:
                    words.append(word)
                    counter_words = collections.Counter(words)
        pprint(counter_words.most_common(10))
    return None


if __name__ == "__main__":
    parse_json('newsafr.json')