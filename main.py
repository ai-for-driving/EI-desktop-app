import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QLineEdit, QTextEdit, QPushButton)

class EdgeIntelligenceApp(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle('Edge Intelligence')
        self.resize(750, 600)

        # 创建主布局
        main_layout = QHBoxLayout()

        # 创建 Communication 部分
        communication_layout = QVBoxLayout()
        self.network_interface_combo = QComboBox()
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.toggleStartButton)
        self.udp_ip_line_edit = QLineEdit()
        self.udp_port_line_edit = QLineEdit()
        self.received_messages_text_edit = QTextEdit()

        communication_layout.addWidget(QLabel("Network Interface:"))
        communication_layout.addWidget(self.network_interface_combo)
        communication_layout.addWidget(self.start_button)
        communication_layout.addWidget(QLabel("UDP Server IP:"))
        communication_layout.addWidget(self.udp_ip_line_edit)
        communication_layout.addWidget(QLabel("UDP Server Port:"))
        communication_layout.addWidget(self.udp_port_line_edit)
        communication_layout.addWidget(QLabel("Received Messages:"))
        communication_layout.addWidget(self.received_messages_text_edit)

        # 创建 Performance 和 Statistics 部分
        performance_stats_layout = QVBoxLayout()
        performance_layout = QVBoxLayout()
        statistics_layout = QVBoxLayout()

        # 算法选择框和应用按钮的水平布局
        algorithm_layout = QHBoxLayout()
        self.algorithm_combo_box = QComboBox()
        self.apply_button = QPushButton("Apply")
        algorithm_layout.addWidget(QLabel("Select Algorithm:"))
        algorithm_layout.addWidget(self.algorithm_combo_box)
        algorithm_layout.addWidget(self.apply_button)

        performance_layout.addLayout(algorithm_layout)
        performance_layout.addWidget(QLabel("Model Deployment:"))
        performance_layout.addWidget(QLabel("[Model Deployment Details]"))
        performance_layout.addWidget(QLabel("GPU Memory Usage:"))
        performance_layout.addWidget(QLabel("[GPU Memory Details]"))

        # 创建 Statistics 部分的左右排列
        def create_statistic_layout(label_text, value_text):
            layout = QHBoxLayout()
            layout.addWidget(QLabel(label_text))
            layout.addWidget(QLabel(value_text))
            return layout

        statistics_layout.addLayout(create_statistic_layout("Vehicle Request Count:", "[Count]"))
        statistics_layout.addLayout(create_statistic_layout("Inference Latency:", "[Latency]"))
        statistics_layout.addLayout(create_statistic_layout("Average Inference Latency:", "[Average Latency]"))
        statistics_layout.addLayout(create_statistic_layout("Deployment Cost:", "[Cost]"))
        statistics_layout.addLayout(create_statistic_layout("Switching Cost:", "[Cost]"))
        statistics_layout.addLayout(create_statistic_layout("Model Accuracy:", "[Accuracy]"))
        statistics_layout.addLayout(create_statistic_layout("Model Miss Rate:", "[Miss Rate]"))

        performance_stats_layout.addLayout(performance_layout)
        performance_stats_layout.addLayout(statistics_layout)

        # 将布局添加到主布局
        main_layout.addLayout(communication_layout, 1)
        main_layout.addLayout(performance_stats_layout, 2)

        self.setLayout(main_layout)

    def toggleStartButton(self):
        if self.start_button.text() == "Start":
            self.start_button.setText("Stop")
        else:
            self.start_button.setText("Start")

def main():
    app = QApplication(sys.argv)
    main_window = EdgeIntelligenceApp()
    main_window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
