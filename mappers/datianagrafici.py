# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, String, Text, text
from sqlalchemy.dialects.mysql import LONGTEXT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Elencoappellativi(Base):
    __tablename__ = 'elencoappellativi'
    __table_args__ = {'comment': 'Contiene un elenco modificabile di Appellativi'}

    idAppellativo = Column(Integer, primary_key=True, unique=True)
    AppellativoEsteso = Column(String(45))
    AppellativoRidotto = Column(String(45))
    InsData = Column(DateTime)
    InsUtente = Column(String(256))
    InsComputer = Column(String(256))
    ModData = Column(DateTime)
    ModUtente = Column(String(256))
    ModComputer = Column(String(256))


class Elencotitolionorifici(Base):
    __tablename__ = 'elencotitolionorifici'

    idTitoloOnorifico = Column(Integer, primary_key=True, unique=True)
    TitoloOnorificoEsteso = Column(String(45))
    TitoloOnorificoRidotto = Column(String(45))
    InsData = Column(DateTime)
    InsUtente = Column(String(256))
    InsComputer = Column(String(256))
    ModData = Column(DateTime)
    ModUtente = Column(String(256))
    ModComputer = Column(String(256))


class LNazione(Base):
    __tablename__ = 'l_nazione'

    IDNazioneIstat = Column(BigInteger, primary_key=True)
    Nazione = Column(Text)
    Cittadinanza = Column(Text)
    CodBelfiore = Column(Text)
    IsoAlpha2 = Column(Text)
    IsoAlpha3 = Column(Text)
    SostituitoDa = Column(Text)
    AppartieneA = Column(Text)
    flgComunitario = Column(TINYINT)


class LmComuneitaliano(Base):
    __tablename__ = 'lm_comuneitaliano'

    IDComune = Column(Integer, primary_key=True)
    CodBelfiore = Column(Text)
    CodCatastale = Column(Text)
    CodIstat = Column(Text)
    SiglaProvincia = Column(Text)
    Comune = Column(Text)
    CAP = Column(Text)
    Prefisso = Column(Text)
    flgEsisteAncora = Column(Integer)
    flgCambiatoNome = Column(Integer)
    flgAggregato = Column(Integer)
    TipoVariazione = Column(Text)
    VarCodBelfiore = Column(Text)
    VarCodCatastale = Column(Text)
    VarProvincia = Column(Text)
    VarComune = Column(Text)
    flgModificabile = Column(Integer)
    InsData = Column(Text)
    InsUtente = Column(Text)
    InsComputer = Column(Text)
    ModData = Column(Text)
    ModUtente = Column(Text)
    ModComputer = Column(Text)


class Datianagrafici(Base):
    __tablename__ = 'datianagrafici'
    __table_args__ = {'comment': 'Contiene i principali dati anagrafici delle persone.'}

    idDatiAnagrafici = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    Cognome1 = Column(String(256))
    Cognome2 = Column(String(256))
    Cognome3 = Column(String(256))
    Cognome5 = Column(String(256))
    Cognome6 = Column(String(256))
    Nome1 = Column(String(256))
    Nome2 = Column(String(256))
    Nome3 = Column(String(256))
    Nome4 = Column(String(256))
    Nome5 = Column(String(256))
    Nome6 = Column(String(256))
    Alias = Column(String(256))
    CodiceFiscale = Column(String(16), nullable=False, index=True, server_default=text("''"))
    CodiceIdentificatoreUnivoco = Column(String(256), nullable=False, server_default=text("''"), comment='Utilizzato per anagrafiche di uno stato che non hanno il nostro Codice Fiscale (ex. San Marino)')
    Sesso = Column(String(1))
    StatoNascitaTesto = Column(String(45))
    IdStatoNascita = Column(ForeignKey('l_nazione.IDNazioneIstat'), index=True)
    ProvinciaNascitaTesto = Column(String(256))
    ProvinciaNascitaSigla = Column(String(256))
    ComuneNascitaTesto = Column(String(256))
    IdComuneNascita = Column(ForeignKey('lm_comuneitaliano.IDComune'), index=True)
    LocalitaFrazioneNascitaTesto = Column(String(256))
    DataNascita = Column(DateTime)
    IdTitoloOnorifico = Column(ForeignKey('elencotitolionorifici.idTitoloOnorifico'), index=True)
    IdAppellativo = Column(ForeignKey('elencoappellativi.idAppellativo'), index=True)
    Cittadinanza = Column(String(256))
    PartitaIVA = Column(String(45))
    Note = Column(LONGTEXT)
    InsData = Column(DateTime)
    InsUtente = Column(String(256))
    InsComputer = Column(String(256))
    ModData = Column(DateTime)
    ModUtente = Column(String(256))
    ModComputer = Column(String(256))

    elencoappellativi = relationship('Elencoappellativi')
    lm_comuneitaliano = relationship('LmComuneitaliano')
    l_nazione = relationship('LNazione')
    elencotitolionorifici = relationship('Elencotitolionorifici')
