FROM temporalio/admin-tools:1.27.2-tctl-1.18.2-cli-1.3.0

# Switch to root to install packages
USER root

# Install Python and pip (Alpine-style)
RUN apk update && apk add --no-cache python3 py3-pip

# Install FastAPI and Uvicorn
RUN pip3 install --no-cache-dir --break-system-packages fastapi uvicorn

USER temporal

# Copy your API app code
COPY . /app
WORKDIR /app

# Override default ENTRYPOINT (important!)
ENTRYPOINT []

# Start the API when the container runs
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
