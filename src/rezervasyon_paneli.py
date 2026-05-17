"""
Rezervasyon Paneli - v0.4
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QFrame, QMessageBox
)
from PyQt5.QtCore import Qt, pyqtSignal


class RezervasyonKarti(QFrame):
    checkin_clicked = pyqtSignal(dict)
    iptal_clicked = pyqtSignal(dict)
    sil_clicked = pyqtSignal(dict)

    def __init__(self, rezervasyon, parent=None):
        super().__init__(parent)
        self.rezervasyon = rezervasyon
        self.setObjectName("rezervKart")
        self.setFrameShape(QFrame.StyledPanel)
        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 14, 16, 14)
        layout.setSpacing(14)

        isim = str(self.rezervasyon.get('isim', ''))
        soyisim = str(self.rezervasyon.get('soyisim', ''))
        sirket = str(self.rezervasyon.get('sirket', '') or '')
        oda = str(self.rezervasyon.get('oda', ''))
        giris = str(self.rezervasyon.get('giris', ''))
        cikis = str(self.rezervasyon.get('cikis', '') or '')

        # Avatar
        initials = f"{isim[:1]}{soyisim[:1]}".upper() if isim and soyisim else "?"
        avatar = QLabel(initials)
        avatar.setFixedSize(46, 46)
        avatar.setAlignment(Qt.AlignCenter)
        avatar.setStyleSheet("""
            QLabel {
                background-color: #fde68a; color: #92400e;
                border-radius: 23px; font-size: 13pt; font-weight: bold;
            }
        """)
        layout.addWidget(avatar)

        info = QVBoxLayout()
        info.setSpacing(3)

        isim_lbl = QLabel(f"{isim} {soyisim}")
        isim_lbl.setObjectName("musteriIsim")
        info.addWidget(isim_lbl)

        if sirket:
            sirket_lbl = QLabel(sirket)
            sirket_lbl.setStyleSheet("color: #92400e; font-size: 9pt; font-style: italic;")
            info.addWidget(sirket_lbl)

        alt_row = QHBoxLayout()
        alt_row.setSpacing(8)
        oda_lbl = QLabel(f"Oda {oda}")
        oda_lbl.setStyleSheet("""
            font-size: 9pt; color: #92400e; font-weight: 600;
            background-color: rgba(251,191,36,0.20);
            border: 1px solid #fbbf24; border-radius: 4px; padding: 1px 7px;
        """)
        alt_row.addWidget(oda_lbl)
        tarih_lbl = QLabel(f"  •  Giris: {giris}  —  Cikis: {cikis}")
        tarih_lbl.setObjectName("musteriTarih")
        alt_row.addWidget(tarih_lbl)
        alt_row.addStretch()
        info.addLayout(alt_row)
        layout.addLayout(info)
        layout.addStretch()

        # Sag: badge + butonlar
        sag = QVBoxLayout()
        sag.setSpacing(8)
        sag.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        badge = QLabel("REZERVE")
        badge.setObjectName("rezervBadge")
        badge.setAlignment(Qt.AlignCenter)
        sag.addWidget(badge)

        btn_row = QHBoxLayout()
        btn_row.setSpacing(6)

        btn_checkin = QPushButton("Check-in Yap")
        btn_checkin.setObjectName("btnCheckin")
        btn_checkin.clicked.connect(lambda: self.checkin_clicked.emit(self.rezervasyon))
        btn_row.addWidget(btn_checkin)

        btn_iptal = QPushButton("Iptal")
        btn_iptal.setObjectName("btnIptal")
        btn_iptal.clicked.connect(lambda: self.iptal_clicked.emit(self.rezervasyon))
        btn_row.addWidget(btn_iptal)

        btn_sil = QPushButton("Sil")
        btn_sil.setObjectName("btnSil")
        btn_sil.setFixedWidth(50)
        btn_sil.clicked.connect(lambda: self.sil_clicked.emit(self.rezervasyon))
        btn_row.addWidget(btn_sil)

        sag.addLayout(btn_row)
        layout.addLayout(sag)


class RezervasyonPaneli(QWidget):
    guncelleme_gerekli = pyqtSignal()

    def __init__(self, data_manager, parent=None):
        super().__init__(parent)
        self.dm = data_manager
        self._setup_ui()
        self.refresh()

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(12)

        card = QFrame()
        card.setObjectName("mainCard")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(24, 20, 24, 20)
        card_layout.setSpacing(10)
        main_layout.addWidget(card)

        baslik_row = QHBoxLayout()
        col = QVBoxLayout()
        col.setSpacing(2)
        baslik = QLabel("Rezervasyonlar")
        baslik.setObjectName("panelTitle")
        col.addWidget(baslik)
        self.subtitle_lbl = QLabel("Bekleyen rezervasyonlar")
        self.subtitle_lbl.setObjectName("panelSubtitle")
        col.addWidget(self.subtitle_lbl)
        baslik_row.addLayout(col)
        baslik_row.addStretch()
        card_layout.addLayout(baslik_row)

        sep = QFrame()
        sep.setFixedHeight(1)
        sep.setStyleSheet("background-color: #f1f5f9;")
        card_layout.addWidget(sep)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setFrameShape(QFrame.NoFrame)
        self.scroll.setStyleSheet("background: transparent;")
        card_layout.addWidget(self.scroll)

        self.scroll_widget = QWidget()
        self.scroll_widget.setStyleSheet("background: transparent;")
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setSpacing(6)
        self.scroll_layout.addStretch()
        self.scroll.setWidget(self.scroll_widget)

    def refresh(self):
        while self.scroll_layout.count() > 1:
            item = self.scroll_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        rezervasyonlar = self.dm.get_rezervasyonlar()
        self.subtitle_lbl.setText(f"{len(rezervasyonlar)} bekleyen rezervasyon")

        if not rezervasyonlar:
            bos = QLabel("Su an bekleyen rezervasyon bulunmuyor.")
            bos.setAlignment(Qt.AlignCenter)
            bos.setStyleSheet("color: #cbd5e1; font-size: 12pt; padding: 50px;")
            self.scroll_layout.insertWidget(0, bos)
            return

        for r in rezervasyonlar:
            kart = RezervasyonKarti(r)
            kart.checkin_clicked.connect(self._on_checkin)
            kart.iptal_clicked.connect(self._on_iptal)
            kart.sil_clicked.connect(self._on_sil)
            self.scroll_layout.insertWidget(self.scroll_layout.count() - 1, kart)

    def _on_checkin(self, rezervasyon):
        isim = f"{rezervasyon.get('isim','')} {rezervasyon.get('soyisim','')}"
        reply = QMessageBox.question(self, "Check-in Onayi",
            f"{isim} icin check-in yapilsin mi?\n"
            f"Rezervasyon aktif kayda donusturulecek.",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if self.dm.rezervasyon_checkin(rezervasyon["id"]):
                QMessageBox.information(self, "Basarili", f"{isim} check-in yapildi!")
                self.guncelleme_gerekli.emit()
            else:
                QMessageBox.critical(self, "Hata", "Check-in islemi basarisiz.")

    def _on_iptal(self, rezervasyon):
        isim = f"{rezervasyon.get('isim','')} {rezervasyon.get('soyisim','')}"
        reply = QMessageBox.question(self, "Iptal Onayi",
            f"{isim} rezervasyonu iptal edilsin mi?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if self.dm.rezervasyon_iptal(rezervasyon["id"]):
                self.refresh()
            else:
                QMessageBox.critical(self, "Hata", "Iptal islemi basarisiz.")

    def _on_sil(self, rezervasyon):
        isim = f"{rezervasyon.get('isim','')} {rezervasyon.get('soyisim','')}"
        reply = QMessageBox.question(self, "Rezervasyon Silme",
            f"{isim} rezervasyonunu kalici olarak silmek istiyor musunuz?\n\nBu islem geri alinamaz!",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if self.dm.rezervasyon_sil(rezervasyon["id"]):
                self.refresh()
            else:
                QMessageBox.critical(self, "Hata", "Silme islemi basarisiz.")
