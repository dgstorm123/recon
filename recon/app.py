from mcp.server.fastmcp import FastMCP
import os
import subprocess
from datetime import datetime

mcp = FastMCP("Recon_amass")

# Đường dẫn file cụ thể để lưu kết quả
OUTPUT_FILE = "/app/reports/recon_amass_results.txt"


# Tạo file nếu chưa tồn tại
def ensure_output_file_exists():
    if not os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write("=== Recon Amass Subdomain Report ===\n")

@mcp.tool()
async def enumerate_subdomains_amass(domain: str) -> str:
    """
    Sử dụng Amass để liệt kê các subdomain một cách thụ động.

    Parameters:
        domain (str): Tên miền cần quét.

    Returns:
        str: Kết quả subdomain được tìm thấy hoặc thông báo lỗi.
    """
    ensure_output_file_exists()
    results = []
    
    try:
        amass_cmd = [
            "amass", "enum",
            "-d", domain,
            "-passive",
            "-silent"
        ]
        amass = subprocess.check_output(amass_cmd,text = True)
        results.append("=== AmassAmass Results ===\n" + amass)
    except Exception as e:
        return f"[ERROR] Không thể chạy Amass: {str(e)}"

    if not results or results[0] == "":
        return f"[INFO] Không tìm thấy subdomain nào cho {domain}."
    else:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(f"\n=== Kết quả cho domain: {domain} ===\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("\n".join(results))
            f.write("\n=== Kết thúc ===\n")
        return f"[OK] Đã lưu kết quả subdomain của {domain} vào file: {OUTPUT_FILE}"
