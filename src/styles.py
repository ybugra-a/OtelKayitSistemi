"""
Uygulama stilleri - v0.4
"""

MAIN_STYLE = """
QWidget {
    font-family: 'Segoe UI', Tahoma, Arial;
    font-size: 10pt;
    color: #1e293b;
    background-color: #f1f5f9;
}
QMainWindow { background-color: #f1f5f9; }

#navBar {
    background-color: #ffffff;
    border-bottom: 1px solid #e2e8f0;
}
#appTitle {
    font-size: 13pt; font-weight: bold; color: #0f172a; letter-spacing: -0.3px;
}
#navBtn {
    background: transparent; color: #64748b; border: none;
    border-radius: 20px; padding: 7px 18px; font-size: 10pt;
    font-weight: 500; min-height: 34px;
}
#navBtn:hover { background-color: #f1f5f9; color: #1e293b; }
#navBtnActive {
    background-color: #0f172a; color: #ffffff; border: none;
    border-radius: 20px; padding: 7px 18px; font-size: 10pt;
    font-weight: 600; min-height: 34px;
}
#navBtnActive:hover { background-color: #1e293b; }

#statKart { background-color: #ffffff; border-radius: 14px; border: 1px solid #e2e8f0; }
#statBaslik { font-size: 8pt; font-weight: bold; color: #94a3b8; letter-spacing: 0.8px; }
#statDeger { font-size: 22pt; font-weight: bold; color: #0f172a; letter-spacing: -0.5px; }

#panelTitle { font-size: 16pt; font-weight: bold; color: #0f172a; letter-spacing: -0.3px; }
#panelSubtitle { font-size: 9pt; color: #94a3b8; }
#mainCard { background-color: #ffffff; border-radius: 16px; border: 1px solid #e2e8f0; }
#formLabel { font-size: 8pt; font-weight: bold; color: #64748b; letter-spacing: 0.5px; }

QLineEdit, QComboBox, QDateEdit, QDoubleSpinBox {
    background-color: #ffffff; border: 1.5px solid #e2e8f0;
    border-radius: 8px; padding: 9px 12px; font-size: 10pt;
    color: #1e293b; min-height: 22px;
}
QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QDoubleSpinBox:focus {
    border: 1.5px solid #2563eb;
}
QLineEdit:hover, QComboBox:hover { border-color: #cbd5e1; }

/* BUG 4 - Sky blue dropdown oklar */
QComboBox::drop-down {
    border: none; width: 28px;
    background-color: transparent;
}
QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 6px solid #38bdf8;
    margin-right: 8px;
}
QDateEdit::drop-down {
    border: none; width: 28px;
    background-color: transparent;
}
QDateEdit::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 6px solid #38bdf8;
    margin-right: 8px;
}

/* Combobox dropdown liste */
QComboBox QAbstractItemView {
    background-color: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-radius: 8px;
    color: #1e293b;
    selection-background-color: #f1f5f9;
    selection-color: #0f172a;
    padding: 4px; outline: none;
}
QComboBox QAbstractItemView::item {
    padding: 9px 14px; color: #1e293b;
    background-color: #ffffff; min-height: 20px;
}
QComboBox QAbstractItemView::item:hover { background-color: #f1f5f9; color: #0f172a; }
QComboBox QAbstractItemView::item:selected { background-color: #f1f5f9; color: #0f172a; }

/* Butonlar */
QPushButton {
    border-radius: 8px; padding: 10px 20px;
    font-weight: 600; font-size: 10pt; min-height: 38px;
}

/* Mavi - Kaydet, Ekle, Ara */
#btnKaydet, #btnEkle, #btnAra {
    background-color: rgba(37,99,235,0.10);
    color: #1d4ed8; border: 2px solid #2563eb;
}
#btnKaydet:hover, #btnEkle:hover, #btnAra:hover {
    background-color: rgba(37,99,235,0.18);
}

/* Gri - Temizle */
#btnTemizle {
    background-color: rgba(100,116,139,0.08);
    color: #475569; border: 2px solid #94a3b8;
}
#btnTemizle:hover { background-color: rgba(100,116,139,0.14); color: #334155; }

/* Gri - Duzenle */
#btnDuzenle {
    background-color: rgba(100,116,139,0.08);
    color: #475569; border: 2px solid #94a3b8;
    padding: 6px 16px; font-size: 9pt; min-height: 32px; border-radius: 6px;
}
#btnDuzenle:hover { background-color: rgba(100,116,139,0.14); color: #334155; }

/* Koyu - Checkout */
#btnCikis {
    background-color: rgba(15,23,42,0.82);
    color: #f8fafc; border: 2px solid #1e293b;
    padding: 6px 16px; font-size: 9pt; min-height: 32px; border-radius: 6px;
}
#btnCikis:hover { background-color: #0f172a; color: #ffffff; }

/* Kirmizi - Sil */
#btnSil {
    background-color: rgba(239,68,68,0.08);
    color: #dc2626; border: 2px solid #ef4444;
}
#btnSil:hover { background-color: rgba(239,68,68,0.15); }

/* Amber - Yedekle */
#btnYedekle {
    background-color: rgba(217,119,6,0.08);
    color: #b45309; border: 2px solid #d97706;
}
#btnYedekle:hover { background-color: rgba(217,119,6,0.15); }

/* Mor - Rezerve Et */
#btnRezarve {
    background-color: rgba(124,58,237,0.10);
    color: #6d28d9; border: 2px solid #7c3aed;
    border-radius: 8px; padding: 10px 20px;
    font-weight: 600; font-size: 10pt; min-height: 38px;
}
#btnRezarve:hover { background-color: rgba(124,58,237,0.18); }

/* Siyah - Kara Listeye Ekle */
#btnBlacklist {
    background-color: rgba(15,23,42,0.85);
    color: #f1f5f9; border: 2px solid #0f172a;
    border-radius: 8px; padding: 10px 20px;
    font-weight: 600; font-size: 10pt; min-height: 38px;
}
#btnBlacklist:hover { background-color: #0f172a; color: #ffffff; }

/* Kirmizi kucuk - Iptal */
#btnIptal {
    background-color: rgba(239,68,68,0.08);
    color: #dc2626; border: 2px solid #ef4444;
    padding: 6px 14px; font-size: 9pt; min-height: 30px; border-radius: 6px;
}
#btnIptal:hover { background-color: rgba(239,68,68,0.15); }

/* Yesil kucuk - Checkin */
#btnCheckin {
    background-color: rgba(22,163,74,0.10);
    color: #15803d; border: 2px solid #16a34a;
    padding: 6px 14px; font-size: 9pt; min-height: 30px; border-radius: 6px;
}
#btnCheckin:hover { background-color: rgba(22,163,74,0.18); }

/* Misafir karti */
#musteriKart {
    background-color: #ffffff; border: 1px solid #f1f5f9;
    border-radius: 12px; margin: 2px 0; padding: 14px;
}
#musteriKart:hover { border-color: #e2e8f0; }
#musteriIsim { font-size: 11pt; font-weight: bold; color: #0f172a; }
#musteriOda {
    font-size: 9pt; color: #2563eb; font-weight: 600;
    background-color: rgba(37,99,235,0.08);
    border: 1px solid rgba(37,99,235,0.25);
    border-radius: 4px; padding: 1px 7px;
}
#musteriTarih { font-size: 9pt; color: #94a3b8; }

/* Rezervasyon karti */
#rezervKart {
    background-color: #fefce8; border: 1.5px solid #fde68a;
    border-radius: 12px; margin: 2px 0; padding: 14px;
}
#rezervKart:hover { border-color: #fbbf24; }

/* Odeme badge */
#odemeUyari {
    font-size: 8pt; color: #b45309; font-weight: bold;
    background-color: rgba(217,119,6,0.10);
    border: 1.5px solid #f59e0b; border-radius: 5px; padding: 3px 10px;
}
#odemeVar {
    font-size: 8pt; color: #15803d; font-weight: bold;
    background-color: rgba(34,197,94,0.10);
    border: 1.5px solid #22c55e; border-radius: 5px; padding: 3px 10px;
}
#rezervBadge {
    font-size: 8pt; color: #7c3aed; font-weight: bold;
    background-color: rgba(124,58,237,0.10);
    border: 1.5px solid #7c3aed; border-radius: 5px; padding: 3px 10px;
}

/* Oda kartlari */
#odaMusait {
    background-color: rgba(34,197,94,0.07); border: 1.5px solid #86efac;
    border-radius: 10px; padding: 10px;
}
#odaDolu {
    background-color: rgba(239,68,68,0.07); border: 1.5px solid #fca5a5;
    border-radius: 10px; padding: 10px;
}
#odaNo { font-size: 14pt; font-weight: bold; color: #0f172a; }
#odaDurumMusait { color: #16a34a; font-weight: bold; font-size: 9pt; }
#odaDurumDolu { color: #ef4444; font-weight: bold; font-size: 9pt; }

/* Tablo */
QTableWidget {
    border: 1px solid #e2e8f0; border-radius: 12px;
    background-color: #ffffff; gridline-color: #f8fafc;
    selection-background-color: #eff6ff; selection-color: #1e293b;
    alternate-background-color: #fafafa;
}
QTableWidget::item { padding: 8px 12px; border-bottom: 1px solid #f8fafc; color: #374151; }
QTableWidget::item:selected { background-color: #eff6ff; color: #1e293b; }
QHeaderView::section {
    background-color: #f8fafc; color: #64748b; padding: 10px 12px;
    border: none; border-bottom: 1px solid #e2e8f0;
    font-weight: bold; font-size: 8pt; letter-spacing: 0.5px;
}

/* Scroll */
QScrollArea { border: none; background: transparent; }
QScrollBar:vertical { border: none; background: #f1f5f9; width: 6px; border-radius: 3px; }
QScrollBar::handle:vertical { background: #cbd5e1; border-radius: 3px; min-height: 20px; }
QScrollBar::handle:vertical:hover { background: #94a3b8; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }

/* Autocomplete */
QListWidget {
    border: 1.5px solid #e2e8f0; border-radius: 8px;
    background-color: #ffffff; color: #1e293b;
}
QListWidget::item { padding: 8px 12px; border-bottom: 1px solid #f8fafc; color: #1e293b; }
QListWidget::item:hover, QListWidget::item:selected { background-color: #eff6ff; color: #1e293b; }

/* GroupBox */
QGroupBox {
    border: 1px solid #e2e8f0; border-radius: 10px;
    margin-top: 12px; padding: 8px; background-color: #ffffff;
}
QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 6px; color: #2563eb; font-weight: bold; }

/* MessageBox */
QMessageBox { background-color: #ffffff; }
QMessageBox QLabel { color: #374151; font-size: 10pt; }
QMessageBox QPushButton {
    min-width: 80px; background-color: rgba(37,99,235,0.10);
    color: #1d4ed8; border: 2px solid #2563eb;
    border-radius: 6px; padding: 6px 16px; font-weight: 600;
}
QMessageBox QPushButton:hover { background-color: rgba(37,99,235,0.18); }

/* SpinBox */
QDoubleSpinBox::up-button, QDoubleSpinBox::down-button { width: 20px; border: none; background: #f8fafc; }

/* Filtre */
#filterPanel { background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 10px; }
#bosaMessaj { color: #cbd5e1; font-size: 12pt; }

/* Durum etiketleri */
#etiketAktif {
    background-color: rgba(34,197,94,0.10); color: #15803d;
    border: 1.5px solid #22c55e; border-radius: 4px; padding: 2px 8px;
    font-size: 8pt; font-weight: bold;
}
#etiketCikis {
    background-color: rgba(239,68,68,0.08); color: #dc2626;
    border: 1.5px solid #ef4444; border-radius: 4px; padding: 2px 8px;
    font-size: 8pt; font-weight: bold;
}

#backupInfo { background-color: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 12px; }

QProgressBar { border: none; border-radius: 3px; background-color: #f1f5f9; height: 6px; }
QProgressBar::chunk { border-radius: 3px; background-color: #2563eb; }

QLabel { color: #374151; background: transparent; }
"""
