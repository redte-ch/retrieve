#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import zotero_qa


def test_a_document_is_a_unique_piece_of_knowledge():
    # Arrange
    document = zotero_qa.Document(
        authors=[{"first_name": "Mauko", "last_name": "Quiroga-Alvarado"}],
        title="Practical Domain-Driven Design in the Public Sector",
        date=2024,
        summary="How to use domain-driven design in the public sector",
        content="...",
    )
    different_author = zotero_qa.Document(
        authors=[{"first_name": "Brunildo", "last_name": "Soto"}],
        title="Practical Domain-Driven Design in the Public Sector",
        date=2024,
        summary="How to use domain-driven design in the public sector",
        content="...",
    )
    different_title = zotero_qa.Document(
        authors=[{"first_name": "Mauko", "last_name": "Quiroga-Alvarado"}],
        title="Unpractical Feature-Driven Design in the Public Sector",
        date=2024,
        summary="How to use domain-driven design in the public sector",
        content="...",
    )
    different_date = zotero_qa.Document(
        authors=[{"first_name": "Mauko", "last_name": "Quiroga-Alvarado"}],
        title="Practical Domain-Driven Design in the Public Sector",
        date=2027,
        summary="How to use domain-driven design in the public sector",
        content="...",
    )
    different_summary = zotero_qa.Document(
        authors=[{"first_name": "Mauko", "last_name": "Quiroga-Alvarado"}],
        title="Practical Domain-Driven Design in the Public Sector",
        date=2024,
        summary="How not to use feature-driven design in the public sector",
        content="...",
    )
    different_content = zotero_qa.Document(
        authors=[{"first_name": "Mauko", "last_name": "Quiroga-Alvarado"}],
        title="Practical Domain-Driven Design in the Public Sector",
        date=2024,
        summary="...",
        content="The most prevalent anti-pattern in the public sector is...",
    )

    # Assert
    assert document != different_author
    assert document != different_title
    assert document != different_date
    assert document == different_summary
    assert document == different_content
