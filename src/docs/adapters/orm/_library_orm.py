#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlmodel import Field, SQLModel


class LibraryORM(SQLModel, table=True):
    libraryID: int = Field(primary_key=True)
    type: str
    editable: int
    filesEditable: int
    version: int = Field(default=0)
    storageVersion: int = Field(default=0)
    lastSync: int = Field(default=0)
    archived: int = Field(default=0)
