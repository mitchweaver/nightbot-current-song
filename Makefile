PREFIX = ${HOME}/.local
CFLAGS = -O2 -pipe -fstack-protector-strong
BIN = nightbot-current-song.py

all: install

install:
	install -D -m 0755 ${BIN} ${DESTDIR}${PREFIX}/bin/${BIN}

uninstall:
	rm ${DESTDIR}${PREFIX}/bin/${BIN}
