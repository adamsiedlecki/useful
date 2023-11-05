Lokalizacja

```agsl
/var/log
```

- /var/log/syslog

```bash
grep "dbus-daemon" /var/log/syslog
```

```bash
grep "dbus-daemon" /var/log/syslog | less
```

grep z regexem
```bash
grep "05:3[56789]:" /var/log/syslog | less
```

Opcja -E w grep to rozszerzony silnik wyrażeń regularnych

Zliczanie liczby słów
```bash
grep "colord" /var/log/syslog | wc -w
```

