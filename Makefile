# Install your python dependencies, make sure you are inside a VENV first
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Cleans up ObjectBox folder and Python cache files if it exists
clean:
	@echo "Cleaning up..."
	rm -rf objectbox/
	rm -rf config/__pycache__
	rm -rf core/__pycache__

# Run the Streamlit application
run:
	@echo "Starting Streamlit application..."
	streamlit run app.py