# Sử dụng Ubuntu làm base image
FROM kalilinux/kali-rolling

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Cài đặt các gói cần thiết
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    curl \
    golang \
    wget \
    nmap \
    unzip \
    amass \
    && rm -rf /var/lib/apt/lists/*

# Set up Python virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Check Go version
RUN go version

# download mcp 
RUN pip install "mcp[cli]"

# Check network connectivity to GitHub
RUN curl -v https://github.com

# Thiết lập thư mục làm việc
WORKDIR /app

# Set up tools directory
RUN mkdir -p /root/tools

# Create necessary directories for the application
RUN mkdir -p /app/reports /app/templates

# Cài đặt các thư viện Python nếu có requirements.txt
RUN if [ -f requirements.txt ]; then pip3 install --no-cache-dir -r requirements.txt; fi

# Sao chép mã nguồn ứng dụng vào container
COPY . .

# Add Go binaries to PATH
ENV PATH="/root/go/bin:$PATH"

# Lệnh mặc định khi container khởi chạy
CMD ["python", "app.py"]
