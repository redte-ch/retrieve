#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
#
#  cython: language_level=3

"""Zotero QA allows you to chat with your Zotero PDF collections."""

from zotero_qa._pdf cimport DocLoader, Page, PageParser
from zotero_qa._text cimport DocSplitter, TextSplitter
