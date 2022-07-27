prestart:
	poetry run ./prestart.sh
.PHONY: prestart

start:
	poetry run ./run.sh
.PHONY: start

clean:
	rm -rf example.db
.PHONY: clean