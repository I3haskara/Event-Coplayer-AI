import json
import os
import subprocess
import sys
import time


class FigmaClient:
    """Lightweight helper that simulates a Figma REST payload export."""

    def __init__(self, export_dir: str = "assets", project_name: str = "Q3_Board_Audit") -> None:
        self.export_dir = export_dir
        self.project_name = project_name

    def create_design_ticket(self, risk_log):
        """
        Generates a JSON payload compatible with Figma plugin data.
        Each risk or approval becomes a sticky note node.
        """
        print("[Figma-Python] Initializing design export...")

        figma_payload = {
            "figma_file_id": "X992-mock-id",
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "nodes": [],
        }

        y_offset = 0
        for item in risk_log:
            node = {
                "type": "STICKY",
                "content": item["msg"],
                "color": "#FF4444" if item["type"] == "RISK" else "#00C851",
                "position": {"x": 0, "y": y_offset},
            }
            figma_payload["nodes"].append(node)
            y_offset += 200

        os.makedirs(self.export_dir, exist_ok=True)

        filename = f"{self.project_name}_Export.json"
        filepath = os.path.join(self.export_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(figma_payload, f, indent=4)

        print(f"[Figma-Python] Payload generated: {filepath}")
        return filepath

    def open_in_figma(self, filepath: str) -> bool:
        """
        Simulates opening the file in the OS default viewer.
        In a real app, this would be a deep link to figma.com.
        """
        abs_path = os.path.abspath(filepath)
        if sys.platform == "win32":
            os.startfile(abs_path)
        elif sys.platform == "darwin":
            subprocess.call(["open", abs_path])
        else:
            subprocess.call(["xdg-open", abs_path])
        return True
