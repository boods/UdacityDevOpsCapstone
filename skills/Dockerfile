FROM python:3.7.3-stretch

# Create a working directory
WORKDIR /skills

# Copy source code to working directory
COPY . skills.py /skills/

# Install packages from requirements.txt
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run app.py at container launch
CMD ["python", "skills.py"]
