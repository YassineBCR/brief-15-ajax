FROM python:3.11-alpine

# where to copy your file
WORKDIR /app

# Copy your application code
COPY . .

# Install Python dependencies from requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "api_models.py"]