# SimplePyKeyLogger
## Spiegazione
Questo proggetto è stato creato per **dimostrare quanto sia semplice incappare in un virus informatico**.
I Keylogger sono dei malware molto semplici che sono in grado di "registare" tutti i caratteri inseriti dall'utente nella tastiera, sia essa fisica o virtuale, attraverso le scorciatoglie globali.
Quindi potenzialmente anche dati sensibili come passworld o numeri delle carte di credito.
Ormai sono dei malware molto rari, in quanto ormai la maggior parte degli anti virus è in grado di riconoscerli facilmente.
Su Linux è più semplice il lavoro di un keylogger, in quanto per *XOrg(il protocollo grafico di Linux)* qualsiasi programma è in grado di richiedere di inoltrarli qualsiasi evento della tastiera.
Con però Wayland, questa cosa non avviene più, in quanto per sicurezza non ha più accesso diretto ai tasti.
Il programma è molto seplice: Un'app all'apparenza normale per scaricare video da Youtube in realta installa il virus, richiedendo all'utente che vennga eseguito per il corretto funzionamento del programma


## Linguaggi utilizzati
L'intero progetto è stato realizzato **SOLO** utilizzando il linguaggio *Python* e le librerie:
* [Kivymd](https://kivymd.readthedocs.io/en/latest/), ovvero la libreria grafica per la realizzazione dell'*installer* di video.
* [Pynput](https://pypi.org/project/pynput/), ovvero per realizzare il Keylogger.
* [l'API 'ipify'](https://api.ipify.org/), per ottenere l'indirizzo ip del dispositivo.


### Versione: 0.1 BETA
Ancora non è presente il collegamento al server
