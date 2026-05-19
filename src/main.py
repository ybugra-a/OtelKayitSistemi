"""
Otel Kayit ve Oda Yonetim Sistemi - v0.4
"""

import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QMessageBox, QPushButton, QFrame, QStackedWidget, QSizePolicy
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QIcon

from data_manager import DataManager
from kayit_modulu import KayitModulu
from aktif_musteri_paneli import AktifMusteriPaneli
from rezervasyon_paneli import RezervasyonPaneli
from oda_durumu_paneli import OdaDurumuPaneli
from arama_arsiv import AramaArsiv
from blacklist_modulu import BlacklistModulu
from ayarlar import Ayarlar
from styles import MAIN_STYLE


def get_icon_path():
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, "otel_icon.png")
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "otel_icon.png")


class OtelKayitApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data_manager = DataManager()
        self.setWindowTitle("Otel Kayit ve Oda Yonetim Sistemi")
        self.setMinimumSize(1280, 720)
        # ikon devre disi - v0.5'te guncellenecek
        # icon_path = get_icon_path()
        # if os.path.exists(icon_path):
        #     self.setWindowIcon(QIcon(icon_path))
        self._setup_ui()
        self._check_backup_warning()
        QTimer.singleShot(800, self._check_bekleyen_rezervasyonlar)

    def _setup_ui(self):
        self.setStyleSheet(MAIN_STYLE)
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        nav = self._create_navbar()
        main_layout.addWidget(nav)

        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(20, 16, 20, 16)
        content_layout.setSpacing(14)

        self.stat_bar = self._create_stat_bar()
        content_layout.addWidget(self.stat_bar)

        self.stack = QStackedWidget()
        content_layout.addWidget(self.stack)
        main_layout.addWidget(content)

        self._create_pages()
        self._switch_page(0)

    def _create_navbar(self):
        nav = QWidget()
        nav.setObjectName("navBar")
        nav.setFixedHeight(58)
        layout = QHBoxLayout(nav)
        layout.setContentsMargins(24, 0, 24, 0)
        layout.setSpacing(4)

        title = QLabel("Otel Kayit Sistemi")
        title.setObjectName("appTitle")
        layout.addWidget(title)
        layout.addSpacing(24)

        self._nav_buttons = []
        nav_items = [
            ("Kayit", 0),
            ("Aktif Misafirler", 1),
            ("Rezervasyonlar", 2),
            ("Oda Durumu", 3),
            ("Arsiv", 4),
            ("Kara Liste", 5),
            ("Ayarlar", 6),
        ]
        for label, idx in nav_items:
            btn = QPushButton(label)
            btn.setObjectName("navBtn")
            btn.clicked.connect(lambda checked, i=idx: self._switch_page(i))
            btn.setCursor(Qt.PointingHandCursor)
            layout.addWidget(btn)
            self._nav_buttons.append(btn)

        layout.addStretch()
        return nav

    def _create_stat_bar(self):
        bar = QWidget()
        layout = QHBoxLayout(bar)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(14)

        self.stat_dolu = self._make_stat_card(False)
        self.stat_musait = self._make_stat_card(True)
        layout.addWidget(self.stat_dolu)
        layout.addWidget(self.stat_musait)
        return bar

    def _make_stat_card(self, is_green):
        card = QFrame()
        card.setObjectName("statKart")
        card.setFixedHeight(100)
        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 14, 20, 14)
        layout.setSpacing(6)

        baslik_lbl = QLabel("MUSAIT ODALAR" if is_green else "DOLULUK ORANI")
        baslik_lbl.setObjectName("statBaslik")
        layout.addWidget(baslik_lbl)

        deger_lbl = QLabel("0 Oda")
        deger_lbl.setObjectName("statDeger")
        layout.addWidget(deger_lbl)

        from PyQt5.QtWidgets import QProgressBar
        progress = QProgressBar()
        progress.setFixedHeight(6)
        progress.setTextVisible(False)
        progress.setValue(0)
        if is_green:
            progress.setStyleSheet("QProgressBar { background: #1e1e30; border-radius: 4px; } QProgressBar::chunk { background: #22c55e; border-radius: 4px; }")
            self._stat_musait_lbl = deger_lbl
            self._stat_musait_prog = progress
        else:
            progress.setStyleSheet("QProgressBar { background: #1e1e30; border-radius: 4px; } QProgressBar::chunk { background: #475569; border-radius: 4px; }")
            self._stat_dolu_lbl = deger_lbl
            self._stat_dolu_prog = progress
        layout.addWidget(progress)
        return card

    def _update_stats(self):
        odalar = self.data_manager.get_odalar()
        toplam = len(odalar)
        dolu = sum(1 for o in odalar if o["durum"] == "Dolu")
        musait = toplam - dolu
        self._stat_dolu_lbl.setText(f"{dolu} Oda Dolu")
        self._stat_musait_lbl.setText(f"{musait} Oda Musait")
        if toplam > 0:
            self._stat_dolu_prog.setValue(int(dolu / toplam * 100))
            self._stat_musait_prog.setValue(int(musait / toplam * 100))

    def _create_pages(self):
        # Sayfa 0: Kayit + Aktif yan yana
        kayit_page = QWidget()
        kayit_page.setStyleSheet("background: transparent;")
        kl = QHBoxLayout(kayit_page)
        kl.setContentsMargins(0, 0, 0, 0)
        kl.setSpacing(14)

        self.kayit_modulu = KayitModulu(self.data_manager)
        self.kayit_modulu.kayit_yapildi.connect(self._on_kayit_yapildi)
        self.kayit_modulu.rezervasyon_yapildi.connect(self._on_rezervasyon_yapildi)
        kl.addWidget(self.kayit_modulu, 42)

        self.aktif_panel = AktifMusteriPaneli(self.data_manager)
        self.aktif_panel.guncelleme_gerekli.connect(self._refresh_all)
        kl.addWidget(self.aktif_panel, 58)
        self.stack.addWidget(kayit_page)           # 0

        # Sayfa 1: Aktif misafirler tam
        self.aktif_panel_full = AktifMusteriPaneli(self.data_manager)
        self.aktif_panel_full.guncelleme_gerekli.connect(self._refresh_all)
        self.stack.addWidget(self.aktif_panel_full) # 1

        # Sayfa 2: Rezervasyonlar
        self.rezervasyon_paneli = RezervasyonPaneli(self.data_manager)
        self.rezervasyon_paneli.guncelleme_gerekli.connect(self._refresh_all)
        self.stack.addWidget(self.rezervasyon_paneli) # 2

        # Sayfa 3: Oda durumu
        self.oda_paneli = OdaDurumuPaneli(self.data_manager)
        self.oda_paneli.oda_degisti.connect(self._on_oda_degisti)
        self.stack.addWidget(self.oda_paneli)       # 3

        # Sayfa 4: Arsiv
        self.arama_modulu = AramaArsiv(self.data_manager)
        self.arama_modulu.guncelleme_gerekli.connect(self._refresh_all)
        self.stack.addWidget(self.arama_modulu)     # 4

        # Sayfa 5: Kara Liste
        self.blacklist_modulu = BlacklistModulu(self.data_manager)
        self.stack.addWidget(self.blacklist_modulu) # 5

        # Sayfa 6: Ayarlar
        self.ayarlar_modulu = Ayarlar(self.data_manager)
        self.ayarlar_modulu.oda_degisti.connect(self._refresh_all)
        self.stack.addWidget(self.ayarlar_modulu)   # 6

    def _switch_page(self, index):
        self.stack.setCurrentIndex(index)
        self.stat_bar.setVisible(index == 0)
        for i, btn in enumerate(self._nav_buttons):
            btn.setObjectName("navBtnActive" if i == index else "navBtn")
            btn.setStyle(btn.style())
        if index == 0:
            self._update_stats()
            self.aktif_panel.refresh()
        elif index == 1:
            self.aktif_panel_full.refresh()
        elif index == 2:
            self.rezervasyon_paneli.refresh()
        elif index == 3:
            self.oda_paneli.refresh()
        elif index == 6:
            self.ayarlar_modulu.refresh()

    def _on_kayit_yapildi(self):
        self.aktif_panel.refresh()
        self.aktif_panel_full.refresh()
        self.oda_paneli.refresh()
        self.kayit_modulu.refresh_oda_listesi()
        self._update_stats()

    def _on_rezervasyon_yapildi(self):
        self.rezervasyon_paneli.refresh()

    def _on_oda_degisti(self):
        self.kayit_modulu.refresh_oda_listesi()
        self.aktif_panel.refresh()
        self.aktif_panel_full.refresh()
        self._update_stats()

    def _refresh_all(self):
        self.aktif_panel.refresh()
        self.aktif_panel_full.refresh()
        self.rezervasyon_paneli.refresh()
        self.oda_paneli.refresh()
        self.kayit_modulu.refresh_oda_listesi()
        self.arama_modulu.refresh()
        self._update_stats()

    def _check_bekleyen_rezervasyonlar(self):
        bekleyenler = self.data_manager.get_bekleyen_rezervasyonlar()
        if not bekleyenler:
            return
        isimler = "\n".join(
            f"  • {r.get('isim','')} {r.get('soyisim','')} — Oda {r.get('oda','')} — Giris: {r.get('giris','')}"
            for r in bekleyenler
        )
        reply = QMessageBox.question(self, "Bekleyen Rezervasyonlar",
            f"Giris tarihi gelen {len(bekleyenler)} rezervasyon var:\n\n{isimler}\n\n"
            f"Rezervasyonlar sekmesine gitmek ister misiniz?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self._switch_page(2)

    def _check_backup_warning(self):
        if self.data_manager.check_backup_needed():
            QTimer.singleShot(500, self._show_backup_warning)

    def _show_backup_warning(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Yedekleme Hatirlatmasi")
        msg.setIcon(QMessageBox.Warning)
        msg.setText(
            "Son yedeklemenin uzerinden 30 gun gecti.\n\n"
            f"Lutfen kayitlar.xlsx dosyasini yedekleyin.\n\n"
            f"Dosya: {self.data_manager.get_excel_path()}"
        )
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Otel Kayit Sistemi")
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    # ikon devre disi - v0.5'te guncellenecek
    window = OtelKayitApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
