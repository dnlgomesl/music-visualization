# Instala as dependências
install:
	pip install -r requirements.txt

# Executa o projeto
run:
	python music_visualization.py

# Remove arquivos gerados pelo projeto
clean:
	rm -rf __pycache__
