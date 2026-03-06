# Start with a standard Python image
FROM python:3.11-slim

# Install basic system tools that ML libraries like CatBoost or SciPy sometimes need to compile
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# CACHE TRICK: Copy ONLY the requirements file first
COPY requirements.txt .

# Install the heavy dependencies. 
# (This step is cached. It will only re-run in the future if you edit requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# NOW copy the rest of your project files. 
# (When you edit your Python code, Docker only rebuilds from this fast step downward)
COPY . .

# Expose the standard ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000 8501

# Set a default command. 
# (Assuming you are running a FastAPI app named 'main.py' with an instance called 'app')
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]