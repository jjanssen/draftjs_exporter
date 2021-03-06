from __future__ import absolute_import, unicode_literals

from lxml import etree, html

from draftjs_exporter.constants import BLOCK_TYPES, ENTITY_TYPES, INLINE_STYLES
from draftjs_exporter.entities.image import Image
from draftjs_exporter.entities.link import Link
from draftjs_exporter.html import HTML

# TODO Support dt/dd, hr, br, cite, mark, q, s, sub, sup, video?
config = {
    'entity_decorators': {
        ENTITY_TYPES.LINK: Link(),
        ENTITY_TYPES.IMAGE: Image(),
    },
    'block_map': {
        BLOCK_TYPES.UNSTYLED: {'element': 'p'},
        BLOCK_TYPES.HEADER_ONE: {'element': 'h1'},
        BLOCK_TYPES.HEADER_TWO: {'element': 'h2'},
        BLOCK_TYPES.HEADER_THREE: {'element': 'h3'},
        BLOCK_TYPES.HEADER_FOUR: {'element': 'h4'},
        BLOCK_TYPES.HEADER_FIVE: {'element': 'h5'},
        BLOCK_TYPES.HEADER_SIX: {'element': 'h6'},
        BLOCK_TYPES.UNORDERED_LIST_ITEM: {'element': 'li', 'wrapper': ['ul', {'className': 'bullet-list'}]},
        BLOCK_TYPES.ORDERED_LIST_ITEM: {'element': 'li', 'wrapper': ['ol', {}]},
        BLOCK_TYPES.BLOCKQUOTE: {'element': 'blockquote'},
        # TODO Ideally would want double wrapping in pre + code.
        # See https://github.com/sstur/draft-js-export-html/blob/master/src/stateToHTML.js#L88
        BLOCK_TYPES.CODE: {'element': 'pre'},
    },
    'style_map': {
        INLINE_STYLES.ITALIC: {'element': 'em'},
        INLINE_STYLES.BOLD: {'element': 'strong'},
        INLINE_STYLES.CODE: {'element': 'code'},
        INLINE_STYLES.STRIKETHROUGH: {'textDecoration': 'line-through'},
        INLINE_STYLES.UNDERLINE: {'textDecoration': 'underline'},
    },
}

exporter = HTML(config)

content_state = {
    'entityMap': {
        '0': {
            'type': 'LINK',
            'mutability': 'MUTABLE',
            'data': {
                'url': 'http://example.com'
            }
        },
        '1': {
            'type': 'LINK',
            'mutability': 'MUTABLE',
            'data': {
                'url': 'https://www.springload.co.nz/work/nz-festival/'
            }
        }
    },
    'blocks': [
        {
            'key': '6mgfh',
            'text': 'User experience (UX) design',
            'type': 'header-two',
            'depth': 0,
            'inlineStyleRanges': [
                {
                    'offset': 16,
                    'length': 4,
                    'style': 'BOLD'
                }
            ],
            'entityRanges': []
        },
        {
            'key': '5384u',
            'text': 'Everyone at Springload applies the best principles of UX to their work.',
            'type': 'blockquote',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        },
        {
            'key': 'eelkd',
            'text': 'The design decisions we make building tools and services for your customers are based on empathy for what your customers need.',
            'type': 'unstyled',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        },
        {
            'key': 'b9grk',
            'text': 'User research',
            'type': 'unordered-list-item',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        },
        {
            'key': 'a1tis',
            'text': 'User testing and analysis',
            'type': 'unordered-list-item',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': [
                {
                    'offset': 0,
                    'length': 25,
                    'key': 0
                }
            ]
        },
        {
            'key': 'adjdn',
            'text': 'A/B testing',
            'type': 'unordered-list-item',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        },
        {
            'key': '62lio',
            'text': 'Prototyping',
            'type': 'unordered-list-item',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        },
        {
            'key': '62lio',
            # TODO Test HTML entities encoding
            'text': 'Beautiful <code/>',
            'type': 'unordered-list-item',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': []
        },
        {
            'key': 'fq3f',
            'text': 'How we made it delightful and easy for people to find NZ Festival shows',
            'type': 'unstyled',
            'depth': 0,
            'inlineStyleRanges': [],
            'entityRanges': [
                {
                    'offset': 0,
                    'length': 71,
                    'key': 1
                }
            ]
        }
    ]
}

markup = exporter.call(content_state)
# Pretty print the markup, removing the top-level node that lxml adds.
document_root = html.fromstring('<root>%s</root>' % markup)
print(etree.tostring(document_root, encoding='unicode', pretty_print=True).replace('<root>', '').replace('</root>', ''))
