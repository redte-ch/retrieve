#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class Proxies(Base):
    __tablename__ = "proxies"

    proxyID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    multiHost: Mapped[int | None] = mapped_column(Integer)
    autoAssociate: Mapped[int | None] = mapped_column(Integer)
    scheme: Mapped[str | None] = mapped_column(Text)

    proxyHosts: Mapped[list["ProxyHosts"]] = relationship(
        "ProxyHosts", back_populates="proxies"
    )
