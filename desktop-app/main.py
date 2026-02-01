import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QLabel, QTextEdit
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


API_URL = "http://127.0.0.1:8000/api/upload/"
USERNAME = "admin"
PASSWORD = "dhyey2323"


class DesktopApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chemical Equipment Visualizer (Desktop)")
        self.setGeometry(200, 100, 950, 740)

        # ---------------- THEME ----------------
        self.setStyleSheet("""
        QWidget {
            background-color: #0b1220;
            color: #e5e7eb;
            font-family: Segoe UI, Arial;
            font-size: 15px;   /* ⬆ increased */
        }

        QPushButton {
            background-color: #38bdf8;
            color: #020617;
            padding: 10px 18px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #0ea5e9;
        }
        QPushButton:disabled {
            background-color: #475569;
            color: #cbd5f5;
        }

        QTextEdit {
            background-color: #020617;
            border: 1px solid #1e293b;
            border-radius: 8px;
            padding: 12px;
            font-size: 14px;
        }

        QLabel {
            font-size: 15px;
        }
        """)

        # ---------------- LAYOUT ----------------
        main_layout = QVBoxLayout()
        main_layout.setSpacing(16)
        main_layout.setContentsMargins(22, 22, 22, 22)

        # Top buttons
        top_bar = QHBoxLayout()
        self.upload_btn = QPushButton("📂 Upload CSV")
        self.upload_btn.clicked.connect(self.upload_csv)

        self.save_btn = QPushButton("💾 Save Chart")
        self.save_btn.clicked.connect(self.save_chart)
        self.save_btn.setEnabled(False)

        top_bar.addWidget(self.upload_btn)
        top_bar.addWidget(self.save_btn)
        top_bar.addStretch()

        # Status
        self.status_label = QLabel("No file uploaded")

        # Output
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)

        # Chart (shared figure for bar + pie)
        self.figure = Figure(facecolor="#020617")
        self.canvas = FigureCanvas(self.figure)

        # Assemble
        main_layout.addLayout(top_bar)
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.output_box, 2)
        main_layout.addWidget(self.canvas, 3)

        self.setLayout(main_layout)

    # ---------------- UPLOAD ----------------
    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )
        if not file_path:
            return

        self.upload_btn.setEnabled(False)
        self.status_label.setText("Uploading and analyzing...")

        try:
            with open(file_path, "rb") as f:
                response = requests.post(
                    API_URL,
                    files={"file": f},
                    auth=(USERNAME, PASSWORD),
                    timeout=10
                )

            if response.status_code != 200:
                self.status_label.setText("Upload failed")
                self.upload_btn.setEnabled(True)
                return

            data = response.json()
            summary = data["summary"]
            insights = data["insights"]

            self.render_text(summary, insights)
            self.render_charts(summary)

            self.status_label.setText("Analysis completed")
            self.save_btn.setEnabled(True)

        except Exception as e:
            self.status_label.setText("Server connection error")
            print(e)

        self.upload_btn.setEnabled(True)

    # ---------------- TEXT OUTPUT ----------------
    def render_text(self, summary, insights):
        self.output_box.clear()

        self.section("System Health")
        self.output_box.append(
            f"Health Score: {summary['health_score']} ({summary['health_status']})"
        )

        self.section("Alerts")
        if summary["alerts"]:
            for a in summary["alerts"]:
                self.output_box.append(f"• {a}")
        else:
            self.output_box.append("• No active alerts")

        self.section("Recommended Actions")
        if summary["recommended_actions"]:
            for a in summary["recommended_actions"]:
                self.output_box.append(f"• {a}")
        else:
            self.output_box.append("• No actions required")
        self.section("Insights")
        for i in insights:
            self.output_box.append(f"• {i}")

    def section(self, title):
        self.output_box.append(
            f"<br><span style='color:#38bdf8; font-size:16px;'><b>{title}</b></span>"
        )

    # ---------------- BAR + PIE CHART ----------------
    def render_charts(self, summary):
        self.figure.clear()

        labels = list(summary["type_distribution"].keys())
        values = list(summary["type_distribution"].values())

        # Bar chart
        ax1 = self.figure.add_subplot(121)
        ax1.bar(labels, values, color="#38bdf8")
        ax1.set_title("Equipment Type Distribution", color="#e5e7eb")
        ax1.set_ylabel("Count", color="#e5e7eb")
        ax1.tick_params(colors="#e5e7eb")
        ax1.set_facecolor("#020617")

        # Pie chart
        ax2 = self.figure.add_subplot(122)
        ax2.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=140,
            textprops={"color": "#e5e7eb"},
        )
        ax2.set_title("Equipment Type Share", color="#e5e7eb")

        self.figure.tight_layout()
        self.canvas.draw()

    # ---------------- SAVE CHART ----------------
    def save_chart(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Chart",
            "equipment_distribution.png",
            "PNG Files (*.png)"
        )
        if path:
            self.figure.savefig(path, dpi=200, bbox_inches="tight")
            self.status_label.setText("Chart saved successfully")


# ---------------- RUN APP ----------------
app = QApplication(sys.argv)
window = DesktopApp()
window.show()
sys.exit(app.exec_())
