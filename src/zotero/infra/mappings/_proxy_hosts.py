#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import ForeignKey, Index, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class ProxyHosts(Base):
    __tablename__ = "proxyHosts"
    __table_args__ = (Index("proxyHosts_proxyID", "proxyID"),)

    hostID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    proxyID: Mapped[int | None] = mapped_column(ForeignKey("proxies.proxyID"))
    hostname: Mapped[str | None] = mapped_column(Text)

    proxies: Mapped["Proxies"] = relationship("Proxies", back_populates="proxyHosts")
